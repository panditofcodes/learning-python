def calc(a,b):
    sum = a + b
    sub = a - b
    multi = a * b
    dev = a/b
    return sum,sub,multi,dev
results = calc(10,2)
for result in results:
    print(result)