def find_smallest_diff(num, nums):
    minimum_diff = abs(nums[0] - num)

    for i in range(len(nums)):
        calc_min_diff = abs(nums[i] - num)
        if calc_min_diff < minimum_diff:
            minimum_diff = calc_min_diff

    return minimum_diff


def find_equal_min_diffs(num, array_nums, minimun_diff):
    index_value = []
    for i in range(len(array_nums)):
        calc_minimun_diff = abs(array_nums[i] - num)
        if minimun_diff == calc_minimun_diff:
           index_value.append(f"{i}:{array_nums[i]}")

    return index_value


def int_list_converter(array):
    for i in range(len(array)):
        array[i] = int(array[i])

    return array


def main():
    n = int(input())
    array = input().split()
    array = int_list_converter(array)
    minimun_diff = find_smallest_diff(n, array)
    print(f"menor distância absoluta: {minimun_diff}")
    output = find_equal_min_diffs(n, array, minimun_diff)
    for i in range(len(output)):
        print(output[i])


main()

