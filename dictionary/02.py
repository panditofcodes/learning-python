record = {}
num_of_students = int(input("Enter total num of students: "))
i=1
while i <=num_of_students: 
    name = input("Enter name of students: ")
    marks = float(input("Enter marks of students: "))
    record[name] = marks
    i=i+1
print("Name of Student","\t","% of marks")
for x in record:
    print("\t",x,"\t\t",record[x])