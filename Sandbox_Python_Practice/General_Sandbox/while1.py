# practicing while loops
# Jonathan Lee

x = 1
while x < 6:
    print (x)
    x += 1

print ("test b")
x = 2
while x < 12:
    print (x)
    x += 3

print ("test c")
x = -10
while x < 1:
    print (x)
    x += 2

print ("test d")
x = 0
while x < 4:
    print("*" * 4)
    x += 1

print ("test e")

x = 0
string = "CSI 500"
while x < len(string):
    print(string[x])
    x += 1

print ("test f")

list = []
prompt = "Please enter a number ('0' to finish): "
response = float(input(prompt))
while response != 0:
    list.append(response)
    response = float(input(prompt))
print("Your numbers sorted: ", sorted(list))
print("The sum of your numbers: ", sum(list))
print("The average of your numbers: ", sum(list)/len(list))