# Temperature Conversion Tool

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

Temperature = input("Enter the temperature to convert: ")

try:
    Temperature = float(Temperature)
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
else:
    Weather = input("Is this temperature in Celsius or Fahrenheit? (C/F) ")

    def convert_to_celsius(fahrenheit):
        FtoC = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
        print(f"{fahrenheit}°F is {FtoC:.2f}°C")

    def convert_to_fahrenheit(celsius):
        CtoF = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
        print(f"{celsius}°C is {CtoF:.2f}°F")

    if Weather.upper() == "C":
        convert_to_fahrenheit(Temperature)
    elif Weather.upper() == "F":
        convert_to_celsius(Temperature)
    else:
        print("Invalid option. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
