# ====================================
# Attached: Module 4 - Quiz 1
# ====================================
# File: Project #1
# ====================================
# Name: Salary
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# asking the user to enter the gross salary
salary = int(input("Enter the gross salary: "))

# calculating the subtotal
subtotal = salary * .10

# adding the 10% to the gross salary
total = subtotal + salary

# displaying the total
t = "{:,.2f}".format(total)
print("The total outcome: $", t)

''''
=================== Output ===========================
Enter the gross salary: 80000
The total outcome: $ 88,000.00

Process finished with exit code 0

'''

# ====================================
# Attached: Module 4 - Quiz 1
# ====================================
# File: Project #2
# ====================================
# Name: Scores
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# asking the user to enter 4 scores
test1 = int(input("Enter a score: "))
test2 = int(input("Enter a score: "))
test3 = int(input("Enter a score: "))
test4 = int(input("Enter a score: "))

# calculating the sum
total = test1 + test2 + test3 + test4

# calculating the average
average = total / 4

# displaying the total and the average
print("The total:", total)
print("The average: %.0f" % average)

''''
=================== Output ===========================
Enter a score: 60
Enter a score: 70
Enter a score: 80
Enter a score: 90
The total: 300
The average: 75

Process finished with exit code 0

'''

# ====================================
# Attached: Module 4 - Quiz 1
# ====================================
# File: Project #3
# ====================================
# Name: Name
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# asking the user their first name, last name and age
firstName = input("What is your first name? ")
lastName = input("What is your last name? ")
age = input("What is your age? ")

# displaying the first and last name including their age
print("The outcome:", firstName, lastName + ", " + age)

''''
=================== Output ===========================
What is your first name? Jacqueline
What is your last name? Ceballos Gomez
What is your age? 21
The outcome: Jacqueline Ceballos Gomez, 21

Process finished with exit code 0

'''

# ====================================
# Attached: Module 4 - Quiz 1
# ====================================
# File: Project #4
# ====================================
# Name: Sales and Commissions
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# asking the user to enter the sales
sales = int(input("Enter the sales: "))

# using an if-elif statement to assign the sales to the commission
# displaying the commission based off the sales
if 50000 <= sales <= 60000:
    print("The commission rate for this is 10%.")
elif 70000 <= sales <= 80000:
    print("The commission rate for this is 20%.")
elif 90000 <= sales <= 100000:
    print("The commission rate for this is 30%.")

''''
=================== Output ===========================
Enter the sales: 55000
The commission rate for this is 10%.

Process finished with exit code 0

Enter the sales: 77000
The commission rate for this is 20%.

Process finished with exit code 0

Enter the sales: 99000
The commission rate for this is 30%.

Process finished with exit code 0

'''

# ====================================
# Attached: Module 4 - Quiz 1
# ====================================
# File: Project #5
# ====================================
# Name: Sales and Commissions (Part 2)
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# asking the user to enter the sales
sales = int(input("Enter the sales: "))

# using an if-elif statement to assign the sales to the commission
# calculating the sales with the commission and adding it to the salary
# displaying the results
if 50000 <= sales <= 69000:
    subtotal = sales * .10
    total = subtotal + sales
    t = "{:,.2f}".format(total)
    print("The total outcome: $", t)
elif 70000 <= sales <= 80000:
    subtotal = sales * .20
    total = subtotal + sales
    t = "{:,.2f}".format(total)
    print("The total outcome: $", t)
elif 90000 <= sales <= 100000:
    subtotal = sales * .30
    total = subtotal + sales
    t = "{:,.2f}".format(total)
    print("The total outcome: $", t)

''''
=================== Output ===========================
Enter the sales: 65000
The total outcome: $ 71,500.00

Process finished with exit code 0

Enter the sales: 76000
The total outcome: $ 91,200.00

Process finished with exit code 0

Enter the sales: 98000
The total outcome: $ 127,400.00

Process finished with exit code 0

'''

# ====================================
# Attached: Module 4 - Quiz 1
# ====================================
# File: Project #6
# ====================================
# Name: Scores
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# assigning a variable
MAX_AVERAGE = 100

# asking the user to enter scores
test1 = int(input("Enter grade score: "))
test2 = int(input("Enter grade score: "))
test3 = int(input("Enter grade score: "))
test4 = int(input("Enter grade score: "))

# calculating the average
average = (test1 + test2 + test3 + test4) / 4

# using a while loop to displaying the following if the average is above 100.
while average > MAX_AVERAGE:
    print("You must re-enter the 4 scores. ")

    # using an if-elif statement to assign the averages to their letter grade
    # displaying the averages and their letter grade.
    if 90 <= average <= 100:
        print("The average score is", round(average))
        print("You got an A!")
    elif 80 <= average <= 89:
        print("The average score is", round(average))
        print("You got an B!")
    elif 70 <= average <= 79:
        print("The average score is", round(average))
        print("You got an C!")
    elif 60 <= average <= 69:
        print("The average score is", round(average))
        print("You got an D!")
    elif average < 60:
        print("The average score is", round(average))
        print("You got an F!")

    # stopping the loop from going on infinitely.
    break

''''
=================== Output ===========================
Enter grade score: 92
Enter grade score: 94
Enter grade score: 96
Enter grade score: 98
The average score is 95
You got an A!

Process finished with exit code 0

=================== Output 2 =========================
Enter grade score: 103
Enter grade score: 105
Enter grade score: 106
You must re-enter the 4 scores. 

Process finished with exit code 0

'''

# ====================================
# Attached: Module 4 - Quiz 1
# ====================================
# File: Project #7
# ====================================
# Name: Sum
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# assigning the variable
total = 0

# creating a loop that will display the sum of the number between 1 - 10
for number in range(1, 11):
    # adding two values and assigning it to a variable
    total += number
    # display the results
    print(total)

''''
=================== Output ===========================
1
3
6
10
15
21
28
36
45
55

Process finished with exit code 0

'''
