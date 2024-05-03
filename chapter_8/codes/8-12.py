def sandwich_toppings(*toppings):
    msg = "Your sandwich has the following toppings: "
    print(msg)

    for topping in toppings:
        print(f"- {topping}")


sandwich_toppings('cheese', 'tomato', 'lettuce')
sandwich_toppings('cheese', 'tomato', 'lettuce', 'onion')
sandwich_toppings('cheese', 'tomato', 'lettuce', 'onion', 'mayo')
sandwich_toppings('cheese', 'tomato', 'lettuce', 'onion', 'mayo', 'ketchup')