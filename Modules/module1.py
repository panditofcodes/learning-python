def f1():

    if __name__=='__main__':

        print("The code executed as a program")

    else:

        print("The code executed as a module from some other program")
f1()

def func_extracter(module_name):
    x = dir(module_name)

    funcs = {}
    i = 0
    for f in x : 
        funcs[i] = f
        i+=1


    for k, v in funcs.items():
        print(v,"--",k)

    opt = int(input("Enter your choice:"))

    return opt