import datetime

class person:
    def __init__ (self,name,country,dob):
        self.name = name
        self.country = country
        self.dob = dob

    def age_calculator(self):
        today = datetime.date.today()
        age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return age

name = input("Enter name: ")
country = input("Enter country: ")
dob_year = int(input("Enter year: "))
dob_month = int(input("Enter month: "))
dob_day = int(input("Enter day: "))

dob = datetime.date(dob_year, dob_month, dob_day)

person1 = person(name, country, dob)

print(person1.age_calculater())
