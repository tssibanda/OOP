#######################################################################################
# Program Description: Program that displays Pascal's Triangle based on the height
# user inputs.

""" Second Submission Notes: The first program I submitted used the factorial method of generating Pascal's
    Triangle, however this version of the same problem uses several functions that generate lists. It stores a list of
    numbers for each row in one list It then prints each row separately and finally prints a string version of the rows
    in the shape of a triangle.
"""

# Author: Thamsanqa Sibanda
# Date: 07/11/2019
# Compiler: PyCharm Python 3.x
# Text Editor: PyCharm
######################################################################################

# function find the length of a list
def lenth(L):
    # count the number of elements in a list
    counter = 0
    for n in L:
        counter += 1
    return counter

# Function to create new rows
def make_new_row(old_row):

    # Container for new row
    new_row = []

    #add tmp index with a value of 0 to the end of the old row to allow the addition of the last element
    tmp_old_row = old_row.copy()
    tmp_old_row.append(0)

    # count elements in list
    len_old_row = lenth(tmp_old_row)

    # Generate rows in the list
    if old_row == []:# create first row
        new_row.append(1)
    elif old_row == [1]: # create second row
        for i in range(0,2):
            new_row.append(1)
    else:
        # create third row or onward.
        new_row.append(1)
        for n in range(0,len_old_row-1):
            new_row.append(tmp_old_row[n]+tmp_old_row[n+1])

    return new_row

# Function to print list rows without the commas and the square brackets
def stringfy_n_centre(list):
        for item in list:
            print(' '.join(str(i) for i in item).center(100))

# function to display all requirements for lab test
def Display_Pascals_Triangle():

    old_row=[]
    list_of_rows = []
    # get the user's desired height.

    # validate user's input, only positive integers allowed.
    while True:
        try:
            height = int(input("Enter the desired height of Pascal's triangle: "))
            height = int(height)
            if height > 2:
                break
            else:
                print("Please enter a number greater than 2.")
        except ValueError:
            print("Invalid integer! Please try again ...")


    # generate lists for pascal's table
    for i in range(0,height):
        old_row = make_new_row(old_row)
        list_of_rows.append(old_row)

    # print whole list of lists
    print("Printing whole list of lists:")
    print(list_of_rows)

    # Print list of lists, one list at a time
    print("Printing list of lists, one list at a time:")
    for i in list_of_rows:
        print(i)

    # print one list at a time, centered and without punctuation
    stringfy_n_centre(list_of_rows)

# Display Pascal's Triangle
Display_Pascals_Triangle()