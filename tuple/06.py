print("Important function of tuple".rjust(75))

tup = 1,2,2,2,4,5,6,7,7,7
print(tup)

print("Length:",len(tup))

print("Count:",tup.count(2))

print("Index: ",tup.index(6))

ran_tup = (7,3,4,2,5,6,1)
print(ran_tup)
print("Sorted tuple:",sorted(ran_tup))

print("Min:",min(tup))
print("Max:",max(tup))

print("Comparison".rjust(75))
print(tup,ran_tup , tup == ran_tup)