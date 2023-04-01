# Read an integer N. This N will be the number of integer numbers X that will be read.

# Print how many these numbers X are in the interval [10,20] and how many values are out of this interval.

# Input: The first line of input is an integer N (N < 10000), that indicates the total number of test cases.
# Each case is an integer number X (-107 < X < 107).

# Output: For each test case, print how many numbers are in and how many values are out of the interval.

N = int(input())
X = [int(input()) for k in range(N)]
In = 0
Out = 0
for j in X:
    if j > -10**7 and j < 10**7:
        if j >= 10 and j <= 20:
            In+=1
        else:
            Out +=1
print(f"{In} in\n{Out} out")