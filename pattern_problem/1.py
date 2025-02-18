def print_pattern(row):
    i = 0
    while i<=row:
        for j in range(0,4):
            print("*",end="")
        print("\n")
        i+=1
    
row = int(input("Enter Number of Rows:"))
print_pattern(row)