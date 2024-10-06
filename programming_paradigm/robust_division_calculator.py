#Robust division Calculator with command line arguments

numerator = input("Entre the numerator :")
denominator = input("Entre the denominator :") 

def safe_divide(numerator, denominator):
    try :
        numerator = float(numerator)
        denominator = float(denominator)

        try :
            print(f"The result of the division is {numerator / denominator}")
            return numerator / denominator
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")

    except ValueError:
            print("Error: Please enter numeric values only.")



