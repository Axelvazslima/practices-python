# Finding the middle value in an array


def findMiddleValue():
    print("""We are finding the middle value in the numbers you put in.

    Instructions: 
    1- Enter a number
    2- hit space then put another number (Do this until you are good.)
    3- When you are done hit enter.\n""")
    yourNumInput = input("Input numbers: ").split()
    yourNum = [int(i) for i in yourNumInput]
    yourNum.sort()
    set(yourNum)
    iMiddle = len(yourNum)//2
    if len(yourNum) % 2 == 0:
        middle = (yourNum[(iMiddle) - 1] + yourNum[iMiddle]) / 2
    else:
        middle = yourNum[iMiddle]
    print(f"You middle value is {middle}")

findMiddleValue()