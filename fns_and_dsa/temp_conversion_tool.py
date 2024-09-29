# temperature Conversion Tool

global FAHRENHEIT_TO_CELSIUS_FACTOR
global CELSIUS_TO_FAHRENHEIT_FACTOR 

Temperature = input("Enter the temperature to convert: ")
if not Temperature.isdigit():
    print("Invalid temperature. Please enter a numeric value.")
    
else:
    Weather = input("Is this temperature in Celsius or Fahrenheit? (C/F)")

    def convert_to_celsius(fahrenheit):
        FAHRENHEIT_TO_CELSIUS_FACTOR = (int(fahrenheit) - 32)*5/9 
        return print(f"{Temperature} is {FAHRENHEIT_TO_CELSIUS_FACTOR} °C")

    def convert_to_fahrenheit(celsius):
        CELSIUS_TO_FAHRENHEIT_FACTOR = (int(celsius) * 5/9) + 32
        return print(f"{Temperature} is) {CELSIUS_TO_FAHRENHEIT_FACTOR} °F")


    if (Weather == "C"):
        convert_to_fahrenheit(Temperature)
    elif(Weather == "F"):
        convert_to_celsius(Temperature)





