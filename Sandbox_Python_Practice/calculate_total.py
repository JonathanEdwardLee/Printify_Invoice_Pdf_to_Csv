# Write a function calculate_total that takes 3 parameters:
# a. meal: the cost of the meal
# b. tax_rate: the percent tax (e.g., NJ tax would be 0.07)
# c. tip_rate: the percent tip (e.g., a 20% tip rate is 0.20)
# Proper tipping technique dictates that the tip should be calculated
# based on the total cost of the meal, before tax is applied. Then,
# return the total. Test your function works by using the following call:
# calculate_total(53.48, .07, .18).
# Note that the total for the above meal with tax & tip is $66.85.
# Jonathan Lee

def calculate_total(meal, tax, tip):
    total = tip * meal + meal * tax + meal
    return total

    # Write a function hey that takes a number as a parameter, squares it, and
    # outputs the parameter squared:

def hey (num):
    squared = num * num # return num ** 2
    return squared

# Write a function there that takes a number n as a parameter, and returns 2n if
# n is positive, and 0 otherwise. Your function should output the following for the
# given calls:

def there (n):
    if n >= 0:
        return 2 ** n
    else: #else optional
        return 0
    
# Write a function are_we that takes a number of times to repeat and a phrase to
# be repeated as parameters and outputs the following for the given calls:
    
def are_we (num,call):
    for i in range(num):
        print ("Are we", call, "yet?", end=" ")
    print()


def main():
    print (calculate_total(53.48,.07, .18))
    print (hey(5))
    print (hey(0))
    print (hey(-3))
    print ("nth power")
    print (there(5)) #32
    print (there(0)) #1
    print (there(3)) #8
    print (there(-2)) #0
    print (there(-6))
    are_we (2, "there")
    are_we(3, "50") 

main()