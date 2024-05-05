from pathlib import Path

cats_path = Path('cats.txt')
dogs_path = Path('dogs.txt')

try:
    cats = cats_path.read_text(encoding='utf-8')
except FileNotFoundError:
    print('The file cats.txt does not exist.')

try:
    dogs = dogs_path.read_text(encoding='utf-8')
except FileNotFoundError:
    print('The file dogs.txt does not exist.')

print("Cats: ")
for cat in cats.splitlines():
    print(f"- {cat.title()}")

print("\nDogs: ")
for dog in dogs.splitlines():
    print(f"- {dog.title()}")