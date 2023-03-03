# ====================================
# Attached: Class Exercise #3
# ====================================
# File: Challenge #1 (Part 1)
# ====================================
# Name: Temperature
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# assigning a variable
max_temp = 102.5

# getting the first substance's temperature
temp1 = float(input("Enter temperature: "))

# instruct the user to adjust the thermostat if it goes above 102.5
while temp1 > max_temp:
    print("The temperature is too high.")
    break

# getting the second substance's temperature
temp2 = float(input("Enter temperature: "))

# instruct the user to adjust the thermostat if it goes above 102.5
while temp2 > max_temp:
    print("The temperature is too high.")
    break

# getting the third substance's temperature
temp3 = float(input("Enter temperature: "))

# instruct the user to adjust the thermostat if it goes above 102.5
while temp3 > max_temp:
    print("The temperature is too high.")
    break

# getting the fourth substance's temperature
temp4 = float(input("Enter temperature: "))

# instruct the user to adjust the thermostat if it goes above 102.5
while temp4 > max_temp:
    print("The temperature is too high.")
    break

# getting the fifth substance's temperature
temp5 = float(input("Enter temperature: "))

# instruct the user to adjust the thermostat if it goes above 102.5
while temp5 > max_temp:
    print("The temperature is too high.")
    # getting the sum of the four temps
    total = temp1 + temp2 + temp3 + temp4
    # displaying the sum
    print("Sum:", str(total))

    # getting the average
    average = total / 4
    # displaying the average
    print("Average:", str(average))
    break

''''
=================== Output ===========================
Enter temperature: 60
Enter temperature: 70
Enter temperature: 80
Enter temperature: 90
Enter temperature: 120
The temperature is too high.
Sum: 300.0
Average: 75.0

Process finished with exit code 0

'''

# ====================================
# Attached: Class Exercise #3
# ====================================
# File: Challenge #2 (Part 1)
# ====================================
# Name: Sales
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# assigning the variable to control the loop
keep_going = "y"

# using an infinite while loop
while keep_going == "y":
    # asking the user for a salesperson's sales and commission rate.
    sales = float(input("Enter the amount of sales: "))
    comm_rate = float(input("Enter the commission rate: "))

    # asking the user if they would like to enter a new salesperson's sales and commission rate
    keep_going = input("Do you want to calculate another commission (enter y for yes and n for no): ")

    # using an if statement if the user decides to stop the loop
    if keep_going == "n":
        # calculating the commission
        commission = sales * comm_rate
        # displaying the results
        print("The commission is $%.2f." % commission)
        # stopping the loop from going on infinitely.
        break

''''
=================== Output ===========================
Enter the amount of sales: 199
Enter the commission rate: .6
Do you want to calculate another commission (enter y for yes and n for no): y
Enter the amount of sales: 299
Enter the commission rate: .7
Do you want to calculate another commission (enter y for yes and n for no): y
Enter the amount of sales: 399
Enter the commission rate: .8
Do you want to calculate another commission (enter y for yes and n for no): y
Enter the amount of sales: 499
Enter the commission rate: .9
Do you want to calculate another commission (enter y for yes and n for no): n
The commission is $449.10.

Process finished with exit code 0

'''

# ====================================
# Attached: Class Exercise #3
# ====================================
# File: Challenge #3 (Part 1)
# ====================================
# Name: Even or Odd
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# letting the user know what's going on
print("I will display the numbers 1 through 10. \n")

# the numbers are place in an array
# print odd and even number to a maximum of 10
for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    # calculating the even number
    if (num % 2) == 0:
        # display the number with it stating it even
        print(num, "Even \n")
    else:
        # display the number with it stating it is odd
        print(num, "Odd \n")

''''
=================== Output ===========================
I will display the numbers 1 through 10. 

1 Odd 

2 Even 

3 Odd 

4 Even 

5 Odd 

6 Even 

7 Odd 

8 Even 

9 Odd 

10 Even 

Process finished with exit code 0

'''

# ====================================
# Attached: Class Exercise #3
# ====================================
# File: Challenge #4 (Part 1)
# ====================================
# Name: Name
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# this program will demonstrate a simple loop that uses a list of strings.

# The first for loop will loop through your last name
for last_name in ["Ceballos Gomez"]:
    # the second for loop will through your first name.
    for first_name in ["Jacqueline"]:
        # display both loops
        print("Your full name is " + last_name, "" + first_name)

''''
=================== Output ===========================
Your full name is Ceballos Gomez Jacqueline

Process finished with exit code 0

'''

# ====================================
# Attached: Class Exercise #3
# ====================================
# File: Challenge #5 (Part 1)
# ====================================
# Name: Hello World
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# this program will demonstrate how the range function can be used with a for loop.

# display a message 10 times
for x in range(10):
    print("Hello world!")

''''
=================== Output ===========================
Hello world!
Hello world!
Hello world!
Hello world!
Hello world!
Hello world!
Hello world!
Hello world!
Hello world!
Hello world!

Process finished with exit code 0

'''
