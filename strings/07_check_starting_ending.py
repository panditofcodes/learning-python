m_str = input("Enter main string:")
sub_str = input("Enter sub string that you want to check:")
print("For starting: 1")
print("For ending: 2")
opt = int(input("Choose your option:"))
if(opt==1):
    print("Checking starting:",m_str.startswith(sub_str))
elif(opt==2):
    print("Checking ending:",m_str.endswith(sub_str))
else:
    print("You have choose wrong option")