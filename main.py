from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []

# nums = [3,3]
# target = 6

# print(twoSum(nums, target))