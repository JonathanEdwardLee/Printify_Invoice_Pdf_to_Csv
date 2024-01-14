# write a function
# by Jonathan Lee

def header (text,border):
    length = len(text) + 4
    # text = "Hello, World!"
    # border = "*"
    print(border * length)
    print(border,text,border)
    print(border * length)

header("Hello, World!", "*")
header("Leadership Class", "$")
header("Jonathan Edward Lee", "+")