#Import or call the main calculator file
from CallenculatorV2 import *

#Create a class for looping which operations to use
class loop:
    def __init__(self):
        self.choice = ' '
        while True:
            print("Please select what kind of calculator you would want to use")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")

            self.choice = input("Enter your choice (1-4): ")

            #Make an if-statement which calls all the functions from the main calculator file depending on the user input
            if self.choice == '1':
                    callenculator.add()
                    break

            elif self.choice == '2':
                    callenculator.subtract()
                    break

            elif self.choice == '3':
                    callenculator.multiply()
                    break

            elif self.choice == '4':
                    callenculator.divide()
                    break

            else:
                print("Invalid choice. Please enter a number from 1 to 6.")

#Create another class to ask the user if they want to try the calculator again.
