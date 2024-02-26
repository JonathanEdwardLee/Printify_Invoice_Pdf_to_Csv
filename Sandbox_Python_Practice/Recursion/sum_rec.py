#jonathan lee

def sum_iter(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i
    return total_sum

print(sum_iter(5))

def sum_rec(n):
    if n == 1:   #base case
        return 1
    else:
        return n + sum_rec(n - 1)
    
print(sum_rec(5))