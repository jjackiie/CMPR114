# ====================================
# Attached: m5 Homework #5
# ====================================
# File: Project #1
# ====================================
# Name: Property Tax
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# assigning the variables
assessment_value = 0.60
property_tax = 0.0072


def main():
    # asking the user the value of their property
    property_value = float(input("Enter the actual value of a piece of property? "))
    # calling the function
    show_value(property_value)


def show_value(property_value):
    # calculating the assessment value
    property = property_value * assessment_value
    # formatting the results
    p = "{:,.2f}".format(property)
    # displaying the results
    print("The assessment value: $" + p)

    # calculating the property tax
    tax = property * property_tax
    # formatting the results
    t = "{:,.2f}".format(tax)
    # displaying the results
    print("The property tax: $" + t)


# calling the main function
main()

''''
=================== Output ===========================
Enter the actual value of a piece of property? 10000
The assessment value: $6,000.00
The property tax: $43.20

Process finished with exit code 0

'''

# ====================================
# Attached: m5 Homework #5
# ====================================
# File: Project #2
# ====================================
# Name: Stadium Seating
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# assigning the variables
classA = 20
classB = 15
classC = 10


def main():
    # asking the user the # of tickets in Class A
    a = float(input("Enter the number of tickets for Class A that were sold: "))
    # calling the function
    show_classA(a)

    # asking the user the # of tickets in Class B
    b = float(input("Enter the number of tickets for Class B that were sold: "))
    # calling the function
    show_classB(b)

    # asking the user the # of tickets in Class C
    c = float(input("Enter the number of tickets for Class C that were sold: "))
    # calling the function
    show_classC(c)


def show_classA(a):
    # calculating the total income for class A
    total = a * classA
    # formatting the results
    A = "{:,.2f}".format(total)
    # displaying the results
    print("The total income for class A is: $" + A + "\n")


def show_classB(b):
    # calculating the total income for class B
    total = b * classB
    # formatting the results
    B = "{:,.2f}".format(total)
    # displaying the results
    print("The total income for class B is: $" + B + "\n")


def show_classC(c):
    # calculating the total income for class C
    total = c * classC
    # formatting the results
    C = "{:,.2f}".format(total)
    # displaying the results
    print("The total income for class C is: $" + C + "\n")


# calling the main function
main()

''''   
=================== Output ===========================
Enter the number of tickets for Class A that were sold: 32
The total income for class A is: $640.00

Enter the number of tickets for Class B that were sold: 42
The total income for class B is: $630.00

Enter the number of tickets for Class C that were sold: 52
The total income for class C is: $520.00


Process finished with exit code 0

'''

# ====================================
# Attached: m5 Homework #5
# ====================================
# File: Project #3
# ====================================
# Name: Monthly Sales Tax
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# assigning the variables
state_tax = 0.05
county_tax = 0.025


def main():
    # asking the user the total sales
    sales = float(input("Enter the total sales for this month: "))
    # calling the function
    show_Sales(sales)


def show_Sales(sales):
    # calculating the county sales tax
    county = sales * state_tax
    # formatting the results
    c = "{:,.2f}".format(county)
    # displaying the results
    print("The amount of county sales tax is $" + c + "\n")

    # calculating the state sales tax
    state = sales * county_tax
    # formatting the results
    s = "{:,.2f}".format(state)
    # displaying the results
    print("The amount of state sales tax is $" + s + "\n")

    # calculating the total sales tax
    total_tax = county + state
    # formatting the results
    t = "{:,.2f}".format(total_tax)
    # displaying the results
    print("The amount of total sales tax is $" + t)


# calling the main function
main()

''''   
=================== Output ===========================
Enter the total sales for this month: 60000
The amount of county sales tax is $3,000.00

The amount of state sales tax is $1,500.00

The amount of total sales tax is $4,500.00

Process finished with exit code 0

'''
