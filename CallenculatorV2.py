#Create a class for the calculator
class Callenculator:
    #Use the init function to set default values for variables and a welcome message
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.result = 0
        print("Welcome to Callenculator! The sassiest calculator you can find.")
        
    #Create a function for addition
    def add(self):
        try:
            self.num1 = float(input("Enter the first number: "))
            self.num2 = float(input("Enter the second number: "))
            self.result = self.num1 + self.num2
            print("Sum:", self.result)
        except ValueError:
            print("Error: Looks like someone doesn't know their ABCs and 123s (Please enter numbers only).")
#Create a function for subtraction
#Create a function for multiplication
#Create a function for division            
#Create a variable for the class 
