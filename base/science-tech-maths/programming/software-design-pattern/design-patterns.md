# Design patterns

- decorators
- singleton (keep one instance of a class, for a DB, logger, etc.)
- iterator
- Layered pattern (multiple levels of abstraction)
- clients / server
- master slave
- MVC ![](model-view-controller.jpeg)

<https://github.com/faif/python-patterns>

## Dependency injection

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

## The clean architecture / Hexagonal architecture / Onion architecture

The clean architecture is a way to structure your code in a way that it is independent of frameworks, databases, etc. It is a way to make your code more testable, and more maintainable.

The clean architecture is composed of 4 layers.

![](CleanArchitecture.jpg)

Each of these architectures produce systems that are:

- Independent of Frameworks.
- Testable.
- Independent of UI. The UI can change easily, without changing the rest of the system.
- Independent of Database. You can swap out Oracle or SQL Server, for Mongo, BigTable, CouchDB, or something else. Your business rules are not bound to the database.
- Independent of any external agency.

The further in you go in the architecture, the more stable and abstract the components become. The more high level components are at the center, and the more low level components are at the edges: **the outer circles are mechanisms. The inner circles are policies.**

### The Dependency Rule

This rule says that source code dependencies can only point inwards.
Nothing in an inner circle can know anything at all about something in an outer circle.
In particular, the name of something declared in an outer circle must not be mentioned by the code in the an inner circle.
That includes, functions, classes. variables, or any other named software entity.

For example:

```python
class MyService:
    def __init__(self, repository):
        self._repository = repository

    def do_something(self):
        return self._repository.get("http://www.google.com")
```

The `MyService` class is in the inner circle. The `repository` is in the outer circle.
The `MyService` class depends on the `repository` class, but the `repository` class does not depend on the `MyService` class.

We don’t want anything in an outer circle to impact the inner circles. We don’t want SQL, or HTML, or the database, or the web, or any other mechanism to impact the inner circles. This allows us to keep those mechanisms at arms length from the business rules.

### The Entities

It's the core of the application. It contains the business rules. It is the most abstract layer of the application.

### The Use Cases

It contains the application specific business rules. It is the layer where the application is interacting with the user. It is the layer where the application is interacting with external systems (databases, web services, etc.). It is the layer where the application is interacting with the entities.

### In Python

In python we will design our repository with a domain and adapters folders.

The domain folder will contain the entities and the use cases. It cannot import anything from the adapters folder except for type hints.

The adapters folder will contain the implementation of the use cases, and the implementation of the repositories. It cannot import anything from the domain folder.

You can also define the entrypoint in src/your_app_name/main.py. This file will import the use cases from the domain folder, and the repositories from the adapters folder. You can also define several entrypoints in the entrypoints folder.
