from typing import List


"""def twoSum(nums, target):
    result = []

    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == target:
                result.extend([i, j])
                return result"""


def twoSum(nums: List[int], target: int) -> List[int]:
    hash_table = {}

    for i in range(len(nums)):
        if nums[i] in hash_table:
            return [i, hash_table[nums[i]]]
        hash_table[target - nums[i]] = i


print(twoSum([2, 7, 11, 15], 9))


assert twoSum([2, 7, 11, 15], 9) == [1, 0]
