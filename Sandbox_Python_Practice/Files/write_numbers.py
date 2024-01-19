# writes numbers from a user to a file
# jonathan lee

PROMPT = "Enter a number ( Enter 0 to quit): "

outfilename = input("What is the name of your output file?")

#create a new file object, in "write" mode
dataFile = open(outfilename, "w") # a to append

with open(outfilename, "w") as dataFile:
    while True:
        userinput = input(PROMPT)
        
        if userinput == "0":
            break
        # write the user's input to the file
        print(userinput, file=dataFile)
