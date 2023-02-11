# Python Testing

## Fixtures

Every test function will get the fixture below that sets args:

```python
@pytest.fixture(autouse=True)
def setup_tests():
    # DO stuff
    yield or return...
    # clean if needed
```

This will block all people from using requests.get in their tests:

```python
@pytest.fixture(autouse=True)
def disable_network_calls(monkeypatch):
    def stunted_get():
        raise RuntimeError("Network access not allowed during testing!")
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: stunted_get())
```

## Compare floats

```python
assert output_value == pytest.approx(expected_value)
```

## unittest (mock, patch, MagicMock)

- Mock class
- mock provides a patch() decorator that handles patching module and class level attributes within the scope of a test
- along with sentinel for creating unique objects.
- Mock and MagicMock classes are interchangeable. As the MagicMock is the more capable class it makes a sensible one to use by default.

### Mock

```python
mock = Mock()
mock.__str__ = Mock()
mock.__str__.return_value = 'fooble'
str(mock)  # prints 'fooble'
mock = Mock(return_value=42)
mock()  # 42
```

```python
book = Mock(author=Mock(first_name="Tatjana"))
print(book.author.first_name)  # "Tatjana"

book = Mock()
book.author.first_name = "Evgenij"
print(book.author.first_name)  # "Tatjana"

book = Mock()
print(book.author.first_name)  # "Tatjana"
```

```python
book = Mock()
book.author.get_full_name.return_value = ""
print(book.author.get_full_name())  # ""

book = Mock(author=Mock(get_full_name=Mock(return_value="Aleksandr Pushkin")))
print(book.author.get_full_name())  # "Aleksandr Pushkin"
```

```python
book = Mock()
book.get_review.return_value.reviewer = {"name": "Natalia"}
print(book.get_review(type="oldest").reviewer.get("name", "unknown"))  # "Natalia"
```

⚠ careful with `name` attribute, it is used to describe the Mock name:

```python
author = Mock(name="Pushkin")
print(author.name)  # <Mock name='Pushkin.name' id='140504918800992'>
```

When we are mocking a deeply nested attribute, we don’t need to explicitly create sub-Mocks at every level. As soon as we access an attribute/function/property, a new Mock will automatically be created, if none exists:

```python
book.get_review(sort="date", order="desc").reviewer.get_country().short_name  # valid
```

```python
from unittest import mock

def test_my_function():
    r = Mock()
    r.content = b'{"success": true}'
    with mock.patch('requests.get', return_value=r) as get:  # Avoid doing actual GET request
        some_function()  # Function that calls requests.get
        get.assert_called_once()
```

```python
def some_method(target, value):
    return target.apply(value)

def test_method():
    target = mock.Mock()
    some_method(target, "value")
    target.apply.assert_called_with("value")
```

### return_value

```python
m.return_value = 42
assert m() == 42
```

### side_effect

To mock a method in a class with @patch.object but return a different value each time it is called, use side_effect:

- iterator

    ```python
    mock = Mock(side_effect=[...])
    ```

- exception

    ```python
    user = Mock()
    user.social_accounts.add.side_effect = SocialAlreadyClaimedException
    ```

- as a substitute class/function (But it must be a function or a class not a different type of object and it must accept the same variables as the original function/class.)

    ```python
    create_url = Mock(side_effect=substitue_create_url)
    ```

### Mock useful functions

All useful functions:

- mock_obj.assert_called()  # doesn't work with autospec=True? just assert obj.called
- mock_obj.assert_called_once()
- mock_obj.assert_called_with(100, "Natalia")
- mock_obj.assert_called_once_with(100, "Natalia")
- mock_obj.assert_not_called()
- mock_obj.reset_mock()

When we don't care to know all function parameters or don't care to set them all, we can use ANY as a placeholder.

```python
from mock import ANY
mock_obj.assert_called_once_with(ANY, "Natalia")
```

What about when the mocked function is called more than once:

```python
from mock import call

mock_obj.assert_has_calls(
    [
        call(None, "Evgenij"),
        call(100, "Natalia"),
    ],
    any_order=True
)
```

Special attributes:

```python
>>> # Number of times you called loads():
... json.loads.call_count
1
>>> # The last loads() call:
... json.loads.call_args
call('{"key": "value"}')
>>> # List of loads() calls:
... json.loads.call_args_list
[call('{"key": "value"}')]
>>> # List of calls to json's methods (recursively):
... json.method_calls
[call.loads('{"key": "value"}')]
```

### spec

Put simply, it preconfigures mocks to only respond to methods that actually exist in the spec class. There are several ways to define specs, but the easiest is to simply pass `autospec=True` to the patch call, which will configure the Mock to behave as the object being mocked, raising exceptions for missing attributes and incorrect signatures as required.

When configuring a Mock, you can pass an object specification to the `spec` parameter. The `spec` parameter accepts a list of names or another object and defines the mock’s interface. If you attempt to access an attribute that does not belong to the specification, Mock will raise an AttributeError:

```python
book = Mock(spec=['is_weekday', 'get_holidays'])
print(item.slug)  # attribute error since "slug" is not in "spec"
```

### create_autospec

One way to implement automatic specifications is `create_autospec`.

The `mock.create_autospec` method creates a functionally equivalent instance to the provided class. What this means, practically speaking, is that when the returned instance is interacted with, it will raise exceptions if used in illegal ways.

More specifically, if a method is called with the wrong number of arguments, an exception will be raised.

```python
def test_upload_complete():
    mock_removal_service = mock.create_autospec(RemovalService)  # creates instance
    reference = UploadService(mock_removal_service)
    reference.upload_complete("my uploaded file")
    mock_removal_service.rm.assert_called_with("my uploaded file")
```

You should always use the `create_autospec` method and the `autospec` parameter with the `@patch` and `@patch.object` decorators.

### MagicMock

MagicMock is a subclass of Mock with default implementations of most of the magic methods. You can use MagicMock without having to configure the magic methods yourself:

```python
mock = MagicMock()
mock[3] = 'fish'  # MagicMock already has __getitem__ implemented, this would crash with Mock
mock.__setitem__.assert_called_with(3, 'fish')  # true
mock.__getitem__.return_value = 'result'
mock[2]  # 'result'
```

### @mock.patch

it produces a MagicMock

Generally speaking, the target is constructed like this: `<prefix><suffix><optional suffix>`:

- The prefix is: the path to the module, which will import the function/class/module we are mocking.
- The suffix is: the last part of the from .. import.. statement which imports the object we are mocking, everything after import.
- The optional suffix is: If the suffix is the name of a module or class, then the optional suffix can the a class in this module or a function in this class. This way we can mock only 1 function in a class or 1 class in a module.

See level 5 here: <https://www.ines-panker.com/2020/06/01/python-mock.html>

```python
@mock.patch('mymodule.os')
def test_rm(mock_os):
    rm("any path")  # calls rm (that calls patched os.remove inside)
    mock_os.remove.assert_called_with("any path")  # test parameters match
```

```python
@mock.patch('mymodule.os.path')
@mock.patch('mymodule.os')
def test_rm(mock_os, mock_path):
    mock_path.isfile.return_value = False  # set up the mock
    rm("any path")  # don't delete file since file doesn't exist
    assert not mock_os.remove.called
    mock_path.isfile.return_value = True  # make the file 'exist'
    rm("any path")  # should call os.remove
    mock_os.remove.assert_called_with("any path")
```

```python
from unittest import mock

def test_my_function():
    with mock.patch('module.some_function') as some_function:  # Used as context manager
        my_function()  # function that calls `some_function`

        some_function.assert_called_once()
        some_function.assert_called_with(2, 'x')

@mock.patch('module.func')  # Used as decorator
def test_my_function(some_function):
    module.func(10)  # Calls patched function
    some_function.assert_called_with(10)  # True
```

By default, `mock.patch()` will create a new mock object and use that as the replacement value. You can pass a different object using `mock.patch(new=other_object)` if want it to be used in place of a newly created mock object.

### Where to patch?

A good rule of thumb is to patch() the object where it is looked up.

```python
import my_calendar
from unittest.mock import patch

with patch('my_calendar.is_weekday'):  # lookup function in my_calendar module
    my_calendar.is_weekday()  # <MagicMock name='is_weekday()' id='4336501256'>
```

```python
from my_calendar import is_weekday  # is_weekday has local scope, it won't be patched
from unittest.mock import patch

with patch('my_calendar.is_weekday'):
    is_weekday()   # False!!! It called the real function...
```

Do this instead:

```python
from my_calendar import is_weekday
from unittest.mock import patch

with patch('__main__.is_weekday'):
    is_weekday()   # <MagicMock name='is_weekday()' id='4502362992'>
```

### @mock.patch pitfall: decorator order

When using multiple decorators on your test methods, order is important.

```python
@mock.patch('mymodule.sys')
@mock.patch('mymodule.os')
@mock.patch('mymodule.os.path')
def test_something(mock_os_path, mock_os, mock_sys):
    pass
```

```python
patch_sys(patch_os(patch_os_path(test_something)))
```

Since the patch to sys is the outermost patch, it will be executed last, making it the last parameter in the actual test method arguments.

### @mock.patch.object

Also called partial class mocking.

The only difference is that patch takes a string as the target while patch.object needs a reference. patch.object is thus used for patching individual functions of a class.

object() takes the same configuration parameters that patch() does. But instead of passing the target’s path, you provide the target object, itself, as the first parameter.

```python
@mock.patch.object(facebook.GraphAPI, 'put_object', autospec=True)
def test_post_message(mock_put_object):  # instance of class GraphAPI
    sf = simple_facebook.SimpleFacebook()
    sf.post_message(message="Hello World!")
    mock_put_object.assert_called_with(message="Hello World!")
```

```python
from unittest import mock

def test_my_function():
    with mock.patch.object(SomeClass, 'method_of_class', return_value=None) as mock_method:
        instance = SomeClass()
        instance.method_of_class('arg')
        mock_method.assert_called_with('arg')  # True
```

```python
@patch.object(requests, 'get', side_effect=requests.exceptions.Timeout)
def test_get_holidays_timeout(mock_requests):
    with pytest.raises(requests.exceptions.Timeout):
        get_holidays()
```

### Patch dictionnaries

Besides objects and attributes, you can also patch() dictionaries with patch.dict().

```python
with mock.patch.dict('os.environ', {'MY_VAR': 'testing'}):
    assert os.environ['MY_VAR'] == 'testing'
```

`os.path.dict` does not return a mocker:

```python
@mock.patch('os.getcwd', return_value='/home/')
@mock.patch('worker.print')
@mock.patch.dict('os.environ', {'MY_VAR': 'testing'})
def test_patch_builtin_dict_decorators(self, mock_print, mock_getcwd):
    # do stuff
```

### Property mocking

```python
from mock import PropertyMock

@patch.object(Square, "area", new_callable=PropertyMock)
def test(mock_square):
    # do stuff
```

### Patch constant

```python
@patch("code.MY_CONSTANT", new=3)
```

## pytest monkeypatch fixture

monkeypatch is available as a parameter in each test function, and once inside the function we can use monkeypatch.setattr() to patch our command line arguments:

```python
def test_blabla(monkeypatch, tmp_path):
    monkeypatch.setattr("sys.argv", ["pytest", "--name", "logfilename.log"])
    ## Test as usual here
```

every test function will get the fixture below that sets args:

```python
@pytest.fixture(autouse=True)
def mock_sys_args(monkeypatch):
    monkeypatch.setattr("sys.argv", ["pytest", "--name", "logfilename.log"])
```

## pytest mocker

pytest-mock is a pytest plugin thats:

- adds a mocker fixture which uses mock under the hood but with a surface area / api similar to monkeypatch.
- Basically all of the features of mock, but with the api of monkeypatch.
