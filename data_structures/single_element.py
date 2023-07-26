def singleNumber(self, nums: List[int]) -> int:
    print("LeetCode exercise to find the only non-duplicated element in a given array. *Linear time complexity.")
    for i in range(len(nums)):
        if nums.count(nums[i]) == 1:
            return nums[i]
    return 0


