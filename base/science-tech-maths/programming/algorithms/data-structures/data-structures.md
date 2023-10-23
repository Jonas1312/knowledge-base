# Data Structures

[Data Structures Reference](https://www.interviewcake.com/data-structures-reference)

## Trees

![](./trees.jpg)

Binary tree != binary search tree!

## Binary trees

![](./binary-tree.png)

![](./trees-dfs-bfs-complexity.png)

### Depth-first search vs breadth-first search

![](./DFS-BFS.jpg)

## LRU Cache

![](./lru-cache.png)

## Bloom filters

Used for membership tests. linear search or hashmap are slow...

A bloom filter is an array of $N$ bits. The array is proportional to the number of elements we expect to have in the set.

The bloom filter will have $K$ hash functions. Each of these $K$ hash functions should be independent and should uniformly distribute the values across the bit vector. Ideally, we want to use computationally fast hash functions with a low collision rate.

Each of these hash function return a value between $1$ and $N$.

For example, if we have $k=3$ hash functions and we get the following values for a username:

```python
for hash_fn in hash_functions:
    index = hash_fn(username)
    bit_vector[index] = 1
```

To check if an entered username is present, if any of the indices computed by the hash functions on this username is zero, it means the username is not present in the database.

If all indices are at 1, it means the username **MIGHT** be in the database. This can indeed happen if there is a collision in the hash functions. This is called a **false positive**.

To avoid false positives, we can increase the size of the bit vector. This will reduce the probability of collision.

More:

- <https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/>
- <https://llimllib.github.io/bloomfilter-tutorial/>
