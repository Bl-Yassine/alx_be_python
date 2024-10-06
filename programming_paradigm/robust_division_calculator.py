#Robust division Calculator with command line arguments

def safe_divide(numerator, denominator):
    
    try :
        numerator = float(input("Entre the numerator :"))
        denominator = float(input("Entre the denominator :"))

        try :
            numerator / denominator
        except ZeroDivisionError:
            print("You can't divise by Zero")

    except ValueError:
            print("Non numeric value")



