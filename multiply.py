import os
import sys
os.system('cls')
os.system('whoami')
os.system('hostname')
os.system('date /t')
os.system('time /t')
print("Python Version: " + sys.version)
print("This program multiplies two numbers.")
print("\n")
firstnum = int(input("Enter first number: "))
secondnum = int(input("Enter second number: "))
product = firstnum * secondnum
print("Product of:" + str(firstnum) + " and " + str(secondnum) + " is " + product)
   