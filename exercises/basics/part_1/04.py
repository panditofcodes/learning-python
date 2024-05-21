filename = input("Enter a filename seperated by dot(.): ")
extOfFile = filename.rsplit(".")
print("Extension of file is: ",extOfFile[-1])