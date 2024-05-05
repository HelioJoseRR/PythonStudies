jessica = {
    'first_name': 'jessica',
    'last_name': 'santos',
    'age': 24,   
}

carlos = {
    'first_name': 'carlos',
    'last_name': 'silva',
    'age': 25,
}

helio = {
    'first_name': 'helio',
    'last_name': 'jose',
    'age': 22,
}

people = [jessica, carlos, helio]

for person in people:
    print(person['first_name'])
    print(person['last_name'])
    print(f"person['age']\n")