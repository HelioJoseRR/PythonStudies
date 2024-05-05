class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now.")

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    
    def display_flavors(self):
        print(f"These are the flavors: ")
        for flavor in self.flavors:
            print(f"- {flavor}.")

ice_cream_stand = IceCreamStand('helio', 'italian', ['cream', 'vanilla', 'chocolate'])

ice_cream_stand.display_flavors()
