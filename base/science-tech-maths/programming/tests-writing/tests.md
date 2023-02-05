# Tests

Three levels:

- Unit tests
- Integration tests
- End-to-end tests

There should be a lot of unit tests, a few integration tests, and very few end-to-end tests.
Because end-to-end tests are slow, and integration tests are a good compromise.

## Unit tests

> Functions should do one thing, should do it well and should do it only.

## Property testing

For addition implementation, test for:

- x + 0 == x
- a + b == b + a
- a + 2 == a + 1 "twice"
- (a+b)+c == a+(b+c)
