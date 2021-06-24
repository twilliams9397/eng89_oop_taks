# This is the code for the OOP tasks

### Age Permission Task
```python
class Age_Permissions():

    def __init__(self):
        self.age = int(input("How old are you?  "))
        self.drivers_license = input("Do you have a drivers license? Y/N  ").capitalize()
        if self.drivers_license == "Y":
            self.drivers_license == True

    def vote_and_drive(self):
        if self.age > 21 and self.drivers_license == True:
            return "You can both vote and drive!"
        else:
            return "You cannot both vote and drive!"

    def vote(self):
        if self.age > 21:
            return "You are old enough to vote!"
        else:
            return "You are not old enough to vote!"

    def drink(self):
        if self.age >= 16:
            return "You are old enough to drink!"
        else:
            return "You aren't legally old enough to drink but your friends older than 16 might help!"

    def school(self):
        return "You are too young, go back to school!"

user = Age_Permissions()
if user.age >=16:
    while True:
        check = str(input("What permission would you like to check?\n 1 for vote and drive\n 2 for vote\n 3 for "
                          "drink\n Type 'Exit' at anytime to leave.\n"))
        if check == "1":
            print(user.vote_and_drive())
        elif check == "2":
            print(user.vote())
        elif check == "3":
            print(user.drink())
        elif check.capitalize() == "Exit":
            break
else:
    print(user.school())
```
### First Calculator Task
```python
class CalcFunctions:
    def add(self):
        self.x = int(input("What is the first number you would like to add in digits?  "))
        self.y = int(input("What is the second number you would like to add in digits?  "))
        return self.x + self.y

    def subtract(self):
        self.x = int(input("What number would you like to subtract from what in digits? Press enter after each number  "))
        self.y = int(input())
        return self.x - self.y

    def multiply(self):
        self.x = int(input("What is the first number you would like to multiply in digits?  "))
        self.y = int(input("What is the second number you would like to multiply in digits?  "))
        return self.x * self.y

    def divide(self):
        self.x = int(input("What number would you like to divide by what in digits? Press enter after each number  "))
        self.y = int(input())
        return self.x / self.y

calc_functions = CalcFunctions()

while True:
    func = str(input("What function would you like? Add, Subtract, Multiply or Divide?\n Type "
                     "'Exit' to finish.\n")).capitalize()
    if func == "Add":
        print(calc_functions.add())
    elif func == "Subtract":
        print(calc_functions.subtract())
    elif func == "Multiply":
        print(calc_functions.multiply())
    elif func == "Divide":
        print(calc_functions.divide())
    elif func == "Exit":
        break
    else:
        print("Unrecognised input, please try again")
```
### Second Calculator Task
```python
from calc_functions import CalcFunctions
from math import pi


class FunctionalCalc(CalcFunctions):
    def __init__(self):
        super().__init__()

    def circle_area(self):
        self.r = int(input("What is the radius of your circle in digits?  "))
        return pi * self.r ** 2

    def square_area(self):
        self.x = int(input("What is the side length of your square in digits?  "))
        return self.x ** 2

    def rectangle_area(self):
        self.x = int(input("What is the first side length of your rectangle in digits?  "))
        self.y = int(input("What is the second side length of your rectangle in digits?  "))
        return self.x * self.y

functional_calc = FunctionalCalc()

while True:
    func2 = str(input("Would you like the extra functions?\n1 for circle area\n2 for square area"
                      "\n3 for rectangle area\n type 'Exit' to finish\n"))
    if func2 == "1":
        print(functional_calc.circle_area())
    elif func2 == "2":
        print(functional_calc.square_area())
    elif func2 == "3":
        print(functional_calc.rectangle_area())
    elif func2.capitalize() == "Exit":
        break
    else:
        print("Unrecognised input, please try again")
```