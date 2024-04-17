import os
os.system('cls')
name = input("Enter your name: ")
age = input("Enter your age: ")
print("\n\nHello " + name + "!")
print("\nWow!! You are " + age + " years old")
if int(age) >= 18:
    print("\nCongratulations!!! You are an adult")
else:
    print("\nYou have to wait for " + str(18-int(age)) + " more year(s) to become an adult")
print("\nThank you for using this program " + name + "!")
