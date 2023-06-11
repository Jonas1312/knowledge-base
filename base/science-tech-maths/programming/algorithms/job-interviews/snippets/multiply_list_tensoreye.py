# Implement a function that gets a list A of values as input
# It then returns a list B (same length as A) where B[i] is the product of all A[j] where j != i.
# For example: if A = [2, 1, 5, 3], then B would be [15, 30, 6, 10]
# test cases:
# default from above
# empty array
#

# B[0] =      A[1]*A[2]*A[3]*A[4]*...
# B[1] = A[0]*     A[2]*A[3]*A[4]*...

#################################################################


def implementation_1(A):
    indices_zeros_in_A = []
    cum_mult = 1
    for i, x in enumerate(A):
        if x:
            cum_mult *= x
        else:
            indices_zeros_in_A.append(i)

    if len(indices_zeros_in_A) > 1:
        B = [0] * len(A)
    elif len(indices_zeros_in_A) == 1:
        B = [0] * len(A)
        B[indices_zeros_in_A[0]] = cum_mult
    else:
        B = [cum_mult] * len(A)
        for i, x in enumerate(A):
            B[i] //= x
    return B


def implementation_2(A):
    # cum_prod_from_left: {              1,         a[0],    a[0]*a[1],    a[0]*a[1]*a[2],  }
    # cum_prod_from_right:{ a[1]*a[2]*a[3],    a[2]*a[3],         a[3],                 1,  }
    # then prod
    N = len(A)

    cum_prod_from_left = [0] * N
    cum_prod_from_right = [0] * N
    cum_prod_from_left[0] = 1
    cum_prod_from_right[-1] = 1

    B = [0] * N

    for i in range(1, N):
        cum_prod_from_left[i] = cum_prod_from_left[i - 1] * A[i - 1]
        cum_prod_from_right[N - i - 1] = cum_prod_from_right[N - i] * A[N - i]

    print(f"{cum_prod_from_left=}")
    print(f"{cum_prod_from_right=}")

    for i, _ in enumerate(B):
        B[i] = cum_prod_from_left[i] * cum_prod_from_right[i]

    return B


def main():
    print(implementation_1([2, 1, 5, 3]))  # [15, 30, 6, 10]
    print(implementation_1([2, 0, 5, 3]))  # [0, 30, 0,0]
    print(
        implementation_1([2, 0, 5, 0, 5, 8, 9, 3, 5, 4, 7, 6])
    )  # two zeros, so: B = [0]*12
    print("-" * 42)
    print(implementation_2([2, 1, 5, 3]))  # [15, 30, 6, 10]
    print(implementation_2([2, 0, 5, 3]))  # [0, 30, 0,0]
    print(
        implementation_2([2, 0, 5, 0, 5, 8, 9, 3, 5, 4, 7, 6])
    )  # two zeros, so: B = [0]*12


if __name__ == "__main__":
    main()
