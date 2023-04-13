print("""\nThis code is a program that draws a special pattern called a Pascal Triangle on the screen.
The pattern has rows of numbers that start and end with 1, and the numbers in between are the sum of the two numbers above it.
The program lets you choose how many rows you want to see in the pattern, and then it creates the pattern and shows it on the screen.\n""")


def pas_triangle(num_rows):
    pascal_triangle = []
    for i in range(num_rows - 1):
        if num_rows > 1:
            rows = [1, 1]
        for j in range(len(pascal_triangle)):
            if i >= 1:
                j = pascal_triangle[i-1][j] + pascal_triangle[i-1][j + 1]
            rows.insert(-1, j)
        pascal_triangle.append(rows)
    pascal_triangle.insert(0, [1])

    print(pascal_triangle)
    return (pascal_triangle)


pas_triangle(int(input("Pick the number of rows in your Pascal Triangle: ")))
