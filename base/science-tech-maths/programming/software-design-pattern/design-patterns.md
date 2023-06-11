# Design patterns

- decorators
- singleton (keep one instance of a class, for a DB, logger, etc.)
- iterator
- Layered pattern (multiple levels of abstraction)
- clients / server
- master slave
- MVC ![](model-view-controller.jpeg)

<https://github.com/faif/python-patterns>

## Depandency injection

Dependency injection is a technique whereby one object (or static method) supplies the dependencies of another object. A dependency is an object that can be used (a service). An injection is the passing of a dependency to a dependent object (a client) that would use it. The service is made part of the client's state. Passing the service to the client, rather than allowing a client to build or find the service, is the fundamental requirement of the pattern.

In other terms, this pattern allows to "inject" a dependency into a class, instead of letting the class create the dependency.

```python
class Client:
    def __init__(self, service):
        self.service = service

    def do_something(self):
        return self.service.get("http://www.google.com")
```

Instead of:

```python
class Client:
    def __init__(self):
        self.service = Service()

    def do_something(self):
        return self.service.get("http://www.google.com")
```
