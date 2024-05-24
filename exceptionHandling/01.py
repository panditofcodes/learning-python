n = int(input("Enter a number:"))

try:
    print(n/0)
except ZeroDivisionError:
    print("Zero divison error!")
