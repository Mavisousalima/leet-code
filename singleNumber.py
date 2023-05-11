"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1
"""

# What is the time complexity of my function?


def singleNumber(nums):
    return [n for n in nums if nums.count(n) == 1][0]


print(singleNumber([2, 2, 1]))
print(singleNumber([4, 1, 2, 1, 2]))
