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

print("Low: %.2f" % min(numbers))

print("High: %.2f" % max(numbers))

print("Total: %.2f" % total)

print("Average: %.2f" % (total / 20.0))


''''
=================== Output ===========================


'''