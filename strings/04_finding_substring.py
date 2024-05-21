m_str = input("Enter a string: ")
sub_str = input("Eanter sub string:")

f_result = m_str.find(sub_str)

if(f_result==-1):
    print("not found")
else:
    print("found")