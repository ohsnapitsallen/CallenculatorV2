print("Welcome to Callenculator! The sassiest calculator you can find.")
#Create a class for the calculator
class Callenculator:
    #Use the init function to set default values for variables
    def __init__(self):
        self.result = 0
        
    def solve(self, num1, num2):
        pass
    
#Create an inheritcance class for for addition
class add(Callenculator):
    def solve(self, num1, num2):
        try:
            self.result = num1 + num2
        except Exception as e:
            print("Something went wrong:", e)
    
#Create an inheritance for subtraction
class subtract(Callenculator):
    def solve(self, num1, num2):
        try:
            self.result = num1 + num2
        except Exception as e:
            print("Something went wrong:", e)
            
#Create an inheritance for multiplication
class multiply(Callenculator):
    def solve(self, num1, num2):
        try:
            self.result = num1 * num2
        except Exception as e:
            print("Something went wrong:", e)

#Create an inheritance for division
class divide(Callenculator):
    def solve(self, num1, num2):
        try:
            self.result = num1 / num2
        except Exception as e:
            print("Something went wrong:", e)
#Create a variable for the class
callenculator = Callenculator()
