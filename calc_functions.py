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
