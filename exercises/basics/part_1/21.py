num_grp = (1,2,3,4,5,6,7,8,9,10)
num = int(input("Enter a number:"))
if num in num_grp :
    print(f"{num} in range")
else:
    print(f"{num} out of range")