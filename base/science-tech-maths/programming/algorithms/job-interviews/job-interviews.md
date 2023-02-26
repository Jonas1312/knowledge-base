# Technical Interview

## Algebra

- $1+...+N=\frac{N(N+1)}{2}$
- $2^{0}+... +2^{N} = 2^{N+1}-1$
- Arithmetic series: $2 + 5 + 8 + 11 + 14=5\frac{2+14}{2}=40$
- Digit length (for example: `digitLength(69420) == 5` and `digitLength(1337) == 4`): `math.log10(N)`!

  ```python
  def digit_length(n):
    return 1 if n == 0 else (math.floor(math.log10(n)) + 1)
  ```

## Bit Tricks

- Swap two variables using XOR (doesn't work for pointers!)
- `(n & (n - 1)) == 0` True if only one bit is set to 1, also means n is a power of 2.

## Permutations

- Number of distinct permutation a string can have: `ybghjhbuytb`, number of character is `11` and here `h` and `y` are repeated `2` times whereas `b` is repeated `3` times => $\frac{11!}{2!2!3!}=1663200$

## More

- <https://www.techinterviewhandbook.org/>
- [Everything you need to know to get the job.](https://github.com/kdn251/interviews)
- <https://neetcode.io/>
- <https://www.techinterviewhandbook.org/grind75>
- Grind 75 is a modern version of Blind 75 that you can customize.
- <https://www.interviewbit.com/python-interview-questions/>
- <https://luminousmen.com/post/python-interview-questions-junior>
- <https://luminousmen.com/post/python-interview-questions-middle>
- <https://luminousmen.com/post/python-interview-questions-senior>
- <https://realpython.com/quizzes/>
- <https://github.com/donnemartin/interactive-coding-challenges>
- <https://store.lerner.co.il/ace-python-interviews>
- <https://rushter.com/blog/>
