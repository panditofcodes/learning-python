def triangle(rows): 
    while rows > 0:  
        for j in range(rows):  
            print("*", end="")
        print()  
        rows -= 1  

rows = int(input("Enter number of rows: "))
triangle(rows)
