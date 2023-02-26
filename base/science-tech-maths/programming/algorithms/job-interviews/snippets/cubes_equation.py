# a^3 + b^3 = c^3 + d^3
# for int from 1 to 1000
from collections import defaultdict


# O(N²)
def main(n=100):
    hashmap = defaultdict(list)
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            res = a**3 + b**3
            hashmap[res].append((a, b))

    for res, list_of_pairs in hashmap.items():
        if len(list_of_pairs) > 2:
            print(f"{res=} {list_of_pairs}")


if __name__ == "__main__":
    main()
