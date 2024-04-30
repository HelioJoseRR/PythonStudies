cachorro = {
    'tipo': 'cachorro',
    'nome': 'rex',
    'dono': 'bob',
}

gato = {
    'tipo': 'gato',
    'nome': 'garfield',
    'dono': 'alice',
}

pets = [cachorro, gato]

for pet in pets:
    print(f"Pet's type: {pet['tipo']}")
    print(f"Pet's name: {pet['nome']}")
    print(f"Pet's owner: {pet['dono']}\n")