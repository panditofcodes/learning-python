str = "Learning Python is very easy !!!!"
n=len(str)
print("In forward: -")
i=0
while i<n:
    print(str[i],end=' ')
    i=i+1
print("In backward: -")
i=-1
while i>=-n:
    print(str[i],end=' ')
    i=i-1