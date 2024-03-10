# Code for BMI
# def bmi(user_height,user_weight):
"""
user_height = float(input("Enter your height in meters: "))
user_weight = float(input("Enter your weight in kilograms: "))
bmi = user_weight / user_height ** 2
print("Your BMI is", bmi)
"""
# code for simple calculator
"""while True:
    n1 = float(input('Enter the 1st number: '))
    n2 = float(input('Enter the 2nd number: '))
    op = input('Enter the operator: ')

    if op == "+":
        print("The sum is:", n1 + n2)
    elif op == "-":
        print("The difference is:", n1 - n2)
    elif op == "/":
        if n2 != 0:
            print("The quotient is:", n1 / n2)
        else:
            print("Error: Division by zero!")
    elif op == "*":
        print("The product is:", n1 * n2)
    else:
        print("Invalid operator")

    choice = input("Do you want to continue? (y/n): ").lower()
    if choice.lower() != 'y':
        break
"""

import math

def calculate_bmi():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    bmi = weight / (height ** 2)
    print("Your BMI is:", bmi)

def calculate_electricity_bill():
    consumption = float(input("Enter your electricity consumption in kWh: "))
    rate_per_unit = float(input("Enter the rate per kWh: "))
    bill = consumption * rate_per_unit
    print("Your electricity bill is:", bill)

def calculate_velocity():
    distance = float(input("Enter the distance in meters: "))
    time = float(input("Enter the time in seconds: "))
    velocity = distance / time
    print("The velocity is:", velocity, "m/s")

def calculate_acceleration():
    initial_velocity = float(input("Enter the initial velocity in m/s: "))
    final_velocity = float(input("Enter the final velocity in m/s: "))
    time = float(input("Enter the time in seconds: "))
    acceleration = (final_velocity - initial_velocity) / time
    print("The acceleration is:", acceleration, "m/s^2")

def calculate_volume():
    radius = float(input("Enter the radius of the sphere in meters: "))
    volume = (4 / 3) * math.pi * (radius ** 3)
    print("The volume of the sphere is:", volume, "cubic meters")

def calculate_area():
    radius = float(input("Enter the radius of the circle in meters: "))
    area = math.pi * (radius ** 2)
    print("The area of the circle is:", area, "square meters")

def calculate_circumference():
    radius = float(input("Enter the radius of the circle in meters: "))
    circumference = 2 * math.pi * radius
    print("The circumference of the circle is:", circumference, "meters")

def binary_to_decimal():
    binary_number = input("Enter a binary number: ")
    decimal_number = int(binary_number, 2)
    print("The decimal equivalent is:", decimal_number)

def octal_to_decimal():
    octal_number = input("Enter an octal number: ")
    decimal_number = int(octal_number, 8)
    print("The decimal equivalent is:", decimal_number)

functions = {
    "bmi": calculate_bmi,
    "electricity": calculate_electricity_bill,
    "velocity": calculate_velocity,
    "acceleration": calculate_acceleration,
    "volume": calculate_volume,
    "area": calculate_area,
    "circumference": calculate_circumference,
    "binary": binary_to_decimal,
    "octal": octal_to_decimal
}

while True:
    print("Choose what to calculate:")
    print("1. BMI")
    print("2. Local Electricity Bill")
    print("3. Velocity")
    print("4. Acceleration")
    print("5. Volume of Sphere")
    print("6. Area of Circle")
    print("7. Circumference of Circle")
    print("8. Binary to Decimal Conversion")
    print("9. Octal to Decimal Conversion")
    choice = input("Enter your choice (1-9): ")

    if choice.isdigit() and 1 <= int(choice) <= 9:
        function_key = list(functions.keys())[int(choice) - 1]
        functions[function_key]()
    else:
        print("Invalid choice!")

    repeat = input("Do you want to continue? (y/n): ").lower()
    if repeat.lower() != 'y':
        break
