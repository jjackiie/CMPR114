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

# this function will allow the user to write the input
def write():
    print("----Enter your information----")

    # asking the user to enter ir first, last name with their age
    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")
    age = input("Enter your age: ")

    # writing to the default directory
    # the letter a means to append
    info = open("m6_textFile_challenge1.txt", 'a')

    # writing the contents to a file
    info.write(firstName + "\n")
    info.write(lastName + "\n")
    info.write(age + "\n")

    info.close()

    print("\nInfo recorded! \n")


write()


# this program will read from the file
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

# this function will allow the user to write the input
def writeNumbers():
    # writing to the default directory
    # the letter a means append
    outfile = open("m6_numbers.txt", "a")

    # asking the user to enter 3 digits
    num1 = int(input("Enter #1: "))
    num2 = int(input("Enter #2: "))
    num3 = int(input("Enter #3: "))

    # calculating the total and the average
    sum = num1 + num2 + num3
    average = sum / 3

    # writing the contents to a file
    outfile.write("The 1st number is " + str(num1) + "\n")
    outfile.write("The 2nd number is " + str(num2) + "\n")
    outfile.write("The 3rd number is " + str(num3) + "\n")
    outfile.write("\nThe average number is " + str(average) + "\n")
    outfile.write("\nThe total number is " + str(sum) + "\n")

    outfile.close()

    print("\nDate Recorded!")


writeNumbers()


# this program will read from the file
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


# ====================================
# Attached: Class Exercise #6
# ====================================
# File: Challenge #3
# ====================================
# Name: Sales Data
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

def sales():
    num_days = int(input("Enter the days of sales: "))
    sales_files = open("m6_sales.txt", "a")

    # start with 1, and increment by 1 based on the input
    for count in range(1, num_days + 1):
        # inside the loop because it's nested after the for loop
        sales = float(input("Enter the sales for Day #" + str(count) + ": "))
        sales_files.write(str(sales) + "\n")

    # outside the loop, by indenting
    sales_files.close()

    print("Sales Recorded!")

    salary = int(input("\nEnter your salary: "))
    if salary <= 1000:
        print(salary)
    elif salary > 1000:
        subtotal = (salary * .10)
        total = subtotal + salary
        print("The total is " + str(total))


sales()


def readSales():
    sales_file = open("m6_sales.txt", "r")

    line = sales_file.readline()

    # as long an empty string is NOT returned
    while line != " ":
        amount = float(line)

        print(format(amount, ".2f"))

        line = sales_file.readline()

    sales_file.close()


readSales()

''''
=================== Output ===========================
Enter the days of sales: 5
Enter the sales for Day #1: 1000
Enter the sales for Day #2: 1000
Enter the sales for Day #3: 1000
Enter the sales for Day #4: 1000
Enter the sales for Day #5: 1000
Sales Recorded!

Enter your salary: 80000
The total is 88000.0

Process finished with exit code 1

'''

# ====================================
# Attached: Class Exercise #6
# ====================================
# File: Challenge #4
# ====================================
# Name: Records
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

def main():
    num_emps = int(input("Enter the number of employee records: "))

    emp_file = open("m6_employee.txt", "w")

    for count in range(1, num_emps + 1):
        print("Enter data for employee #", count)

        name = input("Name: ")
        id_num = input("ID #: ")
        dept = input("Department: ")

        emp_file.write(name + "\n")
        emp_file.write(id_num + "\n")
        emp_file.write(dept + "\n")

        print()

        emp_file.close()

        print("Recorded!\n")


# calling the main function
main()


def read():
    infile = open("m6_employee.txt", "r")

    fileContents = infile.read()

    infile.close()

    print(fileContents)


read()

''''
=================== Output ===========================
Enter the number of employee records: 1
Enter data for employee # 1
Name: Josh Richard
ID #: 101
Department: Finance

Recorded!

Josh Richard
101
Finance


Process finished with exit code 0

'''

# ====================================
# Attached: Class Exercise #6
# ====================================
# File: Challenge #5
# ====================================
# Name: Transferring Info
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# import the gui interface controls
import tkinter as tk
from tkinter import messagebox

# create the window interface
win = tk.Tk()
# width x height in pixels
win.geometry("500x300")
# label for the title
win.title("Customer Information")

# labeling the widgets
tk.Label(win, text="Enter the last name").grid(column=0, row=0)
tk.Label(win, text="Enter the first name").grid(column=0, row=1)
tk.Label(win, text="Enter the address").grid(column=0, row=2)
tk.Label(win, text="Enter the city").grid(column=0, row=3)
tk.Label(win, text="Enter the state").grid(column=0, row=4)
tk.Label(win, text="Enter the zipcode").grid(column=0, row=5)


def write():
    text_file = open("m6_customers.txt", "a")
    content = text_file.write("\nConfirmation: " + str(LN.get()) + "," + str(FN.get()) + ",\n" + str(AD.get()) + " "
                              + str(C.get()) + "," + str(S.get()) + "," + str(ZIP.get()))
    text_file.close()
    messagebox.showinfo("information", "Data recorded")


def quit():
    messagebox.showinfo("information", "Thank you . . .")
    # closes the interfaces
    win.destroy()


# function name
def submit():
    # display info
    messagebox.showinfo("information",
                        "entered: " + LN.get() + "," + FN.get() + AD.get() + "," + C.get() + "," + S.get() + "," + ZIP.get())


# the StringVar() manages the entry widgets
LN = tk.StringVar()
# text entry widget
tk.Entry(win, width=12, textvariable=LN).grid(column=1, row=0)

# the StringVar() manages the entry widgets
FN = tk.StringVar()
# text entry widget
tk.Entry(win, width=12, textvariable=FN).grid(column=1, row=1)

# the StringVar() manages the entry widgets
AD = tk.StringVar()
# text entry widget
tk.Entry(win, width=12, textvariable=AD).grid(column=1, row=2)

# the StringVar() manages the entry widgets
C = tk.StringVar()
# text entry widget
tk.Entry(win, width=12, textvariable=C).grid(column=1, row=3)

# the StringVar() manages the entry widgets
S = tk.StringVar()
# text entry widget
tk.Entry(win, width=12, textvariable=S).grid(column=1, row=4)

# the StringVar() manages the entry widgets
ZIP = tk.StringVar()
# text entry widget
tk.Entry(win, width=12, textvariable=ZIP).grid(column=1, row=5)

# command calls the click function
# button widget
tk.Button(win, text="submit", command=submit).grid(column=1, row=7)

# command calls the quit function
# button widget
tk.Button(win, text="quit", command=quit).grid(column=2, row=7)

# command calls the function write
# button widget
tk.Button(win, text="transfer", command=write).grid(column=3, row=7)

# ensures the interfaces stays on the screen or window
win.mainloop()
submit()

''''
=================== Output ===========================

Process finished with exit code 0

'''

