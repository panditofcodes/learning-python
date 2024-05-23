import os,sys
file_name = input("Enter file name: ")
if os.path.isfile(file_name):
    print("Form if block:")
    with open(file_name, "w+") as f:
        data = input("Enter your msg: ")
        f.write(data)
        read_data = f.read()
        print(read_data)
else:
    print("From else block:")
    with open(file_name,"a+") as f:
        read_data = f.read()
        print(read_data)
        data = input("Enter your msg: ")
        f.write(data)
        read_data = f.read()
        print(read_data)