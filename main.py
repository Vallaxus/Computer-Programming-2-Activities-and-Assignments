# Code to show print syntax.
print("Hello World")
# Code to show if statements and proper indention.
if 5 > 2:
    print("Five is greater than two.")
if 2 < 5:
    print("Two is less then five.")
# This is a comment
"""
This is a comment
written in 
multiple lines
"""
# Code that shows variables
a = "John"
b = 69
print(a)
print(b)
# Code to show casting (specify the data type of a variable)
x = str(3)  # x will be '3'
y = int(3)  # y will be 3
z = float(3)  # z will be 3.
# Code to show data type of a variable
print(type(x))
# Code to show that str variables can be declared either by using single or double quotes
x = "John"
# is the same as
x = 'John'
# Code to show that variables are case sensitive
a = 4
A = "Sally"
# A will not overwrite a
# Code to show multiple variables can have the same value
x = y = z = "Orange"
print(x)
print(y)
print(z)
# Code to show unpacking variables in the list
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
# Code to show output multiple variables, separated by a comma
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
# Code to show output multiple variables, separated by a + sign
x = "and "
y = "I "
z = "love it! "
print(x + y + z)
# I noticed that when using comma there is no need to add space after a statement
# unlike when using +, I need to put space after a statement for it not to look like this (andIlove it!).
# Code showing the best way to put 2 data types into one output
x = 5
y = "John"
print(x, y)
# Code showing Global variables.
x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()

print("Python is " + x)


# Code showing global keywords
def myfunc1():
    global x
    x = "fantastic"


myfunc1()

print("Python is " + x)

# Code showing conversion from one data type to another
x = 1  # int
y = 2.8  # float
z = 1j  # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Code showing how to do random numbers
import random

print(random.randrange(1, 100))
# Code showing multiline strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Code showiing if string
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
# Code showing if NOT string
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
# Code showing Slicing strings from the start
b = "Hello, World!"
print(b[:5])
# Code showing slicing strings from the end
b = "Hello, World!"
print(b[2:])
# Code showing negative indexing
b = "Hello, World!"
print(b[-5:-2])
# Read three numbers.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.

largest_number = max(number1, number2, number3)
min_num = min(number1, number2, number3)
# Print the result.
print("The largest number is:", largest_number)
print("The lowest number is:", min_num)
# "**" this symbol means exponential
num1 = 2 ** 5
print(num1)
print("I am Vallaxus")
