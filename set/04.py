num_set = {0,1,2,3,4}
print(num_set)

new_num_set = {5,7,8,9,10}
print(new_num_set)

num_set.update(new_num_set,range(5))

print(num_set)
