def twoSum(numbers, target):
    sum_return = [1, 1]
    i, j = 0, -1
    while True:
        if numbers[i] + numbers[j] == target:
            sum_return[0] += i
            sum_return[1] += (len(numbers) + j)
            break
        if i == len(numbers) - j:
            break
        if numbers[i] + numbers[j] < target:
            i+=1
        elif numbers[i] + numbers[j] > target:
            j-=1
    return sum_return

print(twoSum(list(map(int, input().split())), int(input())))
