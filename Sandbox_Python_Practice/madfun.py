# decimal practice
# Jonathan Lee

import math

usernum = float(input("Please enter a decimal number: "))

print ("The absolute of your number is", abs(usernum))
print ("Your number rounded to 0 is", round(usernum, 0))
print ("The square root of the absolute value of your rounded number is", math.sqrt(abs(round(usernum, 0))))