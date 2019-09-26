###########################################################
# Program Description: Program to convert Decimal to Binary
# Date: 26 September 2019
# Author: Thamsanqa Steven Sibanda
###########################################################

# get input from the user
num = input("Enter a positive number your would like to convert to binary: ")
usrNum = num
binNum = int(num) % 2
result = ""

# Convert the users number into binary
if int(num) == 0:
    print("Binary form of 0 is 0")
else:
    while int(num) > 0:
        tmpNum = int(num) % 2
        #print(tmpNum) used to test code and see each step of code
        result = str(tmpNum) + result
        num = int(num) / 2
    # end while loop
    # Display the results
    print("The binary form of",usrNum, "is",result)
# end if else statement#