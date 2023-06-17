print("""This code takes a list of numbers and a target number as inputs, searches for two numbers in the list whose sum is equal to the target, and returns the index of those two numbers.""")

def find_sum():
    nums = input().split()
    target = int(input())

    for index in range(len(nums)):
        nums[index] = int(nums[index])

    indexes = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                indexes.append(i)
                indexes.append(j)

    return indexes

print(find_sum())
