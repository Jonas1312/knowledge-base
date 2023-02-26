# Given an array of integers where each value `1 <= x <= len(array)`
# write a function that finds all the duplicates in the array

# Solution: To avoid using extra space, we flag which elements we've seen
# before by negating the value at indexed at that value in the array.
