str_num = input("Enter a number at least 3 digit:")

num = [int(x) for x in str_num if str_num.isdigit()]
for i in num:
    while i>0:
        print("@",end="")
        i-=1
    print("")