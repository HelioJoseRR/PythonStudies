class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now.")


restaurant = Restaurant("Helio's Place", "Italian")

print(f"{restaurant.restaurant_name.title()}")
print(f"{restaurant.cuisine_type.title()}")

restaurant.describe_restaurant()
restaurant.open_restaurant()