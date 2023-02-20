# ====================================
# Attached: m1 Homework #2
# ====================================
# File: Project #1
# ====================================
# Name: Quarter of the Year
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# asking the user to enter a month
month = int(input("Enter a month between 1 and 12: "))

# if the user enters a number between 1 and 3, the month is in the first quarter.
if 1 <= month <= 3:
    print("The month is in the first quarter. ")

# if the user enter a number between 4 and 6, the month is in the second quarter.
elif 4 <= month <= 6:
    print("The month is in the second quarter. ")

# if the user enters a number between 7 and 9, the month is in the third quarter.
elif 7 <= month <= 9:
    print("The month is in the third quarter. ")

# if the user enters a number between 10 and 12, the month is in the fourth quarter.
elif 10 <= month <= 12:
    print("The month is in the fourth quarter. ")

# if the user enters a number not between 1 and 12, the program will display an error
else:
    # error message
    print("Error!!! The number is not between 1 and 12.")

''''
=================== Output ===========================
Enter a month between 1 and 12: 11
The month is in the fourth quarter. 

Process finished with exit code 0

'''

# ==============================================================

# ====================================
# Attached: m1 Homework #2
# ====================================
# File: Project #2
# ====================================
# Name: Hot Dog Cookout Calculator
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# declaring variables
hotdogPackage = 10
buns = 8

# asking the user to enter the # of people attending
people = int(input("Enter # of people who are attending: "))

# asking the user to enter how many hot dogs each person will get
hotdog = int(input("Enter # of hot dogs each person will be given: "))

# calculating the total
total = people * hotdog

# calculating the minimum # of hot dog packages needed
needed = total // hotdogPackage

# calculating the minimum # of buns needed
needed = total // buns

# calculating the # of hots that are going to be leftover
leftOver = total % hotdogPackage

# calculating the # of buns that are going to be leftover
leftOver = total % buns

# displaying the minimum of hot dogs and buns
print("\nMinimum # of packages of hot dogs required are " + str(needed))
print("Minimum # of packages of hot dog buns required are " + str(needed))

# displaying the leftovers
print("\nNumber of hot dogs that will be left over = " + str(leftOver))
print("Number of hot dogs buns that will be left over = " + str(needed))

''''
=================== Output ===========================
Enter # of people who are attending: 12
Enter # of hot dogs each person will be given: 1

Minimum # of packages of hot dogs required are 1
Minimum # of packages of hot dog buns required are 1

Number of hot dogs that will be left over = 4
Number of hot dogs buns that will be left over = 4

Process finished with exit code 0

'''

# ==============================================================

# ====================================
# Attached: m1 Homework #2
# ====================================
# File: Project #3
# ====================================
# Name: Software Sales
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# declaring the variable
price = 99.00

# asking the user to enter the # of packages purchased
packages = float(input("Enter # of packages purchased: "))

# assigning the quantity of the packages to the discount using if-elif statements
# if the packages are less than 10, there is no discount
if packages < 10:
    discount = 0
# if there are 10-19 packages, there is a 10% discount
elif 10 <= packages <= 19:
    discount = .10
# if there are 20-49 packages, there is a 20% discount
elif 20 <= packages <= 49:
    discount = .20
# if there are 50-99 packages, there is a 30% discount
elif 50 <= packages <= 99:
    discount = .30
# if there are 100 or more packages, there is a 40% discount
elif packages >= 100:
    discount = .40

# calculating the subtotal
subTotal = packages * price

# calculating the discount
discount_amount = subTotal * discount

# calculating the overall total
total = subTotal - discount_amount

# display the subtotal
print("Subtotal: $%.2f" % subTotal)

# display the discount amount
print("Discount amount: $%.2f" % discount_amount)

# display the overall total
print("Total: $%.2f" % total)

''''
=================== Output ===========================
Enter # of packages purchased: 15
Subtotal: $1485.00
Discount amount: $148.50
Total: $1336.50

Process finished with exit code 0

'''
