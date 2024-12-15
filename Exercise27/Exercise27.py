from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
        for i in range (len(nums)):
            for j in range (i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []

nums1 = [2, 7, 11, 15]
target1 = 9
print(f"Input: nums = {nums1}, target = {target1}")
print(f"Output: {twoSum(nums1, target1)}")

nums2 = [3, 2, 4]
target2 = 6
print(f"\nInput: nums = {nums2}, target = {target2}")
print(f"Output: {twoSum(nums2, target2)}")

nums3 = [3, 3]
target3 = 6
print(f"\nInput: nums = {nums3}, target = {target3}")
print(f"Output: {twoSum(nums3, target3)}")
