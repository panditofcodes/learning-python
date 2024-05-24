try:
    f = open("abc.txt","w")
    f.read()
except PermissionError:
    print("Permission Error!")