# Jonathan Lee

#file_path = r'Files\turing.txt'  #two ways to avoid single / problem
file_path = 'Files\\turing.txt'
lines_array = []

with open(file_path, 'r') as file:  #with auto closes or file.close() / file = open()
    for line in file:
        # Append each line to the list, stripping the newline character at the end
        lines_array.append(line.strip())

#print(lines_array)
print(lines_array[0]) 
print(lines_array[1]) 
print(lines_array[-1]) 
print(lines_array[-2]) 
print(len(lines_array))     