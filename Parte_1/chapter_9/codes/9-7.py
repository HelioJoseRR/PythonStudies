class User:

    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} is {self.age} years old and is a {self.gender}!")

    def greet_user(self):
        print(f"Hello {self.first_name.title()}!")

class Admin(User):

    def __init__(self, first_name, last_name, age, gender, privileges):
        super().__init__(first_name, last_name, age, gender)
        self.privileges = privileges

    def show_privileges(self):
        print(f"Admin privileges: ")

        for privilege in self.privileges:
            print(f"- {privilege.title()}!")

admin = Admin('helio', 'jose', 22, 'male', ["Run in the wild", 'ban the trolls', 'clean the server'])

admin.show_privileges()
admin.describe_user()
