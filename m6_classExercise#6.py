# ====================================
# Attached: Class Exercise #6
# ====================================
# File: Challenge #1
# ====================================
# Name: User Info
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================
'''
def write():
    print("----Enter your information----")

    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")
    age = input("Enter your age: ")

    info = open("m6_textFile_challenge1.txt", 'a')

    info.write(firstName + "\n")
    info.write(lastName + "\n")
    info.write(age + "\n")

    info.close()

    print("\nInfo recorded! \n")


write()


def read():
    infile = open("m6_textFile_challenge1.txt", "r")

    fileContents = infile.read()

    infile.close()

    print(fileContents)


read()
'''
''''
=================== Output ===========================
----Enter your information----
Enter your first name: Jacqueline
Enter your last name: Ceballos
Enter your age: 21

Info recorded! 

Jacqueline
Ceballos
21


Process finished with exit code 0

'''


# ====================================
# Attached: Class Exercise #6
# ====================================
# File: Challenge #2
# ====================================
# Name: Write Numbers
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

def writeNumbers():
    outfile = open("m6_numbers.txt", "a")

    num1 = int(input("Enter #1: "))
    num2 = int(input("Enter #2: "))
    num3 = int(input("Enter #3: "))

    sum = num1 + num2 + num3
    average = sum / 3

    outfile.write("The 1st number is " + str(num1) + "\n")
    outfile.write("The 2nd number is " + str(num2) + "\n")
    outfile.write("The 3rd number is " + str(num3) + "\n")
    outfile.write("\nThe average number is " + str(average) + "\n")
    outfile.write("\nThe total number is " + str(sum) + "\n")

    outfile.close()

    print("\nDate Recorded!")


writeNumbers()


def read():
    infile = open("m6_numbers.txt", "r")

    fileContents = infile.read()

    infile.close()

    print(fileContents)


read()

''''
=================== Output ===========================
Enter #1: 22
Enter #2: 33
Enter #3: 44

Date Recorded!

The 1st number is 22
The 2nd number is 33
The 3rd number is 44

The average number is 33.0

The total number is 99


Process finished with exit code 0

'''
