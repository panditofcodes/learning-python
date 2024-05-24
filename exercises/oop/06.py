class stack:

    def __init__(self):
        self.items = []
    
    def push_item(self, item ):
        self.items.append(item)
    
    def pop_item(self):

        if(len(self.items) > 0):
           return self.items.pop()
        else:
            print("Stack is empty!")
    
    def display_item(self):
        print(self.items)

my_stack = stack()

print(my_stack.display_item())
my_stack.push_item(1)
print(my_stack.display_item())
my_stack.push_item(2)
print(my_stack.display_item())
my_stack.push_item(3)
print(my_stack.display_item())
my_stack.push_item(4)
print(my_stack.display_item())
my_stack.push_item(5)

my_stack.pop_item()
print(my_stack.display_item())
my_stack.pop_item()
print(my_stack.display_item())
my_stack.pop_item()
print(my_stack.display_item())