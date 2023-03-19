# You need to write a function that can only be called at most N times within any 1 minute window.
# For example, it can be called at most 10 times in a minute.
# If the function is called more than N times it should throw an exception.
# The function should have expected O(1) performance.

# SOLUTION
# Looking at the use cases the only two are for a stack and a queue.
# Can we use either of those to keep track of how many times a function has been called in the last minute?
# Yes! What we can do is keep a queue that has one entry for each time the function was called within the last minute.
# Whenever the function is called, we remove all entries from the queue that were inserted more than a minute ago.
# If the queue still has a length greater than N, we throw an exception.
# Otherwise we add a new entry to the queue with the current time.
# By keeping track of the length of the queue with a counter, we can determine with O(1) expected time, this function will have O(1) expected performance.

import time as time_lib
from typing import Callable

PROGRAM_START_TIME = time_lib.time()


def time() -> float:
    return time_lib.time() - PROGRAM_START_TIME


class RateLimiter:
    def __init__(self, nb_times: int, time_window: float, func: Callable) -> None:
        self.nb_times = nb_times
        self.time_window = time_window
        self.func = func

        self.queue = []

    def wrapper(self, *args, **kwargs):
        self.queue.append(time())
        self.queue = [t for t in self.queue if time() - t <= self.time_window]
        if len(self.queue) > self.nb_times:
            raise Exception("Too many calls")
        return self.func(*args, **kwargs)


def rate_limiter(nb_times: int, time_window: float):
    def decorator(func):
        rate_limiter_instance = RateLimiter(nb_times, time_window, func)
        return rate_limiter_instance.wrapper

    return decorator


@rate_limiter(nb_times=5, time_window=1)
def function_does_something():
    print("Called at: ", time())
    time_lib.sleep(0.35)


def main():
    for _ in range(20):
        function_does_something()


if __name__ == "__main__":
    main()
