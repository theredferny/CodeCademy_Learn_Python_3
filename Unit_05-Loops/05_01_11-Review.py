single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

squares = []

for digit in single_digits:
    print(digit)
    squares = [digit ** 2 for digit in single_digits]
    cubes = [digit ** 3 for digit in single_digits]

print(squares)
print(cubes)