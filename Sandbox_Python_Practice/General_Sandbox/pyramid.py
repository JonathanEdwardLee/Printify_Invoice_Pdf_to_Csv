# practice writing functions
# Jonathan Lee

# 1. Write a function, pyramid, that takes a single character and a number as parameters and
# displays an ASCII art pyramid to the screen with number rows

def pyramid (icon,height):
    for i in range (1,height + 1):
        print (icon * i)

# 2. Write a function, absolute_difference, that takes two numbers as parameters and
# returns their absolute difference
        
def absolute_difference(num1, num2):
    print (abs(num1 - num2))


def main():
    pyramid("*",2)
    pyramid("+", 5)
    pyramid("x", 10)
    absolute_difference(5, 10)
    absolute_difference(10, 5)
    absolute_difference(200, -200) 

main()