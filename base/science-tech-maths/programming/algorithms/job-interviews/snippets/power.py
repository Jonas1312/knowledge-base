# a**b
def power_iter(a, b):
    ret = 1
    for _ in range(b):
        ret *= a


# O(b)
def power_rec(a, b):
    if b == 0:
        return 1
    else:
        return a * power_rec(a, b - 1)


if __name__ == "__main__":
    power_iter()
