#Pesonal Finance Calculator
income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))

saving = income - expenses 

Prsv = saving * 12 + ( saving * 12 * 0.05)
print("Projected savings after one year, with interest, is: $",int(Prsv))