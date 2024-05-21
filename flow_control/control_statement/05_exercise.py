n1 = float(input("Enter 1st number:"))
n2 = float(input("Enter 2nd number:"))
n3 = float(input("Enter 3rd number:"))

if(n1>n2 and n1 > n3):
    print(n1,"is biggest number.")
elif(n2>n1 and n2>n3):
    print(n2,"is biggest number.")
else:
    print(n3,"is biggest number")