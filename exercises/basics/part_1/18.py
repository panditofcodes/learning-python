str_num_list = input("Enter list of numbers separated by spaces: ")
num_list = [int(num) for num in str_num_list.split()]
count = 0
for i in num_list:
    if i == 4:
        count += 1

print("Number of occurrences of 4:", count)
