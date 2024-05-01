prompt = 'If you could visit one place in the world, where would you go? '
stop_message = 'Would you like to let another person take the poll? (Y/N)'

responses = {}

poll_active = True

while poll_active:
    name = input("Write your name: ")
    response = input(prompt)

    responses[name] = response 

    stop = input(stop_message)

    if stop.lower() == 'n':
        poll_active = False

for name, response in responses.items():
    print(f"{name.title()} response is: {response.title()}")

