###########################################################
# Program Description: Program to convert Binary to Decimal
# Date: 26 September 2019
# Author: Thamsanqa Steven Sibanda
###########################################################

binary = input("Enter the binary number: ")
tempBin = binary
decimal = 0
i=0

while int(binary) != 0:
    dec = int(binary) % 10
    decimal = decimal + dec * pow(2,i)
    binary = int(binary) // 10
    i += 1
print(decimal)
