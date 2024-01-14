# Write a function is_even that takes a number as a parameter and
#returns whether or not it is even. Test that your function works by
#calling it twice, once with an even number and once with an odd
#number, and print the results.
#Jonathan Lee

def is_even(num):
    return num % 2 == 0

def main():
    print ("Is 4 even?", is_even(4))
    print ("Is 5 even", is_even(5))

main()