# ====================================
# Attached: m4 Homework #4.7
# ====================================
# File: Project #1
# ====================================
# Name: Finding the Sum
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# assigning the variables
i = 0
total = 0

# the tuple created
test_tup = (15, 20, 123, 47, 26, 81)

# using a while loop to find the sum of the tuple
while i < len(test_tup):
    total = total + test_tup[i]
    i = i + 1

# displaying the sum
print("The sum of this tuple: " + str(total))

''''
=================== Output ===========================
The sum of this tuple: 312

Process finished with exit code 1

'''

# ====================================
# Attached: m4 Homework #4.7
# ====================================
# File: Project #2
# ====================================
# Name: Finding the Largest Number
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# creating the tuple
test_tup = (15, 20, 123, 47, 26, 81)

# assuming first value in tuple as maximum value
largest = test_tup[0]

for i in range(len(test_tup)):
    # to find the largest value
    if test_tup[i] > largest:
        # assign the largest value to the variable
        largest = test_tup[i]

# displaying the largest number in the tuple
print("The largest number in this tuple:", largest)

''''
=================== Output ===========================
The largest number in this tuple: 123

Process finished with exit code 0

'''

# ====================================
# Attached: m4 Homework #4.7
# ====================================
# File: Project #3
# ====================================
# Name: Finding the Sum
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# creating the tuple
test_tup = ([17, 28], [93, 11], [20, 17])

# converting the tuple to a list and
# finding the sum of the elements in the list using the sum function
total = [sum(t) for t in test_tup]

# displaying the sum of all the integers in the tuple
print("The sum of all integer numbers in this tuple:", total)

''''
=================== Output ===========================
The sum of all integer numbers in this tuple: [45, 104, 37]

Process finished with exit code 0

'''

# ====================================
# Attached: m4 Homework #4.7
# ====================================
# File: Project #4
# ====================================
# Name: Sorting
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# the tuple is created
input_tup = ([2, 20], [44, 1], [3, 13])

# using the sorted function to sort the tuple
sorted_tup = sorted(input_tup)

# displaying the sorted tuple
print("After sorting the tuple:", sorted_tup)

''''
=================== Output ===========================
After sorting the tuple: [[2, 20], [3, 13], [44, 1]]

Process finished with exit code 0

'''