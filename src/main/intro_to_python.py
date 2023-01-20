# Intro to Github and Python
# COT4500 Spring 2023
# Tyler Marks, ty549882

import numpy as np

# Part One: Create a 3 by 3 Identity matrix using the numpy 'identity' function
I = np.identity(3, int)
for row in I:
    print(*row)
print()

# Part Two: To get a matrix where the diagonal is ones and everything else is threes,
#           create a matrix of all 3's then subtract 2 from the diagonal
A = 3 * np.ones((3, 3), int) - 2 * I
for row in A:
    print(*row)
print()

# Part Three: To get this matrix, take the part two matrix and use the numpy delete function
B = np.delete(A, -1, axis=1)
for row in B:
    print(*row)