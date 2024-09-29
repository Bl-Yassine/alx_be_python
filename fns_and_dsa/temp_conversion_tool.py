# temperature Conversion Tool

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

Temperature = input("Enter the temperature to convert: ")
if not Temperature.isdigit():
    print("Invalid temperature. Please enter a numeric value.")
    
else:
    Weather = input("Is this temperature in Celsius or Fahrenheit? (C/F)")

    def convert_to_celsius(fahrenheit):
        FtoC = (int(fahrenheit) - 32)*FAHRENHEIT_TO_CELSIUS_FACTOR
        return print(f"{Temperature} is {FtoC} °C")

    def convert_to_fahrenheit(celsius):
        CtoF = (int(celsius) * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
        return print(f"{Temperature} is) {CtoF} °F")


    if (Weather == "C"):
        convert_to_fahrenheit(Temperature)
    elif(Weather == "F"):
        convert_to_celsius(Temperature)





