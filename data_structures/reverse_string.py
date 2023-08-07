def reverseString(s):
    i, j = 0, -1
    while True:
        if i >= len(s) + j:
            break
        s[i], s[j] = s[j], s[i]
        i+=1
        j-=1

string = list(input())
print(f"Before {string}")
reverseString(string)
print(f"After: {string}")
