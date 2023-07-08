from flask import Flask

# 1. Write the following code: a = 1/0
# a. Build a corresponding try-except block to avoid exception
try:
    a = 1/0
except ZeroDivisionError as e:
    print(e)

# 2. Is the following code legal?
try:
    x = 1
finally:
    print("finally")
## Yes, this is legal, however, I'd add an except + print + pass for logging

# 3. What exception types can be caught by the following handler?
# except:
# print("found an error")
# Catches all the exceptions, as we don't provide a type.

# 4. What is wrong with using the above type of exception handler?
# We should divide exception types to handle each type of error in a fitting manner.
# For example when writing to a file and getting a not found exception, we can create it.

# 5. What exceptions can be caught by the following handlers?
# a. except IOError - Anything related to IO operations on the system, ex. trying to write to a locked file.
# b. except ZeroDivisionError - When we try to divide by zero, ex. task 1.


TEXTS_FILE = 'words.txt'
# 6. Create a text file named “words.txt” programmatically
# a. Write your name into the file
print(f"\nWriting name to {TEXTS_FILE}.")
with open(TEXTS_FILE, 'w') as file:
    file.write("Avital\n")


# 7. Read your file content and print it
print(f"\nReading from {TEXTS_FILE}")
with open(TEXTS_FILE) as file:
    print(file.read())

# 8. Write Hebrew content into your text file and print its content programmatically.
with open(TEXTS_FILE, 'a', encoding="UTF-8") as file:
    file.write("תוכן בעברית")

with open(TEXTS_FILE, 'r', encoding="UTF-8") as file:
    print(file.read())

# 9. Create a Flask application which listens to port 30000 and has 2 routes:
# a. /content - which returns the content of any txt file and status code 200 (e.g:
# localhost:4000/content).
# b. /register - which writes the word “hello” into any txt file and return “success” and
# status code 201 as a response (e.g: localhost:4000/register).
app = Flask(__name__)
@app.route('/content')
def getFileContent():
    file = open('words.txt')
    return_data = file.read()
    file.close()
    return return_data, 200

@app.route("/register")
def writeToFile():
    with open(TEXTS_FILE, 'a') as file:
        file.write('\nHello')
    return "Success", 201

app.run(host='127.0.0.1', debug=True, port=4000)