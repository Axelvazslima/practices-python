nums = input().split()

for i in range(len(nums)):
    nums[i] = int(nums[i])

delta = int(input())

pares = 0
indexes = []
for j in range(len(nums) - 1):
    if nums[j] * delta == nums[j + 1] or nums[j] / nums[j + 1] == delta:
        pares += 1
        indexes.append(j)

print(f"{pares} par(es)")

for k in range(len(indexes)):
    print(nums[indexes[k]], nums[indexes[k] + 1])

