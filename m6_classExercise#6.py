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
'''
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
'''
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
'''
def sales():
    num_days = int(input("Enter the days of sales: "))
    sales_files = open("m6_sales.txt", "a")

    for count in range(1, num_days + 1):
        sales = float(input("Enter the sales for Day #" + str(count) + ": "))
        sales_files.write(str(sales) + "\n")
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

    while line != " ":
        amount = float(line)

        print(format(amount, ".2f"))

        line = sales_file.readline()

    sales_file.close()


readSales()
'''
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
'''
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


main()


def read():
    infile = open("m6_employee.txt", "r")

    fileContents = infile.read()

    infile.close()

    print(fileContents)


read()
'''
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
import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.geometry("500x300")
win.title("Customer Information")

tk.Label(win, text="Enter the last name").grid(column=0, row=0)
tk.Label(win, text="Enter the first name").grid(column=0, row=1)
tk.Label(win, text="Enter the address").grid(column=0, row=2)
tk.Label(win, text="Enter the city").grid(column=0, row=3)
tk.Label(win, text="Enter the state").grid(column=0, row=4)
tk.Label(win, text="Enter the zipcode").grid(column=0, row=5)


def write():
    text_file = open("m6_customers.txt", "a")
    content = text_file.write("\nConfirmation: " + str(LN.get()) + "," + str(FN.get()) + ",\n" + str(AD.get()) + " " + str(C.get()) + "," + str(S.get()) + "," + str(ZIP.get()))
    text_file.close()
    messagebox.showinfo("information", "Data recorded")


def quit():
    messagebox.showinfo("information", "Thank you . . .")
    win.destroy()


def submit():
    messagebox.showinfo("information", "entered: " + LN.get() + "," + FN.get() + AD.get() + "," + C.get() + "," + S.get() + "," + ZIP.get())


LN = tk.StringVar()
txtLastname = tk.Entry(win, width=12, textvariable=LN).grid(column=1, row=0)
FN = tk.StringVar()
txtFirstname = tk.Entry(win, width=12, textvariable=FN).grid(column=1, row=1)
AD = tk.StringVar()
txtAddress = tk.Entry(win, width=12, textvariable=AD).grid(column=1, row=2)
C = tk.StringVar()
txtCity = tk.Entry(win, width=12, textvariable=C).grid(column=1, row=3)
S = tk.StringVar()
txtState = tk.Entry(win, width=12, textvariable=S).grid(column=1, row=4)
ZIP = tk.StringVar()
txtZipcode = tk.Entry(win, width=12, textvariable=ZIP).grid(column=1, row=5)


tk.Button(win, text="submit", command=submit).grid(column=1, row=7)

tk.Button(win, text="quit", command=quit).grid(column=2, row=7)

tk.Button(win, text="transfer", command=write).grid(column=3, row=7)

win.mainloop()
submit()


''''
=================== Output ===========================

Process finished with exit code 0

'''
