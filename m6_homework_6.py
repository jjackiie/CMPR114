# ====================================
# Attached: m6 Homework #6
# ====================================
# File: Project #1
# ====================================
# Name: Things
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# this function will allow the user to write the input
def write():
    # assigning the variables
    animal = "panda"
    fruit = "apple"
    country = "africa"

    # writing to the default directory
    # the letter a means to append
    info = open("things.txt", 'a')

    # writing the contents to a file
    info.write(animal + "\n")
    info.write(fruit + "\n")
    info.write(country + "\n")

    # closes the file
    info.close()

    print("\nInfo recorded! \n")


write()

''''
=================== Output ===========================

Info recorded! 


Process finished with exit code 0

'''


# ====================================
# Attached: m6 Homework #6
# ====================================
# File: Project #2
# ====================================
# Name: Displaying
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# this program will read from the file
def read():
    infile = open("things.txt", "r")

    fileContents = infile.read()

    infile.close()

    print(fileContents)


read()

''''
=================== Output ===========================
panda
apple
africa


Process finished with exit code 0

'''


# ====================================
# Attached: m6 Homework #6
# ====================================
# File: Project #3
# ====================================
# Name: Lists
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# this function will allow the user to write the input
def write():

    # writing to the default directory
    # the letter a means to append
    info = open("number_list.txt", 'a')

    # writing the contents to a file
    for i in range(1,101):
        info.write(str(i))
        info.write("\n")

    # closes the file
    info.close()

    print("Number Written! \n")


write()

''''
=================== Output ===========================
Number Written! 


Process finished with exit code 0

'''


# ====================================
# Attached: m6 Homework #6
# ====================================
# File: Project #4
# ====================================
# Name: Sum of Numbers
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# this function will allow the user to write the input
def write():

    # writing to the default directory
    # the letter a means to append
    info = open("number_list.txt", 'a')

    # writing the contents to a file
    for i in range(1,101):
        info.write(str(i))
        info.write("\n")

    # closes the file
    info.close()

    print("Number Written! \n")


write()

''''
=================== Output ===========================
Number Written! 


Process finished with exit code 0

'''
