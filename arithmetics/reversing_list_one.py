def reverse_list_one():
    print(f"Input 20 numbers in a list then it returns you the reversed list.")

    nums = []
    for i in range(5):
        num = int(input())
        nums.append(num)
        
    return nums[::-1]

