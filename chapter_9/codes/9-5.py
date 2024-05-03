class User:

    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} is {self.age} years old and is a {self.gender}!")

    def greet_user(self):
        print(f"Hello {self.first_name.title()}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

my_user = User('helio', 'jose', 22, 'male')

your_user = User('john', 'karl', 24, 'male')

my_user.describe_user()
my_user.greet_user()

your_user.describe_user()
your_user.greet_user()

my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.increment_login_attempts()

print(my_user.login_attempts)

my_user.reset_login_attempts()

print(my_user.login_attempts)