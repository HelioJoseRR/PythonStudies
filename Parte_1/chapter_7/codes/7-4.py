prompt = "Enter the pizza toppings you want: "

while True:
    topping = input(prompt)

    if topping.lower() == 'quit':
        break
    else:
        print(f"Adding {topping.title()} to your pizza.")