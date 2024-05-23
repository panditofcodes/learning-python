# Generator
import random
employes = {}
def key_generator():
        def generate_key():
            yield int((random.randint(1000,9999)))
        key_gen = generate_key()
        key = next(key_gen)
        return key

def addEmployee():
      addMore = True
      while addMore :
            key = key_generator()
            name = input("Enter name:")
            employes[key]=name
            print("Emp-Id","---","Name")
            for k,v in employes.items():
                  print(k,"---",v)
            addMore = int(input("To add employee enter 1 to exit enter 0:"))
            

addEmployee()