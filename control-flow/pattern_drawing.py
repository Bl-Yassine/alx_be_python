# Drawing Patterns with Nested Loops
row = int(input("Enter the size of the pattern:"))
inner_rows = row
while row > 0:
    count_rows = 1 
    while count_rows <= inner_rows:
        print("*", end="")
        count_rows +=1
    row -=1
    print()