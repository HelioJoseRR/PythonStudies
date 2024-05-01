sandwich_orders = ['carne', 'queijo', 'misto']

finished_sandwiches = []

while sandwich_orders:
    finished = sandwich_orders.pop()

    print(f"I made your {finished.title()} sandwich!")

    finished_sandwiches.append(finished)

for i in finished_sandwiches:
    print(i)