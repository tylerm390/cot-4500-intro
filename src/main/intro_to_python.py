import numpy as np

# Part One
I = np.identity(3, int)
for row in I:
    print(*row)
print()

# Part Two
A = 3 * np.ones((3, 3), int) - 2 * I
for row in A:
    print(*row)
print()

B = np.delete(A, -1, axis=1)
for row in B:
    print(*row)