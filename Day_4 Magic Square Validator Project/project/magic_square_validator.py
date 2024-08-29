# Initialize variables to store the grid values
a1, a2, a3 = 0, 0, 0
b1, b2, b3 = 0, 0, 0
c1, c2, c3 = 0, 0, 0

# Input the 9 numbers using loops
print("Enter 9 numbers for the 3x3 grid:")
for i in range(3):
    for j in range(3):
        value = int(input(f"Enter number for position ({i+1},{j+1}): "))
        if i == 0 and j == 0:
            a1 = value
        elif i == 0 and j == 1:
            a2 = value
        elif i == 0 and j == 2:
            a3 = value
        elif i == 1 and j == 0:
            b1 = value
        elif i == 1 and j == 1:
            b2 = value
        elif i == 1 and j == 2:
            b3 = value
        elif i == 2 and j == 0:
            c1 = value
        elif i == 2 and j == 1:
            c2 = value
        elif i == 2 and j == 2:
            c3 = value

# Calculate sums of rows
row1_sum = a1 + a2 + a3
row2_sum = b1 + b2 + b3
row3_sum = c1 + c2 + c3

# Calculate sums of columns
col1_sum = a1 + b1 + c1
col2_sum = a2 + b2 + c2
col3_sum = a3 + b3 + c3

# Calculate sums of diagonals
diag1_sum = a1 + b2 + c3
diag2_sum = a3 + b2 + c1

# Check if all sums are equal
if (row1_sum == row2_sum == row3_sum == col1_sum == col2_sum == col3_sum == diag1_sum == diag2_sum):
    print("Congratulations! The grid forms a Magic Square.")
else:
    print("The grid does not form a Magic Square.")
