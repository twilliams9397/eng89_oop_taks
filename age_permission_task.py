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
        if self.age < 16:
            return "You are too young, go back to school!"
        else:
            return "You have left school!"

user = Age_Permissions()

print(user.vote_and_drive())
print(user.vote())
print(user.drink())
print(user.school())

