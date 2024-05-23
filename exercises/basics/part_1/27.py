n1 = int(input("Enter 1st number:"))
n2 = int(input("Enter 2nd number:"))
n1_list={1}
n2_list={1}
i = 2
j = 0
while i<=(n1/2):
    if ((n1%i)==0):
        n1_list.add(i)
    i+=1
    j+=1
print(n1_list)
i = 2
while i<=(n2/2):
    if ((n2%i)==0):
        n2_list.add(i)
    i+=1
    j+=1
print(n2_list)
common_factors = n1_list.intersection(n2_list)