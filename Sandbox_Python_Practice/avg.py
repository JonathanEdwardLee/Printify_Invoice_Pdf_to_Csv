# create a program that averages 10 numbers submitted by user
# Jonathan Lee

s = 0 #aggregator variable, zero for adding, 1 if multiplying
for i in range(10):
    num = int(input("Please enter a real number: "))
    s += num
print ("Your average is: ", s / 10)

print()

s = 0
for y in range(5):
    while True:
        try:
            number = float(input("Please enter a real number: "))
            s += number
            break
        except ValueError:
            print("That's not a valid number. Please try again.")

average = s / 5
print("Your average is:", average)

print()

# Initialize a variable to store the sum
total = 0

# Loop to get five numbers from the user
for i in range(5):
    while True:
        try:
            number = float(input(f"Enter number {i + 1}: "))
            total += number
            break
        except ValueError:
            print("Please enter a valid number.")

# Calculate the average
average = total / 5

# Print the average
print("The average of the numbers is:", average)

