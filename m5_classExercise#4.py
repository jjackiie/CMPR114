# ====================================
# Attached: Class Exercise #4
# ====================================
# File: Challenge #1
# ====================================
# Name: Birds
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# this program demonstrates two functions that have local variables with the same name.

def main():
    # call the texas function.
    texas()
    # call the california function
    california()


# definition of the texas function. it creates a local variable named birds.
def texas():
    # asking the user to enter the number of birds in each state
    birds = int(input("How many birds are there in texas? "))
    # displaying the results
    b = "{:,.0f}".format(birds)
    print("Texas has", b, "birds.")


# definition of the texas function. it creates a local variable named birds.
def california():
    # asking the user to enter the number of birds in each state
    birds = int(input("How many birds are there in california? "))
    # displaying the results
    b = "{:,.0f}".format(birds)
    print("California has", b, "birds.")


# call the main function
main()

''''
=================== Output ===========================
How many birds are there in texas? 5000
Texas has 5,000 birds.
How many birds are there in california? 8000
California has 8,000 birds.

Process finished with exit code 0


'''

# ====================================
# Attached: Class Exercise #4
# ====================================
# File: Challenge #2
# ====================================
# Name: About You
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# this program with a function that allows the user to enter
# the last, first names, address, city, state, with zipcode.

def main():
    # asking the user to enter their first name
    first_name = input("Enter your first name: ")

    # asking the user to enter their last name
    last_name = input("Enter your last name: ")

    # asking the user to enter their address
    address = input("Enter your address: ")

    # asking the user to enter their city
    city = input("Enter your city: ")

    # asking the user to enter their state
    state = input("Enter your state: ")

    # asking the user to enter their zipcode
    zipcode = input("Enter your zipcode: ")

    # displaying and formatting the results
    print("\n" + first_name, last_name)
    print(address)
    print(city + "," + state, zipcode)


# call the main function
main()

''''
=================== Output ===========================
Enter your first name: Jacqueline
Enter your last name: Ceballos
Enter your address: 123 Carl St
Enter your city: Orange
Enter your state: CA
Enter your zipcode: 12345

Jacqueline Ceballos
123 Carl St
Orange,CA 12345

Process finished with exit code 0

'''

# ====================================
# Attached: Class Exercise #4
# ====================================
# File: Challenge #3
# ====================================
# Name: Adding
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# using global variable, this program will add 3+4+5 using a function named add

# create a global variable.
total = 0


def add(num1, num2, num3):
    # using the global variable
    global total
    # calculating the total
    total = num1 + num2 + num3
    return total


# adding the three numbers together
add(3, 4, 5)
# displaying the total
print("The total after adding the three number together is", total, ".")

''''
=================== Output ===========================
The total after adding the three number together is 12 .

Process finished with exit code 0

'''

# ====================================
# Attached: Class Exercise #4
# ====================================
# File: Challenge #4
# ====================================
# Name: Numbers
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# using global variable, this program will add three number that
# the user enter. Also, the sum and average of the three numbers.

# create a global variable
total = 0
avg = 0


def add(num1, num2, num3):
    # using the global variable
    global total
    # calculating the total
    total = float(num1) + float(num2) + float(num3)

    return float(total)


def average(num1, num2, num3):
    # using the global variable
    global avg
    # calculating the average
    avg = (float(num1) + float(num2) + float(num3)) / 3

    return float(avg)


# asking the user to enter three numbers
num1 = input("Enter a number: ")
num2 = input("Enter a number: ")
num3 = input("Enter a number: ")

# displaying the total
print("The total is " + str(add(num1, num2, num3)))

# displaying the average
print("The average is " + str(average(num1, num2, num3)))

''''
=================== Output ===========================
Enter a number: 55
Enter a number: 44
Enter a number: 33
The total is 132.0
The average is 44.0

Process finished with exit code 0

'''

# ====================================
# Attached: Class Exercise #4
# ====================================
# File: Challenge #5
# ====================================
# Name: Pay Rate
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# this program will ask the user to enter the hours worked
# and hourly pay using function. The outcome will display the total.

def wage(hourly, hrs):
    # calculating the total
    salary = float(hourly) * float(hrs)

    return float(salary)


# asking the user to enter their hours and hourly pay
hrs = input("Enter your hours: ")
hourly = input("Enter your hourly rate: ")

# displaying the total
print("The total salary is " + str(wage(hrs, hourly)))

''''
=================== Output ===========================
Enter your hours: 40
Enter your hourly rate: 12
The total salary is 480.0

Process finished with exit code 0

'''

# ====================================
# Attached: Class Exercise #4 (Part 2)
# ====================================
# File: Challenge #1
# ====================================
# Name: Kilometer Converter
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# create a global variable
miles = 0


def convert(kilometers):
    # using the global variable
    global miles
    # converting km to miles
    miles = kilometers * 0.6214
    return float(miles)


# asking the user to enter the distance
kilometers = float(input("Enter a distance in kilometers: "))

# displaying the results after the conversion
print("Miles = " + str(convert(kilometers)))

''''
=================== Output ===========================
Enter a distance in kilometers: 111
Miles = 68.9754

Process finished with exit code 0

'''

# ====================================
# Attached: Class Exercise #4 (Part 2)
# ====================================
# File: Challenge #2
# ====================================
# Name: Automobile Costs
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# create a global variable
monthly = 0
annually = 0


def month_cost():
    # using the global variable
    global monthly
    # calculating the monthly cost
    monthly = float(loan) + float(insurance) + float(gas) + float(tires) + float(maintenance)

    return float(monthly)


def annual_cost():
    # using the global variable
    global annually
    # calculating the annually cost
    annually = (float(loan) + float(insurance) + float(gas) + float(tires) + float(maintenance)) * 12

    return float(annually)


# asking the user their monthly expenses
loan = float(input("Enter the monthly loan payment: $"))
insurance = float(input("Enter the monthly insurance cost: $"))
gas = float(input("Enter the monthly gas cost: $"))
tires = float(input("Enter the monthly tires cost: $"))
maintenance = float(input("Enter the monthly maintenance cost: $"))

# displaying the total monthly cost
print("\nThe total monthly automobile cost is " + str(month_cost()))

# displaying the total monthly cost
print("The total annually automobile cost is " + str(annual_cost()))

''''
=================== Output ===========================
Enter the monthly loan payment: $506
Enter the monthly insurance cost: $55
Enter the monthly gas cost: $160
Enter the monthly tires cost: $155
Enter the monthly maintenance cost: $200

The total monthly automobile cost is 1076.0
The total annually automobile cost is 12912.0

Process finished with exit code 0

'''
