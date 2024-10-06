#Robust division Calculator with command line arguments

def safe_divide(numerator, denominator):
    numerator = float(input("Entre the numerator :"))
    denominator = float(input("Entre the denominator :")) 
    try :
        numerator = float(numerator)
        denominator = float(denominator)

        try :
            numerator / denominator
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")

    except ValueError:
            print("Non numeric value")



