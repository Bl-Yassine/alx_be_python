#Robust division Calculator with command line arguments



def safe_divide(numerator, denominator):
    try :
        numerator = float(numerator)
        denominator = float(denominator)
        try :
            return print(f"The result of the division is {numerator / denominator}")
        except ZeroDivisionError:
            return print("Error: Cannot divide by zero.")

    except ValueError:
            return print("Error: Please enter numeric values only.")



