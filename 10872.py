n = int(input())

def pac(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x * pac(x-1)
    
print(pac(n))




