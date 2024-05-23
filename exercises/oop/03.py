class calculator:

    def __init__ (self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    
    def sum (self):
        return self.num1 + self.num2
    
    def sub (self):
        return self.num1 - self.num2
    
    def multi (self):
        return self.num1 * self.num2
    
    def div (self):
        return self.num1 / self.num2

num1 = int(input("Enter a num:"))
num2 = int(input("Enter a num:"))

my_cal = calculator(num1, num2)

print(my_cal.sum())
print(my_cal.sub())
print(my_cal.multi())
print(my_cal.div())
