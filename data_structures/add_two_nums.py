def concat_nums(array):
    num = ''
    for i in range(len(array) - 1, -1, -1):
        num += str(array[i])
    return int(num)


def append_reversed(num):
    str_num = str(num)
    nums = []
    for i in range(len(str_num) - 1, -1, -1):
        nums.append(int(str_num[i]))
    return nums


def main(l1, l2):
    print(
        f"This codes receives two reversed lists of integers and concats them ([1, 3, 2] = 231). Theses numbers are added and the function returns this calculation in a reversed list: Each digit is a list element (2203 = [3, 0, 2, 2]).\nInspired by LeetCode's question -> '2. Add two numbers'"
    )
    num_l1 = concat_nums(l1)
    num_l2 = concat_nums(l2)
    calc = num_l1 + num_l2
    return append_reversed(calc)
