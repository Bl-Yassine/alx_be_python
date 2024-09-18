# Drawing Patterns with Nested Loops
row = int(input("Enter the size of the pattern:"))
inner_rows = row 
while row >0 :
    print("*"*inner_rows, end="")
    row -=1
    print()