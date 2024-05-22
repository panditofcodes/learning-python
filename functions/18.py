students = {
    1:"a",
    2:"b",
    3:"c",
    4:"d",
    5:"e",
}
adult_student = {
    2:"b",
    3:"c",
}
def isadult(func):
    def wrapper(rollNo,name):
        if rollNo in adult_student:
            print("student is adult.")
            return func(rollNo,name)
        else:
            print("Student minor")
            return func(rollNo,name)
    return wrapper

def checkStudent(func):
    def wrapper(rollNo,name):
        if rollNo in students:
            print(f"student exist!")
        else:
            return func(rollNo,name)
    return wrapper


@checkStudent
@isadult
def addStudent(rollNo,name):
    students[rollNo] = name
    print(students)

addStudent(6,"q")