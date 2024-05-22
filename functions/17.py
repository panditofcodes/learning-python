students = {
    1:"a",
    2:"b",
    3:"c",
    4:"d",
    5:"e",
}
def checkStudent (func):
    def wrapper(rollNo,name):
        if rollNo in students:
            return print(f"user already exist: {students[rollNo]}")
        else:
            return func(rollNo, name)
    return wrapper


@checkStudent
def addStudent(rollNo,name):
    students[rollNo] = name
    print(students)


addStudent(3,"F")