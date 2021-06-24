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
