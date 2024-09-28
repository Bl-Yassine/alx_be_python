from datetime import timedelta,datetime

def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return print(f"Current date and time: {current_date}")

display_current_datetime()
DaysAdd = int(input("Enter the number of days to add to the current date:"))
def calculate_future_date():
    future_date = (datetime.now() + timedelta(days=DaysAdd)).strftime("%Y-%m-%d")
    return print(f"Future date: {future_date}")

calculate_future_date()