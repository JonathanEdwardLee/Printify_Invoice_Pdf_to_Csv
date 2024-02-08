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

# Write a function, count_e, that takes a list of strings as a parameter and
# returns the total number of upper and lower case e’s (“E” and “e”) in all the
# strings in the list. Test that your function works with multiple examples.
def count_e(list):
    num_e = 0
    for string in list:
        num_e += string.upper().count("E")
    return num_e

# Write a function, count_vowels, that takes a list of strings as a parameter
# and returns the total number of upper and lower case vowels (A, E, I, O, U) in all
# the strings in the list.
def count_vowels(list):
    num_v = 0
    for string in list:
        upper = string.upper()
        for vowel in "AEIOU":
            num_v += upper.count(vowel)
    return num_v

def main():
    print (mangle("hellothere"))
    test_input = ["hellothere","42 degrees Celsius","eeeeeee"]
    test_output = ["HELOTHRE","42DEGREES CELSUS","EEEEE"]
    for i in range (len(test_input)):
        print ("Mangle ", test_input[i] + ":", mangle(test_input[i])== test_output[i])
    print(count_e(["hi", "hello", "EEK!"]))
    print("count_e", count_e(["hi", "hello", "EEK!"]) ==3)
    print(count_vowels(["hi", "hello", "OOF!"]))
    print("count_vowels", count_vowels(["hi", "hello", "OOF!"])==5)               
main()



