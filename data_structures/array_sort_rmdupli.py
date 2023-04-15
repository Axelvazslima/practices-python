def array_sort_rmdupli():
    print("""\nThis function sort an given array of integers in non-decreasing order. Then it replaces an duplicated element with '_'.
The input should be like this: 1 3 2 4 if you want a array like [1, 3, 2, 4]. Number <Space> Number...
Finally, it counts how many unique int (not counting the '_') elements and tells you the number of non duplicate elements and the list.\n""")
    user_nums = input("Your numbers: ").split()
    nums = []

    for x in user_nums:
        a = int(x)
        if a <= 100 and a >= 1:
            nums.append(a)

    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1):
            if nums[i] == nums[j] and i != j:
                nums[j] = 101
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    for k in range(len(nums)):
        if nums[k] == 101:
            nums[k] = "_"

    for counting in range(len(nums)):
        if type(nums[counting]) == int:
            counting += 1

    if len(nums) >= 1 and len(nums) <= 3 * 10**4:
        print(counting, nums)


array_sort_rmdupli()
