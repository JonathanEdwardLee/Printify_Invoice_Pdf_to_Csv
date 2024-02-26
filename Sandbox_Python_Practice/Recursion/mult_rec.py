# jonathan lee

# multiply two numbers with only addition and subtraction.

def mult_iter(a,b):
    total = 0
    for i in range(b):
        total += a
    return total

print(mult_iter(2,3)) 

def mult_rec(a,b):
    if b == 0:
        return 0
    else:
        return a + mult_rec(a, b-1)
    
print(mult_rec(2,3))