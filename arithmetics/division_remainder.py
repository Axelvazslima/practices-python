def division_remainder(a, b):
    print("This program returns you the remainder of the division between two values. Pass them as arguments.")
    try:
        return int(a % b)
    except:
        return "Invalid data type."

