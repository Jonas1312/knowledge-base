# A prime number is a whole number greater than 1 whose only factors are 1 and itself


# The time complexity is O(n)
def is_prime(x):
    if x in (0, 1):
        return False
    for i in range(2, int(x**0.5) + 1):  # reduced to O(sqrt (N)) thanks to this
        if x % i == 0:
            return False
    return True


# 12 = 2 × 6
# 12 = 3 × 4
# 12 = sqrt(12) × sqrt(12)
# 12 = 4 × 3
# 12 = 6 × 2
# the last two products are the reverse of the previous two, and the critical point of inversion is at sqrt (n).


def dumb_prime_gen():
    i = 2
    while True:
        if is_prime(i):
            yield i
        i += 1


def eratosthenes():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def main():
    gen = eratosthenes()
    for _ in range(15):
        print(next(gen), end=" ")


if __name__ == "__main__":
    main()
