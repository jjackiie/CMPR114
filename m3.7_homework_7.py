# ====================================
# Attached: m3.7 Homework #7
# ====================================
# File: Project #1
# ====================================
# Name: Lowest Scores
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# the get_scores function gets a series of test scores from the user
# and stores them in a list. A reference to the list is returned.

def get_scores():
    # create a empty list
    test_scores = []

    # create a variable to control the loop
    again = "y"

    # get the scores from the user and add them to the list
    while again == "y":
        # get a score and add it to the list
        value = float(input("Enter a test score: "))
        test_scores.append(value)

        # want to do this again?
        print("Do you want to add another score?")
        again = input("y = yes, anything else = no: ")
        print()

    # return the list
    return test_scores


# the get_total function accepts a list as an argument returns the total of the values in the list
def get_total(value_list):
    # create a variable to use an accumulator
    total = 0.0

    # calculate the total of the list elements
    for num in value_list:
        total += num

    # return the total
    return total


# call the main function
if __name__ == "__main__":
    get_scores()

''''
=================== Output ===========================
Enter a test score: 88
Do you want to add another score?
y = yes, anything else = no: y

Enter a test score: 89
Do you want to add another score?
y = yes, anything else = no: y

Enter a test score: 79
Do you want to add another score?
y = yes, anything else = no: n


Process finished with exit code 0

'''


# ====================================
# Attached: m3.7 Homework #7
# ====================================
# File: Project #2
# ====================================
# Name: Number Analysis Program
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# assigning the variables
numbers = []
total = 0

# using a for loop range to loop 20 times
for i in range(20):
    # asking the user to enter a series of 20 numbers
    number = (int(input('Enter number ' + str(i + 1) + ' of 20: ')))
    numbers.append(number)

    # adding two values and assigning it to a variable
    total += number

# display the lowest number in the list
print("\nLowest: %.2f" % min(numbers))

# display the highest number in the list
print("Highest: %.2f" % max(numbers))

# display the total of the numbers in the list
print("Total: %.2f" % total)

# display the average of the numbers in the list
print("Average: %.2f" % (total / 20.0))


''''
=================== Output ===========================
Enter number 1 of 20: 1
Enter number 2 of 20: 2
Enter number 3 of 20: 3
Enter number 4 of 20: 4
Enter number 5 of 20: 5
Enter number 6 of 20: 6
Enter number 7 of 20: 7
Enter number 8 of 20: 8
Enter number 9 of 20: 9
Enter number 10 of 20: 11
Enter number 11 of 20: 22
Enter number 12 of 20: 33
Enter number 13 of 20: 44
Enter number 14 of 20: 55
Enter number 15 of 20: 66
Enter number 16 of 20: 77
Enter number 17 of 20: 88
Enter number 18 of 20: 99
Enter number 19 of 20: 111
Enter number 20 of 20: 222

Lowest: 1.00
Highest: 222.00
Total: 873.00
Average: 43.65

Process finished with exit code 0

'''