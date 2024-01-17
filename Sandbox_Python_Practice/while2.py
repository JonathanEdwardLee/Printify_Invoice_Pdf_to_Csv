# Strings, Lists, and Whiles
# Jonathan Lee

# Write a function average_neg_evens that takes a list of numbers as a
# parameter, and adds all the negative even numbers (less than 0 and
# divisible by 2) together and returns their average.
# Example function call:
# print(average_neg_evens([0, 1, 2, -2, -3, -4, 3, 4]))


def average_neg_evens(list):
    sum = 0
    count = 0 
    # for num in list:
    i = 0 #initializing the loop index variable
    while i < len(list): # loop condition
        num = list[i]  # how we go from index -> value in list
        if num < 0 and num % 2 == 0:
            sum += num
            count += 1
        i += 1 # loop variable increment
    return sum / count

print(average_neg_evens([0, 1, 2, -2, -3, -4, 3, 4])) 

# Write a function count_letter that takes a list of strings and a string
# letter as parameters and returns the number of times this letter
# occurs, both upper- & lower-cased.
# Example function call:

def count_letter(list, letter):
    count = 0
    letter = letter.lower()
    
    i = 0
    # for string in list:
    while i < len(list):
        string = list[i]
        count += string.lower().count(letter)
        i += 1

    return count


list = ["HELLO", "goodbye", "1234 Oooh!"]
print(count_letter(list, "o"))

