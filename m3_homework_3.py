# ====================================
# Attached: m3 Homework #3
# ====================================
# File: Project #1
# ====================================
# Name: Distance Traveled
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# asking the user for the speed of a vehicle
speed = float(input('Enter the speed of the vehicle is mph: '))
# asking the user for the number of hours it has traveled.
hours = int(input('Enter the number of hours traveled: '))

# assigning a variable
i = 1

# formatting the output
print("\nHours  Distance Traveled")
print("------------------------------")

# using a loop to display the distance the vehicle has traveled for each hour of that time period
while i < hours + 1:
    print(i, "         ", speed * i)
    i = i + 1

''''
=================== Output ===========================
Enter the speed of the vehicle is mph: 40
Enter the number of hours traveled: 3

Hours  Distance Traveled
------------------------------
1           40.0
2           80.0
3           120.0

Process finished with exit code 0

'''

# ==============================================================

# ====================================
# Attached: m3 Homework #3
# ====================================
# File: Project #2
# ====================================
# Name: Average rainfall
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# asking the user to enter the number of years
years = int(input('Enter the number of years: '))

# assigning the variables
month = 0
rainfall = 0

# the outer loop will iterate one for each year
for year in range(years):
    print("For year", year + 1, ':'.format((year + 1)))

    # the inner loop will iterate 12 times, once for each month.
    # It will also ask the user for the inches of rainfall for that month
    for months in range(12):
        rainfall_amount = int(input("Enter the rainfall amount for the month: "))

        # adding two values and assigning it to a variable
        month += 1

        # adding two values and assigning it to a variable
        rainfall += rainfall_amount

        # calculating the average
        average = rainfall/month

# display the number of months
print("Number of months:", month)

# display the total inches of rainfall
print("Total rainfall: ", rainfall, "inches")

# display the average rainfall per month for the entire period
print("Average monthly rainfall:  {0:.2f} inches".format(average))

''''
=================== Output ===========================
Enter the number of years: 2
For year 1 :
Enter the rainfall amount for the month: .3
Enter the rainfall amount for the month: .2
Enter the rainfall amount for the month: 0
Enter the rainfall amount for the month: .1
Enter the rainfall amount for the month: 1
Enter the rainfall amount for the month: .6
Enter the rainfall amount for the month: 0
Enter the rainfall amount for the month: .2
Enter the rainfall amount for the month: .1
Enter the rainfall amount for the month: .9
Enter the rainfall amount for the month: 0
Enter the rainfall amount for the month: .4
For year 2 :
Enter the rainfall amount for the month: .1
Enter the rainfall amount for the month: 0
Enter the rainfall amount for the month: 0
Enter the rainfall amount for the month: 0
Enter the rainfall amount for the month: .2
Enter the rainfall amount for the month: 1
Enter the rainfall amount for the month: 2
Enter the rainfall amount for the month: .9
Enter the rainfall amount for the month: .2
Enter the rainfall amount for the month: .1
Enter the rainfall amount for the month: .2
Enter the rainfall amount for the month: .3
Number of months: 24
Total inches of rainfall:  4 inches
Average monthly rainfall:  0.00 inches

Process finished with exit code 0

'''

# ====================================
# Attached: m3 Homework #3
# ====================================
# File: Project #3
# ====================================
# Name: Sum of Numbers
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# assigning a variable
total = 0

# informing the user the way to end the series
print("Note: Enter a negative number to signal the end of the series.")

# asking the user to enter a positive number
numbers = int(input("Enter a positive number: "))

# using a loop to enter a series of positive numbers
while numbers >= 0:
    # adding two values and assigning it to a variable
    total += numbers
    numbers = int(input("Enter a positive number: "))
# if the user enters a negative number, the following will display
else:
    print("You entered a negative number! this is the end of the series.")

# displaying the total sum
print("\nAfter all the positive numbers have been entered, the sum is", total)

''''
=================== Output ===========================
Note: Enter a negative number to signal the end of the series.
Enter a positive number: 1
Enter a positive number: 2
Enter a positive number: 3
Enter a positive number: 4
Enter a positive number: 5
Enter a positive number: -6
You entered a negative number! this is the end of the series.

After all the positive numbers have been entered, the sum is 15

Process finished with exit code 0

'''

