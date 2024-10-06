#Robust division Calculator with command line arguments

def safe_divide(numerator, denominator):
    numerator = input("Entre the numerator :")
    denominator = input("Entre the denominator :") 
    try :
        numerator = float(numerator)
        denominator = float(denominator)

        try :
            return numerator / denominator
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")

    except ValueError:
            print("Error: Please enter numeric values only.")



