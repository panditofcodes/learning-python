X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]

target = 70


for i in X:
    for j in Y:
        for k in Z:
            if (i+j+k) == target:
                print(i,j,k)
                exit()
            
