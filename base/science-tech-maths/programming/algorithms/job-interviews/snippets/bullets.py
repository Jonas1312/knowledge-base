"""
Consider the R2 cartesian plan.
Two bullets, b1 and b2, are shot at the origin (0, 0).
There is a wall represented by the line A*x + B*y + C = 0.
You are given the speed vector of both bullets.
You must determine which bullet will hit the wall first.
PS : The bullets' speed remain constant during all their trajectory.
"""


def main():
    A = 1
    B = -10
    C = 42
    b1 = (5, 4)
    b2 = (3, 2)

    dist = abs(C) / (A ** 2 + B ** 2) ** 0.5  # distance origin to the line
    # d = abs(a*x + b*y + c) / sqrt(a² + b²)

    time1 = dist / (b1[0] ** 2 + b1[1] ** 2) ** 0.5
    time2 = dist / (b2[0] ** 2 + b2[1] ** 2) ** 0.5
    print("b2" if time2 > time1 else "b1")


if __name__ == "__main__":
    main()
