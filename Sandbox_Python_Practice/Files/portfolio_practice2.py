# Data Portfolio Practice
# jonathan lee

import statistics

def output_stats(list):
    print("Mean: ", statistics.mean(list))
    print("Median: ", statistics.median(list))
    print("Standard Deviation: ", statistics.stdev(list))
    print()
# data variables
spring = []
fall = []
#read in the file
csv = "Sandbox_Python_Practice\Files\sample_grades.csv"
file = open(csv)
for line in file:
    # print(line.rstrip()) <- 1. test open
    list = line.rstrip().split(",")
    # print(list) <- 2. test split and whitespace removal
    if list[1] == "Spring 2016":
        spring.append(eval(list[2]))
    else:
        fall.append(eval(list[2]))
file.close()
# print("Spring: ", spring) <- 3. test lists for appropriate data scraped
# print("Fall: ", fall)
print("Fall 2016:")
output_stats(fall)
print("Spring 2016: ")
output_stats(spring)

