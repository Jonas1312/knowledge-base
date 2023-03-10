# Python

- [Python](#python)
  - [Cheat Sheets](#cheat-sheets)
  - [Identity vs equality](#identity-vs-equality)
  - [Shallow and Deep Copy](#shallow-and-deep-copy)
  - [Name resolution](#name-resolution)
  - [Operators](#operators)
    - [Division and Modulo](#division-and-modulo)
    - [Short-circuiting](#short-circuiting)
  - [Unpacking](#unpacking)
  - [Error handling](#error-handling)
  - [Pass by value or reference?](#pass-by-value-or-reference)
  - [Library, Packages, Modules](#library-packages-modules)
    - [python -m](#python--m)
    - [`__init__.py`](#__init__py)
    - [`__main__.py`](#__main__py)
  - [Sequences](#sequences)
    - [Filter Map Reduce](#filter-map-reduce)
    - [Comprehension lists/dicts](#comprehension-listsdicts)
    - [Generators, Iterators](#generators-iterators)
    - [Custom sort](#custom-sort)
  - [Data structures](#data-structures)
    - [Lists](#lists)
    - [Dicts](#dicts)
    - [Sets](#sets)
    - [Frozen sets](#frozen-sets)
    - [String](#string)
    - [Data Classes](#data-classes)
      - [Namedtuple](#namedtuple)
      - [TypedDict](#typeddict)
      - [attrs](#attrs)
      - [Dataclasses](#dataclasses)
      - [Pydantinc](#pydantinc)
  - [Decorators](#decorators)
  - [Context managers (with)](#context-managers-with)
  - [Classes](#classes)
    - [Inheritance and MRO: Method Resolution Order](#inheritance-and-mro-method-resolution-order)
    - [ABC: Abstract Base Classes](#abc-abstract-base-classes)
    - [Class Decorators](#class-decorators)
    - [Metaclasses](#metaclasses)
      - [Example](#example)
  - [Numpy](#numpy)
  - [CPython](#cpython)
  - [GIL](#gil)
  - [Python ooooopssiieess](#python-ooooopssiieess)
  - [Timing code](#timing-code)
  - [Wheels](#wheels)
  - [Virtualenv](#virtualenv)
  - [Logging](#logging)
  - [Python Testing](#python-testing)
    - [Fixtures](#fixtures)
    - [Compare floats](#compare-floats)
    - [unittest (mock, patch, MagicMock)](#unittest-mock-patch-magicmock)
      - [Mock](#mock)
      - [return\_value](#return_value)
      - [side\_effect](#side_effect)
      - [Mock useful functions](#mock-useful-functions)
      - [spec](#spec)
      - [create\_autospec](#create_autospec)
      - [MagicMock](#magicmock)
      - [@mock.patch](#mockpatch)
      - [Where to patch?](#where-to-patch)
      - [@mock.patch pitfall: decorator order](#mockpatch-pitfall-decorator-order)
      - [@mock.patch.object](#mockpatchobject)
      - [Patch dictionnaries](#patch-dictionnaries)
      - [Property mocking](#property-mocking)
      - [Patch constant](#patch-constant)
    - [pytest monkeypatch fixture](#pytest-monkeypatch-fixture)
    - [pytest mocker](#pytest-mocker)

## Cheat Sheets

- [Comprehensive Python Cheatsheet](https://gto76.github.io/python-cheatsheet/)

## Identity vs equality

- use "==" for equality, "is" for identity.
- Python keeps an array of small integer objects (i.e., integers between -5 and 256):

```python
a = b = 1
print('a is b', bool(a is b))  # yes
c = d = 999
print('c is d', bool(c is d))  # false
```

## Shallow and Deep Copy

```python
list1 = [1,2]
list2 = list1        # reference
list3 = list1[:]     # shallow copy
list4 = list1.copy() # shallow copy
```

- The difference between shallow and deep copying is only relevant for __compound objects__ (objects that contain other objects, like lists or class instances):
  - A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
  - A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.
  - Use: `from copy import deepcopy ; list3 = deepcopy(list1)`

## Name resolution

LEGB scope resolution (Local -> Enclosed -> Global -> Built-in)

- Local can be inside a function or class method, for example.
- Enclosed can be its enclosing function, e.g., if a function is wrapped inside another function.
- Global refers to the uppermost level of the executing script itself
- Built-in are special names that Python reserves for itself.

## Operators

### Division and Modulo

- Modulo: `(-5) % 4 = (-2 ?? 4 + 3) % 4 = 3`
- get remainder: `quotient, remainder = divmod(a, b)`

### Short-circuiting

`a = a or []` sets `a` to `[]` if `a` is `None`

## Unpacking

- Unpacking syntax, "splat"-operators, `*args, **kwargs` ([Asterisks in Python: what they are and how to use them](https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/))
- transpose list:

```python
def transpose_list(list_of_lists):
  return [list(row) for row in zip(*list_of_lists)]
```

## Error handling

```python
try:
  print('in try:')
  print('do some stuff')
  float('abc')
except ValueError:
  print('an error occurred')
else:
  print('no error occurred')
finally:
  print('always execute finally')
```

## Pass by value or reference?

- Not by value

```python
a = [1, 2]
def f(x):
    x[0] = 5
print(a)  # prints [5, 2]
```

- Not by reference

```python
a = 3
def f(x):
    x = 5
print(a)  # prints 3
```

- Call by assignment! <https://www.jeffknupp.com/blog/2012/11/13/is-python-callbyvalue-or-callbyreference-neither/>
<img src="./pyname_pyobject.webp" alt="PyName and PyObject" width="300"/>
- the parameter passed in is actually a reference to an object (but the reference is passed by value)

## Library, Packages, Modules

- A module is a bunch of related code grouped together. A module is any python file, it can  contain submodules.
- A package is a collection of various modules. `__init__.py` contains the initialization code for the package. For example, you can control the functions you are exposing from the package by importing those specific functions into `__init__.py` file.
- A library is a collection of modules and packages.

### python -m

`python -m` lets you run modules as scripts.

If your module is just one `.py` file it'll be executed (which usually means code under `if __name__ == '__main__'`).

If your module is a directory, Python will look for `__main__.py` (next to `__init__.py`) and will run it.

### `__init__.py`

`__init__.py` is run when you import a package into a running python program.

For instance, `import idlelib` within a program, runs `idlelib/__init__.py`, which does not do anything as its only purpose is to mark the idlelib directory as a package.

On the otherhand, `tkinter/__init__.py` contains most of the tkinter code and defines all the widget classes.

You might see `__all__` in some `__init__.py` files. This is a list of names that will be imported when you do `from package import *`. It's not used very often.

### `__main__.py`

`__main__.py` is run as `__main__` when you run a package as the main program.

For instance, `python -m idlelib` at a command line runs `idlelib/__main__.py`, which starts Idle.

Similarly, `python -m tkinter` runs `tkinter/__main__.py`.

## Sequences

### Filter Map Reduce

- `filter/map/reduce(lambda x: x, sequence)`
- Mapping: Items in the new iterable are produced by calling the transformation function on each item in the original iterable.
- Filtering: Items in the new iterable are produced by filtering out any items in the original iterable that make the predicate function return false.
- Reducing: applying a reduction function to an iterable to produce a single cumulative value.

### Comprehension lists/dicts

- comprehension list faster than for loop: it doesn't have to look up the list and its append method on every iteration.

### Generators, Iterators

- An iterable is anything you???re able to loop over.
- An iterator is the object that does the actual iterating.
- iterators are also iterables and their iterator is themselves
- [Python: range is not an iterator!](https://treyhunner.com/2018/02/python-range-is-not-an-iterator/)
- 4 ways:
  1) `yield`
  2) generator `a_generator = (i for i in range(0))`
  3) class with `__iter__` and `__next__` (and `__reversed__` if reverse needed)
  4) class with `__getitem__` and iterate on it (and `__len__` if reverse needed)
- A generator IS an iterator
- 4 ways have pros and cons: `yield` and `generator` cannot be reversed

### Custom sort

- `print(sorted(x, key=functools.cmp_to_key(greater)))`

## Data structures

- Everything is immutable except `list`, `dict`, `set`
- `from collections import deque` for stacks and queues

### Lists

- `list = list + a` not in place
- `list += a` in place (same `id`)
- Out of range list slicing

```python
my_list = [1, 2, 3, 4, 5]
print(my_list[899:])  # no error!
```

- Slicing a list `a[2:4]` returns a new list but does a shallow copy. Numpy view doesn't create a new array, it creates a view...
- [] vs list() <https://towardsdatascience.com/no-and-list-are-different-in-python-8940530168b0> , [] is faster!

### Dicts

- `x = car.setdefault("model", "Bronco")` with `car` being a dictionnary. The `setdefault()` method returns the value of the item with the specified key. If the key does not exist, insert the key, with the specified value (`"Bronco"`)
- `car = collections.defaultdict(lambda:"Bronco")`
- resizing: ![](./dicts-resizing.png)

### Sets

```python
A = {0, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}
print("Union :", A | B)  # set([0, 1, 2, 3, 4, 5, 6, 8])
print("Intersection :", A & B)  # set([2, 4])
print("Difference :", A - B)  # set([8, 0, 6])
print("Symmetric difference :", A ^ B)  # set([0, 1, 3, 5, 6, 8])
```

### Frozen sets

immutables

### String

- `str1.rfind(pattern, begin=0, end=len(str1))`

### Data Classes

#### Namedtuple

- ok for small data structures
- they can be typed.

```python
Point = typing.NamedTuple("Point", [('x', int), ('y', int)])
# or the class way:
class Point(NamedTuple):
    x: int
    y: int = 1  # Set default value
```

- hard to add default values
- are immutable.

#### TypedDict

- are a regular dictionary
- typecheckers will warn you of errors.
- But at run time no check is performed.
- no way to customize magic methods (for equality, properties, etc.)

#### attrs

- More powerful than dataclasses
- Attrs supports both ways. The default is to allow positional and keyword arguments like data classes. You can enable kw-only arguments by passing kw_only=True to the class decorator.
- When you need more features (more control over the generated class or data validation and conversion), you should use attrs.

#### Dataclasses

Inspired by attrs, but smaller feature set. Added to the standard library in Python 3.7.

- TypedDict with attributes...
- mostly contain data but they can also include methods
- they reduce the boilerplate you have to write.
- Basic functionality is already implemented (equality, print, etc.).
- They can be made immutable: `@dataclass(frozen=True)`. But be careful cause attributes can be mutable...
- no type validation is done at runtime.
- Data classes support positional as well as keyword arguments.

```python
from dataclasses import dataclass

@dataclass
class DataClassCard:
    rank: str
    suit: str = 42

```

#### Pydantinc

- gives you a class which gives you both static and runtime type safety.
- data validation
- convert data (json, yaml, etc.) to your dataclass in python
- Pydantic models enforce keyword only arguments when creating new instances.
- pydantic allows you to use mutable objects like lists or dicts as default values. pydantic deep-copies the default value for each new instance.
- attrs and data classes are much faster than pydantic when no validation is needed. They also use a lot less memory.
- If you need extended input validation and data conversion, Pydantic is the tool of choice.

## Decorators

```python
def validate_summary(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        if len(data["summary"]) > 80:
            raise ValueError("Summary too long")
        return data
    return wrapper
```

```python
class MyDecorator:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
      # DO STUFF
      self.function(*args, **kwargs)
      # DO STUFF

# adding class decorator to the function
@MyDecorator
def function(arg1, arg2):
    pass

function("foo", "bar")
```

Difference between `@decorator` and `@decorator()`:

- `@pytest.fixture` is a regular decorator, equivalent to `my_decorated_method = pytest.fixture(my_method)`.
- `@pytest.fixture()` is a method that returns a decorator/callable, equivalent to `my_decorated_method = pytest.fixture()(my_method)`.
- For `pytest.fixture`, there is no difference, you can use both since `pytest.fixture()` without arguments will return the decorator `pytest.fixture`.

`functools.wraps` is used to preserve the metadata of the decorated function.

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Do something with func
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def example():
    """Docstring"""
    pass

print(example.__name__)  # example
print(example.__doc__)  # Docstring
```

## Context managers (with)

- Use context managers (with...) instead of try + finally.
- Just need a class with `__enter__` and `__exit__` implemented.

## Classes

- `super()`: [Comment marche r??ellement la fonction super() de Python](http://www.stashofcode.fr/comment-marche-fonction-super-de-python/)
- `super().__init__(args...)`
- [A Guide to Python's Magic Methods](https://rszalski.github.io/magicmethods/)
- `__repr__` vs `__str__`:
  - `__repr__` goal is to be unambiguous
  - `__str__` goal is to be readable
- `__init__` is not a constructor! It is the static method `__new__` (it is not a class method!) that creates and returns a new instance before `__init__()` is called
- `del x` doesn???t directly call `x.__del__()`:
  - `del x` decrements the reference count for x by one
  - `x.__del__()` is only called when x???s reference count reaches zero. It is called when an object is garbage collected which happens at some point after all references to the object have been deleted.
- `hasattr(self, attr_name)` to check if `instance.attr_name` exists

### Inheritance and MRO: Method Resolution Order

```python
class A():
  def foo(self):
    print("class A")
class B(A):
  pass
class C(A):
  def foo(self):
    print("class C")
class D(B,C):
  pass
D().foo()  # prints class C, searches in B first!
```

```python
class A:
  x = 1

class B(A):
  pass

class C(A):
  pass

A.x, B.x, C.x  # (1, 1, 1)
B.x = 2 # B.x is now 2
A.x, B.x, C.x  # (1, 2, 1)
A.x = 3 # A.x is now 3
A.x, B.x, C.x  # (3, 2, 3) # C.x is now 3 !!!
```

Since C.x is not defined, it searches in A, and since A.x is now 3, C.x is now 3.

### ABC: Abstract Base Classes

### Class Decorators

- staticmethod: code that belongs to a class, but that doesn't use the object itself at all
- classmethod: Class methods are methods that are
not bound to an object, but to??? a class
- abstractmethod: method defined in a base class, but that may not provide any implementation
- property: access or compute property

<https://towardsdatascience.com/why-you-should-wrap-decorators-in-python-5ac3676835f9>

### Metaclasses

Since classes are objects, you can create them on the fly, like any object.

Metaclasses are the "stuff" that creates classes. They are classes that create classes.

Well, metaclasses are what create these objects. They are the classes' classes, you can picture them this way:

```python
MyClass = MetaClass()
my_object = MyClass()
```

`type` is the metaclass Python uses to create all classes behind the scenes.

The `__class__` of any `__class__`  is `type`.

`type` has an ability: it can create classes on the fly. `type` can take the description of a class as parameters, and return a class.

`type` works this way: `type(name: str, bases: tuple, attrs: dict)`

- `name`: name of the class
- `bases`: tuple of the parent class (used for inheritance, can be left empty)
- `attrs`: dictionary containing attributes names and values

You can thus create a class with `type`:

```python
MyClass = type("MyClass", (), {'bar':True})
my_instance = MyClass()
# same as
class MyClass:
    bar = True
```

To create a metaclass, you need to subclass `type`:

```python
class MyMetaClass(type):
"""Metaclass.

Prints a message every time a class is created.

Also automatically add a 'bar' attribute set to True to every class.
"""
    def __new__(cls, name, bases, dct):
        print("Creating class %s" % name)
        dct['bar'] = True
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):  # MyClass is created by Meta
    pass

my_instance = MyClass()
print(my_instance.bar)  # True
```

#### Example

Let's create a singleton metaclass:

```python
class Singleton(type):
    _instances = {}

    def __call__(cls, name, bases, attrs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(name, bases, attrs)
        return cls._instances[cls]

class MyClass(metaclass=Singleton):
    pass

my_instance = MyClass()
my_instance2 = MyClass()
print(my_instance is my_instance2)  # True
```

## Numpy

- `np.take(A, indices=[0, -1], axis=0)` faster than `B = A[[0, -1], :]`
- `a += x` faster than `a = a + x` because inplace
- [100 numpy exercises (with solutions)](https://github.com/rougier/numpy-100)
- <https://numpy.org/devdocs/user/basics.broadcasting.html>

![](./partition_argpartition.png)

## CPython

![](cpython-interpreter.png)

## GIL

- GIL, Global Interpreter Lock
- a mutex that allows only one thread to hold the control of the Python interpreter.
- only one thread can be in a state of execution at any point in time.
- it can be a performance bottleneck in CPU-bound and multi-threaded code.
- Why GIL?
  - Python uses reference counting for memory management.
  - The problem was that this reference count variable needed protection from race conditions where two threads increase or decrease its value simultaneously.
- Imagine you have two threads, each one having to add an element to a dictionary.
- This operation, adding an element to a dictionary, is not a single operation in the underlying C code. It is a series of instructions.
- The problem is that if two threads try at the same time to add an element to that dictionary, the order in which the series of instructions (which are executed twice, once per each thread) above is interleaved may end up making a mess.
- So you need to ensure that the series of instructions is executed by only one thread at a time. How to do so?
- You use a lock. A lock is basically a guarantee that the first thread that needs to execute those instructions, will execute them without any other thread touching that dictionary until it's done adding that element.
- Now the problem moves to how granular you want the lock to be. Clearly, if one thread is acting on one dictionary, and another thread is acting on another dictionary, they don't conflict with each other and they can work in parallel, but then you need to add a lock to every dictionary. The same applies to every list, every mutable structure, external or internal. This is a lot of locks to handle and manage. And each lock occupies memory, and each lock requires time to be grabbed, and time to be released.
- So a simpler solution is to have One lock (TM). The first thread that grabs it wins, and does whatever it wants until it's done. __Even if the second thread has no intention of touching anything that the first thread is modifying, it will have to wait until the first thread is done.__

## Python ooooopssiieess

- <https://github.com/satwikkansal/wtfpython>

```python
def foo(bar=[]):  # the default value for a function argument is only evaluated once, at the time that the function is defined. Each time the function is called, the same list is used.
  bar.append("baz")
  return bar
```

## Timing code

```python
import timeit
print(timeit.timeit(my_function, number=100000))
```

- the `timeit` function requires you to pass only the name of the function (in this case `my_function`)
- the `%timeit` magic command requires the function call `my_function()` itself. `%timeit sum(range(100))`
- `python -m cProfile -s tottime your_program.py` ([Profiling and optimizing your Python code](https://toucantoco.com/en/tech-blog/tech/python-performance-optimization))

## Wheels

- <https://www.lfd.uci.edu/~gohlke/pythonlibs/>
- <http://eturnbull.ca/pythonlibs/>

## Virtualenv

```shell
virtualenv --python=c:\Python25\python.exe path/to/new/env/envname
```

## Logging

```python
import logging

logging.basicConfig(level=logging.WARNING)  # minimum level that will be logged

logging.debug('')  # won't be logged
logging.info('')  # won't be logged
logging.warning('')
logging.error('')
logging.critical("")
```

Python doesn???t provide any logging handlers by default, resulting in not seeing anything but an error from the logging package itself...

Add a handler to the root logger so we can see the actual errors:

```python
import logging

logger = logging.getLogger('my_app')  # you can use another logger name for a module of your app
logger.setLevel(logging.DEBUG)  # minimum level that will be logged
logger.addHandler(logging.StreamHandler())  # add a handler to the root logger. StreamHandler() will log to the console. You can use FileHandler() to log to a file.
```

To keep a single logger for the whole app:

```python
LOGGER = None

def get_logger():
    global LOGGER

    if LOGGER is not None:
        return LOGGER

    LOGGER = logging.getLogger("my_app")
    LOGGER.handlers.clear()  # remove all handlers
    LOGGER.addHandler(logging.StreamHandler())
    return LOGGER
```

## Python Testing

### Fixtures

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

### Compare floats

```python
assert output_value == pytest.approx(expected_value)
```

### unittest (mock, patch, MagicMock)

- Mock class
- mock provides a patch() decorator that handles patching module and class level attributes within the scope of a test
- along with sentinel for creating unique objects.
- Mock and MagicMock classes are interchangeable. As the MagicMock is the more capable class it makes a sensible one to use by default.

#### Mock

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
print(book.author.first_name)  # "Evgenij"

book = Mock()
print(book.author.first_name)  # <Mock name='mock.author.first_name' id='140504918800992'>
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

??? careful with `name` attribute, it is used to describe the Mock name:

```python
author = Mock(name="Pushkin")
print(author.name)  # <Mock name='Pushkin.name' id='140504918800992'>
```

When we are mocking a deeply nested attribute, we don???t need to explicitly create sub-Mocks at every level. As soon as we access an attribute/function/property, a new Mock will automatically be created, if none exists:

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

#### return_value

```python
m.return_value = 42
assert m() == 42
```

#### side_effect

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

#### Mock useful functions

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
????      call(None, "Evgenij"),
????      call(100, "Natalia"),
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

#### spec

Put simply, it preconfigures mocks to only respond to methods that actually exist in the spec class. There are several ways to define specs, but the easiest is to simply pass `autospec=True` to the patch call, which will configure the Mock to behave as the object being mocked, raising exceptions for missing attributes and incorrect signatures as required.

When configuring a Mock, you can pass an object specification to the `spec` parameter. The `spec` parameter accepts a list of names or another object and defines the mock???s interface. If you attempt to access an attribute that does not belong to the specification, Mock will raise an AttributeError:

```python
book = Mock(spec=['is_weekday', 'get_holidays'])
print(item.slug)  # attribute error since "slug" is not in "spec"
```

#### create_autospec

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

#### MagicMock

MagicMock is a subclass of Mock with default implementations of most of the magic methods. You can use MagicMock without having to configure the magic methods yourself:

```python
mock = MagicMock()
mock[3] = 'fish'  # MagicMock already has __getitem__ implemented, this would crash with Mock
mock.__setitem__.assert_called_with(3, 'fish')  # true
mock.__getitem__.return_value = 'result'
mock[2]  # 'result'
```

#### @mock.patch

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

#### Where to patch?

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

#### @mock.patch pitfall: decorator order

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

#### @mock.patch.object

Also called partial class mocking.

The only difference is that patch takes a string as the target while patch.object needs a reference. patch.object is thus used for patching individual functions of a class.

object() takes the same configuration parameters that patch() does. But instead of passing the target???s path, you provide the target object, itself, as the first parameter.

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

#### Patch dictionnaries

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

#### Property mocking

```python
from mock import PropertyMock

@patch.object(Square, "area", new_callable=PropertyMock)
def test(mock_square):
    # do stuff
```

#### Patch constant

```python
@patch("code.MY_CONSTANT", new=3)
```

### pytest monkeypatch fixture

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

### pytest mocker

pytest-mock is a pytest plugin thats:

- adds a mocker fixture which uses mock under the hood but with a surface area / api similar to monkeypatch.
- Basically all of the features of mock, but with the api of monkeypatch.
