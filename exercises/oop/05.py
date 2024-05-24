class shoppingCart:

    def __init__ (self):
        self.cart = []

    def add_item(self,item_name, qty, price):
        item = (item_name,qty,price)
        self.cart.append(item)
        
    def remove_item(self,item_name):
        for item in self.cart:
            if item[0] == item_name:
                self.cart.remove(item)
                break

    def calc_total_price(self):
        total = 0
        for item in self.cart:
            total = total + (item[1]*item[2])
        return total
    
my_cart = shoppingCart()

keepAsking = True

while keepAsking:
    choice = int(input("Add Item : 1\nRemove Item: 2\nCalculate Price: 3\nExit: 0\nEnter you choice:"))

    if(choice == 1):
        item_name = input("Enter item name:")
        qty = int(input("Enter quantity: "))
        price = float(input("Enter price:"))

        my_cart.add_item(item_name,qty,price)

        print(my_cart.cart)

    elif(choice == 2):
        item_name = input("Enter item name:")

        my_cart.remove_item(item_name)
    elif(choice == 3):
        print(f"Total Price: {my_cart.calc_total_price()}")
    else:
        print(my_cart.cart)
        keepAsking = False