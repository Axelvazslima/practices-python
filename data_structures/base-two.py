nums = list(map(int, input().split()))

counter = 0
for i in range(len(nums)):
    counter += 2**i if nums[i] != 0 else 0

print(counter)
