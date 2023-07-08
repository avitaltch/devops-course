print("Class 1005 Lesson 2. Avital Tchernoguz.")
# 1. Create two variables name X and Y
# a. Print “BIG” if X is bigger than Y
# b. Print “small” if X is smaller than Y
print("\nTask 1:")
x = 0
y = 0

if x > y:
    print("BIG")
elif x < y:
    print("small")
else:
    print("Equal")


# 2. Run a “for” loop 5 times.
# a. Print iteration number every time.
print("\nTask 2:")
for num in range(5):
    print(f"Iteration {num + 1}")


# 3. If else vars:
# a. Create a variable and initialize it with a number 1-4.
# b. Create 4 conditions (if-elif) which will check the variable.
# c. print the season name accordingly:
# i. 1 = summer
# ii. 2 = winter
# iii. 3 = fall
# iv. 4 = spring
print("\nTask 3:")
season = 1
if season == 1:
    print("Summer")
elif season == 2:
    print("Winter")
elif season == 3:
    print("Fall")
elif season == 4:
    print("Spring")
else:
    print("Unknown, there are only 4 seasons on earth.")


# 4. While loop:
# a. how many times will the following loop run?
# b. what will be printed last?
print("\nTask 4:")
print("a. The loop will run 10 times.")
print("b. '10' will be printed last.")


# 5. Write a program with variables holding the following
# a. Your age.
# b. First letter of your last name.
# c. Current shekels-dollar currency.
# d. Did you fly abroad (true/false)?
# e. Your apartment numbers.
# f. Print all variables.
# g. Add the currency to your age and check the result.
print("\nTask 5:")
age = 27
initial_last_name_letter = 'T'
usd_to_ils_conversion_rate = 3.73
have_flown = True
apartment_number = 15
print(age, initial_last_name_letter, usd_to_ils_conversion_rate, have_flown, apartment_number)
print(age + usd_to_ils_conversion_rate)


# 6. Create a program which uses input with the following
# a. Ask user for his phone number
# b. Print the words “phone number” and the phone number the user entered.
print("\nTask 6:")
phone_number = input("Insert phone number: ")
print(f"Phone number: {phone_number}")

# 7. Write a program with the following
# a. Method named print_hello() that prints the word “hello”.
# b. Method named calculate() which adds 5+3.2 and prints the result.
print("\nTask 7:")


def print_hello():
    print("hello")


def calculate():
    print(5 + 3.2)


# 8. Write a program with the following
# a. Method that receives your name and prints it.
# b. Method that receives a number, divide it by 2, and prints the result.
print("\nTask 8:")


def get_name():
    name_input = input("Please provide your name: ")
    print(name_input)


def split_number_by_2():
    number = input("Please insert a number to be divided by 2: ")
    print(float(number) / 2.0)


# 9. Write a program with the following:
# a. Method that receives two numbers, add them, and return the sum.
# b. Method that receives two Strings, add space between them, and return one
# spaced string.
print("\nTask 9:")


def sum_two_numbers(num1, num2):
    return num1 + num2


def space_strings(str1, str2):
    return f"{str1} {str2}"
