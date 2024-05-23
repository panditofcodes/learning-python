import os

file_name = input("Enter a filename:")

if(os.path.isfile(file_name)):
    print("Yes found!")
else:
    print("Not found!")