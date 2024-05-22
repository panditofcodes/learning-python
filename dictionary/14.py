d={}

print(d)



# result = d.setdefault(key,value)


def addEntry():
    key = input("Enter key value:")
    if key in d.keys():
        print("Key is already present: {}".format(d[key]))
        key = input("Enter key anyother value:")
    value = input("Enter value: ")
    result = d.setdefault(key,value)
    return(result)

allEntryAdded = True

while allEntryAdded == True:
    addEntry()
    for k,v in d.items():
        print(k,"--",v)
    allEntryAdded = int(input("Do you want to add more: 1 for Yes and 0 for no:"))