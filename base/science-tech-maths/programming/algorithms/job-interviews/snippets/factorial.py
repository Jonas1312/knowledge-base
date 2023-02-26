# O(N)
def factorial_iter(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


# even if it's recursive, the complexity is still O(N)
def factorial_rec(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return n * factorial_rec(n - 1)


if __name__ == "__main__":
    print(factorial_iter(4) == 24)
    print(factorial_rec(4) == 24)
    print(factorial_iter(6) == 720)
    print(factorial_rec(6) == 720)
