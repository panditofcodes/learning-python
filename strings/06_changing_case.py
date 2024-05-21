str = input("Enter a string:")

print("For uppercase 1")
print("For lowercase 2")
print("For swapcase 3")
print("For titlecase 4")
print("For capitalize 5")

opt = int(input("Enter your choice:"))

if(opt==1):
    print("changed into uppercase:",str.upper())
elif(opt==2):
    print("changed into lowercase:",str.lower())
elif(opt==3):
    print("changed into swapcase:",str.swapcase())
elif(opt==4):
    print("changed into lowercase:",str.title())
elif(opt==5):
    print("changed into capitalizecase:",str.capitalize())
else:
    print("you have choosen wrong option......")