# jonathan lee

# reverse a string recursively

def reverse(s):
    if len(s) == 0:
        return ''
    else:
        return s[-1] + reverse(s[:-1])
    
print(reverse("Happy Friday!"))
    