from functools import lru_cache


# recursive fib is O(2^N) by default O(branches^depth)
@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)


# linear complexity
def fib_iterative(n):
    if n in {0, 1}:
        return n
    a = 0
    b = 1
    for _ in range(1, n):
        a, b = b, a + b  # iterable unpacking
    return b


# there's also the matrix way, with series.
# [Finding Fibonacci numbers using Linear Algebra](https://gitlab.com/snippets/1879264)
# <https://specbranch.com/posts/fibonacci/>
