n = int(input("Enter number of rows:"))

for i in range(0,n):
    print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
