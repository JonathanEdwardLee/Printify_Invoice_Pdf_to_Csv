# jonathan Lee

dataFile = open(r"Sandbox_Python_Practice\Files\hello.txt")
for line in dataFile:
    print("-" + line.rstrip())
dataFile.close()