n = int(input())

nums = []
for i in range(n):
    num = int(input())
    nums.append(num)

vetores = []
for j in range(len(nums)):
    if j <= len(nums) - 3:
        vetor = (nums[j] + nums[j + 1] + nums[j + 2]) // 3
        vetores.append(vetor)

if n > 2:
    print(nums)
    print(vetores)
