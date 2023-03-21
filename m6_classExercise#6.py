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
