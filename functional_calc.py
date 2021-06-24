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
