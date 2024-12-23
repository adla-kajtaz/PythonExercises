from typing import List

def removeDuplicates(nums: List[int]) -> int:
    if not nums:
        return 0
        
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[k] = nums[i]
            k += 1
    
    return k

nums1 = [1, 1, 2]
print(f"Input: nums = {nums1}")
print(f"Output: {removeDuplicates(nums1)}")

nums2 = [0,0,1,1,1,2,2,3,3,4]
print(f"\nInput: nums = {nums2}")
print(f"Output: {removeDuplicates(nums2)}")
