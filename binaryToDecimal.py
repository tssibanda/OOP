###########################################################
# Program Description: Program to convert Binary to Decimal
# Date: 26 September 2019
# Author: Thamsanqa Steven Sibanda
###########################################################

usrBinNum = input("Enter the binary number: ")
binNum = len(usrBinNum)-1
result = 0
bits = 0
power =

while binNum !=0:

    if usrBinNum[binNum] != 0:
        binNum = binNum - 1
        bits = bits ** power


