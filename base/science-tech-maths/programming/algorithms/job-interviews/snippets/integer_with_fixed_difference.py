# O(N)
def main(array, k):
    seen_integers = set()
    for x in array:
        seen_integers.add(x)
    for x in array:
        if x - k in seen_integers:
            print((x, x - k))
        # if x + k in seen_integers:
        #     print((x, x + k))


if __name__ == "__main__":
    main([1, 7, 5, 9, 2, 12, 3], k=2)
