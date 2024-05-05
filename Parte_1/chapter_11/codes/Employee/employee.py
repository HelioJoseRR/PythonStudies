class Employee:
    def __init__(self, first_name, last_name, anual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.anual_salary = anual_salary

    def give_raise(self, raise_amount=5000):
        self.anual_salary += raise_amount