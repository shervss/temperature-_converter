# Program by: Shervin Marco Mangulabnan
# Date of Creation: September 26, 2024
# Purpose: a program that converts temperatures between Celsius and Fahrenheit

# Ask the user to input a temperature
temperature = float(input("Enter the temperature: "))

# Ask the user for the conversion type
conversion_type = input("Convert to (C)elsius or (F)ahrenheit? ").strip().upper()

# Perform the appropriate conversion
if conversion_type == 'C':
    result = (temperature - 32) * 5/9
    print(f"{temperature} Fahrenheit is {result:.2f} Celsius.")
elif conversion_type == 'F':
    result = (temperature * 9/5) + 32
    print(f"{temperature} Celsius is {result:.2f} Fahrenheit.")
else:
    print("Invalid conversion type selected. Please choose 'C' or 'F'.")
