def outer_function():
    x = 10
    
    def inner_function():
        nonlocal x
        x = 20
        print("Inner function:", x)
    
    inner_function()
    print("Outer function:", x)

outer_function()
