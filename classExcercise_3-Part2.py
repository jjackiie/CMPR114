# ====================================
# Attached: Class Exercise #3
# ====================================
# File: Challenge #1 (Part 2)
# ====================================
# Name: Calculations
# ====================================
# Description: this program calculates
# the sum of a series of numbers entered
# by the user.
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# assigning the maximum number
MAX = 5

# assigning the variable
total = 0.0

# explaining what we are doing
print("This program calculates the sum of", MAX, "numbers you will enter. \n")

# getting the numbers, accumulating them and getting the average
for counter in range(MAX):
    number = int(input("Enter a number: "))
    total = total + number
    avg = total / MAX

# displaying the results
print("\nThe total is", total)
print("The average is", avg)

''''
=================== Output ===========================
This program calculates the sum of 5 numbers you will enter. 

Enter a number: 11
Enter a number: 22
Enter a number: 33
Enter a number: 44
Enter a number: 55

The total is 165.0
The average is 33.0

Process finished with exit code 0

'''

# ====================================
# Attached: Class Exercise #3
# ====================================
# File: Challenge #2 (Part 2)
# ====================================
# Name: Product
# ====================================
# Description: this program calculates
# the number the user enters and the result
# will be assigned to a variable.
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# assigning the variable
product = 0

while product < 100:
    # asking the user to enter a #
    number = int(input("Enter a number: "))
    # multiplying the number by 10 and the result assigned to a variable named product
    product = number * 10
    # displaying the results
    print("Result:", product)

''''
=================== Output ===========================
Enter a number: 55
Result: 550

Process finished with exit code 0

'''

# ====================================
# Attached: Class Exercise #3
# ====================================
# File: Challenge #3 (Part 2)
# ====================================
# Name: Bug Collector
# ====================================
# Description: this program calculates
# the total number of bugs collected
# during a five day period.
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# assigning the variables
days = 0
total = 0

while days < 5:
    # asking the user to enter the # of bugs collected
    bugs = int(input("Enter the number of bugs collected: "))
    # calculating the total and days
    total += bugs
    # adding two values and assigning it to a variable
    days += 1

# display the results
print("\nTotal number of bugs collected:", total)

''''
=================== Output ===========================
Enter the number of bugs collected: 1
Enter the number of bugs collected: 2
Enter the number of bugs collected: 3
Enter the number of bugs collected: 4
Enter the number of bugs collected: 5

Total number of bugs collected: 15

Process finished with exit code 0

'''

# ====================================
# Attached: Class Exercise #3
# ====================================
# File: Challenge #4 (Part 2)
# ====================================
# Name: Calories Burned
# ====================================
# Description: this program will display
# the number of calories burned after
# 10, 15, 20, 25, 30 minutes.
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# assigning the variable
minutes = 10

while minutes <= 30:
    # calculating the total
    total = minutes * 4.2
    # displaying the total
    print("The number of calories burned after", minutes, "is", total)
    # adding two values and assigning it to a variable
    minutes += 5

''''
=================== Output ===========================
The number of calories burned after 10 is 42.0
The number of calories burned after 15 is 63.0
The number of calories burned after 20 is 84.0
The number of calories burned after 25 is 105.0
The number of calories burned after 30 is 126.0

Process finished with exit code 0

'''

# ====================================
# Attached: Class Exercise #3
# ====================================
# File: Challenge #5 (Part 2)
# ====================================
# Name: Lap Times
# ====================================
# Description: this program will display
# the users time of their fastest lap,
# slowest lap and average lap time.
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

laps = int(input("Enter the # of times you have run around the racetrack: "))



''''
=================== Output ===========================


'''