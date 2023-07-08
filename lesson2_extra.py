# Print First 10 natural numbers using while loop
x = 0
while x < 10:
    x += 1
    print(x)


# Write a program to print the following number pattern using a loop
# Expected Output:
#     1
#     1 2
#     1 2 3
#     1 2 3 4
#     1 2 3 4 5
STEP_SIZE = 5
for i in range(1, STEP_SIZE + 1):
    layer = ""
    for j in range(i):
        layer += f'{j + 1} '
    print(layer.rstrip(' '))


# Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number
# For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)
# Expected Output:
#       Enter number 10
#       Sum is:  55
number = int(input("Enter a number: "))
additive_result = 0
for i in range(1, number + 1):
    additive_result += i
print(f"Additive Factorial: {additive_result}")


# Print list in reverse order using a loop
# Given: list1 = [10, 20, 30, 40, 50]
# Expected output:
#    50
#    40
#    30
#    20
#    10
listToPrintInReverse = [10, 20, 30, 40, 50]
# Solution 1:
listLength = len(listToPrintInReverse)
print("Reverse Solution 1")
for i in range(listLength):
    print(listToPrintInReverse[listLength - i - 1])

# Solution 2:
print("Reverse Solution 2")
for i in reversed(listToPrintInReverse.copy()):
    print(i)

# Solution 3
print("Reverse Solution 3")
for i in range(listLength - 1, -1, -1):
    print(listToPrintInReverse[i])
