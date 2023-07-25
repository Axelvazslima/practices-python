def search_insert_position(nums, target):
    print("This function in the solution of a leetcode problem thats asks for the index to position the element in order in a list (if it's not already there) or it's index")
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return i + 1

print(search_insert_position([1, 3, 4, 6, 8, 10, 22, 25], int(input("Input the target number: "))))
