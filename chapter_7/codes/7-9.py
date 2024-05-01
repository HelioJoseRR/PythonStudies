sandwich_orders = ['pastrami' ,'carne', 'pastrami', 'queijo', 'misto', 'pastrami']

finished_sandwiches = []

message = "The deli has run out of pastrami!"

print(message)

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    finished = sandwich_orders.pop()

    print(f"I made your {finished.title()} sandwich!")

    finished_sandwiches.append(finished)

for i in finished_sandwiches:
    print(i)