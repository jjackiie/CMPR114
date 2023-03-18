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

classA = 20
classB = 15
classC = 10


def main():
    a = float(input("Enter the number of tickets for Class A that were sold: "))
    show_classA(a)
    b = float(input("Enter the number of tickets for Class B that were sold: "))
    show_classB(b)
    c = float(input("Enter the number of tickets for Class C that were sold: "))
    show_classC(c)


def show_classA(a):
    total = a * classA
    A = "{:,.2f}".format(total)
    # displaying the results
    print("The total income for class A is: $" + A + "\n")


def show_classB(b):
    total = b * classB
    B = "{:,.2f}".format(total)
    # displaying the results
    print("The total income for class B is: $" + B + "\n")


def show_classC(c):
    total = c * classC
    C = "{:,.2f}".format(total)
    # displaying the results
    print("The total income for class B is: $" + C + "\n")


main()
''''   
=================== Output ===========================
Enter the number of tickets for Class A that were sold: 32
The total income for class A is: $640.00

Enter the number of tickets for Class B that were sold: 42
The total income for class B is: $630.00

Enter the number of tickets for Class C that were sold: 52
The total income for class B is: $520.00


Process finished with exit code 0

'''
