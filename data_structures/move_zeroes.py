def moveZeroes(nums):
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == 0:
            nums.append(0)
            nums.pop(i)
seq = list(map(int, input().split()))
print(f"Before: {seq}")
moveZeroes(seq)
print(f"After: {seq}")
