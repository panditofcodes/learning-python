student_data = {}
def addEntry():
    key = input("Enter name:")
    if key in student_data.keys():
        print("Key is already present: {}".format(student_data[key]))
        key = input("Enter key anyother value:")
    value = input("Enter marks: ")
    result = student_data.setdefault(key,value)
    
    
    allEntryAdded = True

    while allEntryAdded == True:
        allEntryAdded = int(input("Do you want to add more: 1 for Yes and 0 for no:"))
        if allEntryAdded == True:
            addEntry()
        else:
            iniate_program()
    return(result)

def see_student_data():
    name = input("Enter name:")
    if name in student_data:
        print(f"marks of {name} is {student_data[name]}")
    else:
        choice = int(input("No data found! Either wrong name or not availabele! To add data enter 1 and search again enter 0:"))
        if choice == 1:
            addEntry()
        else:
            see_student_data()

def iniate_program():
    opt = input("Enter 1 if you want to add data and 2 to see data and press enter to exit: ")
    if opt == "":
        exit()
    elif int(opt) == 1:
        see_student_data()
    else:
        addEntry()
iniate_program()