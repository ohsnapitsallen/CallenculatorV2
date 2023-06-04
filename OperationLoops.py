#Import or call the main calculator file
from CallenculatorV2 import *

#Create a class for looping which operations to use
class loop:
    def __init__(self, operate = ' '):
        self.choice = ' '
        while True:
            print("Please select what kind of calculator you would want to use")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")

            self.choice = input("Enter your choice (1-4): ")
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                #Make an if-statement which calls all the functions from the main calculator file depending on the user input
                if self.choice == '1':
                    operate = add()
                    operate.solve(num1, num2)
                    print("Sum:", operate.result)
                    break

                elif self.choice == '2':
                    operate = subtract()
                    operate.solve(num1, num2)
                    print("Difference:", operate.result)
                    break

                elif self.choice == '3':
                    operate = multiply()
                    operate.solve(num1, num2)
                    print("Product:", operate.result)
                    break

                elif self.choice == '4':
                    operate = divide()
                    operate.solve(num1, num2)
                    print("Quotient:", operate.result)
                    break

                else:
                    print("Numbers ain't that hard to learn buddy. (Enter only numbers from 1 to 4)")
                    
            except ValueError:
                print("Error: Looks like someone doesn't know their ABCs and 123s (Please enter numbers only).")
                
            except ZeroDivisionError:
                print("Error: Have you tried dividing 0 cookies to your 0 friends (You cannot devide by zero)")

                

                
#Create another class to ask the user if they want to try the calculator again.
class question:
    def __init__(self):
        self.response = ' '
        while self.response != "n":
            self.response = input("Do you want to try the calculator again? (Answer with 'y' or 'n' only.): ")

            if self.response == "y":
                loop()
            elif self.response == "n":
                print("Thank You")
                break
            else:
                print("Hey! that's not 'y' nor 'n'. (Please Try Again)")
