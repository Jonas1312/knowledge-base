def main(A, B):
    pointer_a = pointer_b = 0
    while pointer_a < len(A) and pointer_b < len(B):
        if B[pointer_b] < A[pointer_a]:
            pointer_b += 1
        elif B[pointer_b] > A[pointer_a]:
            pointer_a += 1
        else:
            print(A[pointer_a])
            pointer_a += 1
            pointer_b += 1


if __name__ == "__main__":
    main(A=[13, 27, 35, 40, 49, 55, 59], B=[12, 35, 39, 40, 55, 58, 60])
