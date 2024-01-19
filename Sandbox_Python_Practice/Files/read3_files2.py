# Create a program similar to above that counts the number of words in the files as well.
# After printing out information about each file, this program should also print the total
# number of lines & words in all 3 files. You can use the string split function to split a line
# of input into a list of words by splitting the line on spaces.
# Jonathan Lee


# List of filenames to read
filenames = [r'Sandbox_Python_Practice\Files\text1.txt', r'Sandbox_Python_Practice\Files\text2.txt', r'Sandbox_Python_Practice\Files\text3.txt']
total_lines = 0
total_words = 0

# Write the line and word counts to counts.txt
with open('counts.txt', 'w') as output_file:
    for filename in filenames:
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()  # Read all lines into a list
                num_lines = len(lines)
                words = [word for line in lines for word in line.split()]  # Split lines into words
                num_words = len(words)
                
                # Write individual file's statistics
                output_file.write(f"{filename}: {num_lines} lines, {num_words} words\n")
                
                # Add to total counts
                total_lines += num_lines
                total_words += num_words

        except FileNotFoundError:
            print(f"File {filename} not found.")
            output_file.write(f"{filename}: File not found\n")

    # Write the total counts at the end of the file
    output_file.write(f"\nTotal: {total_lines} lines, {total_words} words")

print("Line and word counts have been written to counts.txt")
