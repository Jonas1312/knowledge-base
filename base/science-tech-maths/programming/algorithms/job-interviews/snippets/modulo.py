# Addition of a number of size n takes time O(n).
# Don't confuse a number and its encoding size, which is logarithmically smaller.
# for python, the algorithm used is O(n*x) where n is the length of the dividend and x is the length of the divisor


def modulo(a, b):
    div = int_div(a, b)
    return a - mult(div, b)


# O(a/b)
def int_div(a, b):
    assert a >= b
    i = 0
    while a >= b:
        a -= b
        i += 1
    return i


def mult(a, b):
    ret = 0
    for _ in range(b):
        ret += a
    return ret


def main():
    print(mult(3, 4))
    print(mult(3, 3))
    print(mult(1, 4))
    print(mult(-10, 4))
    print(int_div(4, 3))
    print(int_div(6, 3))
    print(int_div(9, 3))
    print(int_div(10, 4))
    print(int_div(4, 4))
    print(modulo(5, 4))
    print(modulo(-5, 4))  # 3 in python


if __name__ == "__main__":
    main()
