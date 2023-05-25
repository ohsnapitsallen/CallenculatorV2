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
                print("Numbers ain't that hard to learn buddy. (Enter only numbers from 1 to 4)")

                
#Create another class to ask the user if they want to try the calculator again.
class question:
    def __init__(self):
        self.response = ' '
        while self.response != "n":
            self.response = input("Do you want to try the calculator again? (Answer with 'y' or 'n' only.): ")

            if self.response == "y":
                loop()
            elif self.response == "n":
                break
            else:
                print("Hey! that's not 'y' nor 'n'. (Please Try Again)")
