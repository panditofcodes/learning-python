def triangle(rows):
    i = 1  
    while i <= rows:
        for j in range(1, i + 1):  
            print(i, end="")
        print()  
        i += 1  

rows = int(input("Enter number of rows: "))
triangle(rows)
