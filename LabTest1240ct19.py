#######################################################################################
# Program Description: Program that displays Pascal's Triangle based on the height a
# user inputs.
# Author: Thamsanqa Sibanda
# Date: 24/10/2019
# Compiler: PyCharm Python 3.x
# Text Editor: PyCharm
######################################################################################

import math
import string

# function to generate elements in a row
def rows(x,y):

    # Code to calculate each item that goes into the row
    return int((math.factorial(x)) / ((math.factorial(y)) * math.factorial(x - y)))


#function to make new rows
def make_new_row(num_rows):

    # Store results
    asnwer = []

    # for loop to generate row
    for i in range(num_rows):
        # store the elements in the row
        row = []
        for k in range(i + 1):
            row.append(rows(i,k))
        asnwer.append(row)
    return asnwer

# funcction to display each row
def display_rows(num_of_rows):
    # for loop will display earch row and center it.
    for rows in make_new_row(num_of_rows):
        print(' '.join([str(i) for i in rows]).center(100))



#ask user for input, ie. ask height of triangle and to check if input is a number
num_of_rows = 'a'
chkr=0
# code to validate input
while chkr !=1:
    num_of_rows = input("Enter the desired height of Pascal's triangle: ")
    if num_of_rows in string.digits and num_of_rows > '0':
        chkr = 1
    else:
        print("Invalid input, only positive integers allowed! Please try again")

# display each row
display_rows(int(num_of_rows))
