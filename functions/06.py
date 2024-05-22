def fact(num):
    factorial = 1
    while num >=1:
        factorial = factorial*num
        num = num-1
    return factorial
for i in range(1,6):
    print(f"Factorial of {i} is {fact(i)}")