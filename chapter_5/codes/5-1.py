"""
5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test.
"""

# Test 1

alien = 'predador'

print("Is alien == 'predador'? I predict True.")
print(alien == 'predador')

# Test 2

alien = 'predador'

print("\nIs alien == 'Predador'? I predict False.")
print(alien == 'Predador')

# Test 3

filmes = ['predador', 'alien', 'star wars']
filme_favorito = 'predador'

print("\nIs 'predador' in filmes? I predict True.")
print(filme_favorito in filmes)

# Test 4

filmes = ['predador', 'alien', 'star wars']
filme_favorito = 'Star Trek'

print("\nIs 'Star Trek' in filmes? I predict False.")
print(filme_favorito in filmes)

# Test 5

filmes = ['predador', 'alien', 'star wars']
filme_favorito = 'STAR WARS'

print("\nIs lower 'STAR WARS' in filmes? I predict True.")
print(filme_favorito.lower() in filmes)
