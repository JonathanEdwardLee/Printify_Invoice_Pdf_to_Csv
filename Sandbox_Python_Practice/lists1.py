# Writing programs with lists and strings
# Jonathan Lee

# Write a program that creates a list of 20 numbers input by the user and prints
# the average (mean) of the list.

#list = []
#for i in range (20):
    #num = float(input("Please enter a number: "))
    #list.append (num)

#print ("You entered: ", list)
#print ("Your average is ", sum(list)/len(list))

#2. Write a function mangle that takes a string as a parameter and returns the
# string after performing the following operations:
# i. Converting the string to all upper case letters
# ii. Removing the third character
# iii. Removing the third to last character

def mangle(str):
    str = str.upper()
    str = str[0:2] + str[3:-3] + str[-2:]
    return str

def main():
    print (mangle("hellothere"))
    test_input = ["hellothere","42 degrees Celsius","eeeeeee"]
    test_output = ["HELOTHRE","42DEGREES CELSUS","EEEEE"]
    for i in range (len(test_input)):
        print ("Mangle ", test_input[i] + ":", mangle(test_input[i])== test_output[i])

main()



