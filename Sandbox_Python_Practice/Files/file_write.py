# writes content from a user to a file
# jonathan lee

PROMPT = "Enter the next line in the file: "

outfilename = input("What is the name of your output file?")
numLines = eval(input("How many lines do you want to write?"))

#create a new file object, in "write" mode
dataFile = open(outfilename, "w") # a to append

for x in range(numLines):
    userinput = input(PROMPT)
    # write the user's input to the file
    print(userinput, file=dataFile)

# close the file with the method "close"
dataFile.close()