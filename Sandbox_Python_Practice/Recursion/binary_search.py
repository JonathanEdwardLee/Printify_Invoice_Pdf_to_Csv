# jonathan lee

a = [-4,5,7,10,23,46,75,89,92,103]

# iterative binary search

def binary_search(a, num):
    mid = -1
    min = 0 
    max = len(a) - 1

    while mid == -1 or (a[mid] != num and a[max] >= num):
        mid = round((max + min) / 2)
        if a[mid] == num:
            return mid
        elif a[mid] > num:
            max = mid -1
        elif a[mid] < num:
            min = mid + 1
    return -1

print(binary_search(a,35))
print(binary_search(a,7))

# recursive binary search

def search(a, num, min, max):
    mid = min + (max - min) // 2
    if min > max:
        return -1
    elif num < a[mid]:
        return search(a,num,min,mid-1)
    elif num > a[mid]:
        return search(a,num,mid+1,max)
    else:
        return mid
def bin_search(a,num):
    return search(a,num,0,len(a)-1)

print(bin_search(a,35))
print(bin_search(a,7))