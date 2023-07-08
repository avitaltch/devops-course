print("Class 1005 Lesson 2 Challenges. Avital Tchernoguz.")
# Challenges:
# 10.Create a nested for loop (loop inside another loop) to create a pyramid shape:
print("\nTask 10 solution 1:")
PYRAMID_CHAR = "#"
PYRAMID_SIZE = 10
for i in range(PYRAMID_SIZE):
    layer = ""
    for j in range(i):
        layer += PYRAMID_CHAR
    print(layer)

print("\nTask 10 solution 2:")
for char_count in range(PYRAMID_SIZE):
    print(PYRAMID_CHAR * char_count)

# 11.Create a nested for loop to create X shape (width is 7, length is 7):
print("\nTask 11:")
CROSS_CHAR = "#"
BLANK_CHAR = " "
CROSS_SIZE = 7

for i in range(0, CROSS_SIZE):
    line = ""
    # For every line (from 0 to 7)
    for j in range(0, CROSS_SIZE):
        # If we are on the same position from the start or the beginning draw a char
        # If we wanted to do a straight line, we would do "j == 0 or j == CROSS_SIZE - 1"
        if j == i or j == CROSS_SIZE - i - 1:
            line += CROSS_CHAR
        else:
            line += BLANK_CHAR

    print(line)


# 12.Write a program with the following:
# a. Method that gets a number from the user (using input).
# b. Method that receive the number from the first method, and computes the sum of
# the digits the integer (e.g. 25 = 7, 2+5=7)
print("\nTask 12:")


def number_input():
    return int(input('Please insert an integer (round number): '))


def sum_digits(number):
    total = 0
    while number > 0:
        total += number % 10
        number = int(number / 10)

    return total


print(sum_digits(number_input()))