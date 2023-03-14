# ====================================
# Attached: Class Exercise #3
# ====================================
# File: Challenge #1
# ====================================
# Name:
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
# Attached: Class Exercise #3
# ====================================
# File: Challenge #2
# ====================================
# Name:
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

def main():
    first_name = input("Enter your first name: ")

    last_name = input("Enter your last name: ")

''''
=================== Output ===========================


'''
