num_set = {1,2,2,2,2,2,3,3,3,344,5,6777,8,}
unique_Set = []
print(num_set)
for num in num_set:
    if num not in unique_Set:
        unique_Set.append(num)
print(unique_Set)