n=2
print("start writting......")
while n>1:
    f = open("abc.txt","a")
    msg = input()
    f.write(msg+" ")
    f.close()
    f = open("abc.txt","r")
    print(f.read())