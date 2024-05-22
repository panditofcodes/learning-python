d = {
    100:"Ravi",
    200:"Suraj",
    300:"Shiv",
}

print("Dictionary:",d)
key = int(input("Enter the key that you want to del:"))
del d[key]
print("After deletation: ",d)