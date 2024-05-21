str = input("enter a string:")

print("For alphanumerical value: 1")
print("For alphabatical value: 2")
print("For digits value: 3")
print("For lowecase: 4")
print("For uppercase: 5")
print("For title: 6")
print("For space: 7")

opt = int(input("Enter your option:"))

if(opt==1):
    print(str.isalnum())
elif(opt==2):
    print(str.isalpha())
elif(opt==3):
    print(str.isdigit())
elif(opt==4):
    print(str.islower())
elif(opt==5):
    print(str.isupper())
elif(opt==6):
    print(str.istitle())
elif(opt==7):
    print(str.isspace())
else:
    print("you have choosen a wrong option.")