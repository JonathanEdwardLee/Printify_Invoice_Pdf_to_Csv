# Write a python program that reads 3 files called test1.txt, text2.txt, and text3.txt, counts
# the number of lines in each file, and prints out the number of lines to a file counts.txt
# Jonathan Lee

# List of filenames to read
filenames = [r'Sandbox_Python_Practice\Files\text1.txt', r'Sandbox_Python_Practice\Files\text2.txt', r'Sandbox_Python_Practice\Files\text3.txt']
line_counts = {}

# Count the number of lines in each file
for filename in filenames:
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            line_counts[filename] = len(lines)
    except FileNotFoundError:
        print(f"File {filename} not found.")
        line_counts[filename] = 'File not found'

# Write the line counts to counts.txt
with open('counts.txt', 'w') as output_file:
    for filename, count in line_counts.items():
        output_file.write(f"{filename}: {count} lines\n")

print("Line counts have been written to counts.txt")
