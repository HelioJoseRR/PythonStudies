from pathlib import Path

cats_path = Path('cats.txt')
dogs_path = Path('dogs.txt')

try:
    cats = cats_path.read_text(encoding='utf-8')
except FileNotFoundError:
    cats = ''
    pass

try:
    dogs = dogs_path.read_text(encoding='utf-8')
except FileNotFoundError:
    dogs = ''
    pass

if cats:
    print("Cats: ")
    for cat in cats.splitlines():
        print(f"- {cat.title()}")

if dogs:
    print("\nDogs: ")
    for dog in dogs.splitlines():
        print(f"- {dog.title()}")