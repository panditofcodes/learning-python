def sum_thrice(n1,n2,n3):
    result = n1+n2+n3
    if (n1==n2==n3):
        result = n1 * n2 * n3
    return result

print(sum_thrice(1,2,3))