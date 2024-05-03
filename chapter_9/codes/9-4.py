class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now.")

    def set_number_served(self, number_set):
        self.number_served = number_set

    def increment_number_served(self):
        self.number_served += 20

restaurant = Restaurant("helio's place", 'italian')

print(f"Served: {restaurant.number_served}")

restaurant.number_served = 12

print(f"Served: {restaurant.number_served}")

restaurant.set_number_served(13)

print(f"Served: {restaurant.number_served}")

restaurant.increment_number_served()

print(f"Served: {restaurant.number_served}")


