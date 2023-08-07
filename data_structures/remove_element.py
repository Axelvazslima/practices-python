def removeElement(nums, val):
    counter = 0
    for i in range(len(nums) -1, -1, -1):
        if nums[i] == val:
            nums.pop(i)
            nums.append("_")
        else:
            counter += 1
    return counter

print(removeElement(list(map(int, input().split())), int(input())))
