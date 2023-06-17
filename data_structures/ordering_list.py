def reversing_lists(wanted_list):
    sort_question = int(input("""\nThis function receives a list as an argument and returns it but reversed.
It uses the bubblesort algorithm.
Do you want it reversed, sorted in decrescent order or sorted in crescent order?

Type, respectively; 1, 2 or 3: """))
    
    match sort_question:
        case 1:
            wanted_list = wanted_list[::-1]
        case 2:
            wanted_list.sort()
            wanted_list = wanted_list[::-1]
        case 3:
            wanted_list.sort()
    return wanted_list


print(reversing_lists([1, 4, 6, 8, 7]))
