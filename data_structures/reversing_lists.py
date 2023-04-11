def reversing_lists(wanted_list):
    sort_question = int(input("""\nThis function receives a list as an argument and returns it but reversed.
It uses the Two pointer method, which makes it more efficient and faster.
* it's up to you, but the list should be sorted.

Do you want it sorted? >> 0 for 'no', 1 for 'yes': """))
    if sort_question:
        wanted_list.sort()
    i = 0
    j = len(wanted_list)-1
    print(i, j)
    while i < j:
        wanted_list[i], wanted_list[j] = wanted_list[j], wanted_list[i]
        i += 1
        j -= 1
    return wanted_list
