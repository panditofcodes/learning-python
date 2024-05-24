try:
    f = open("abc.txt","r")
    f.read()
except FileNotFoundError:
    print("File not available!")