from pathlib import Path
import json

path = Path('favorite_number.json')

if path.exists():
    content = path.read_text(encoding='utf-8')
    number = json.loads(content)
    print(f"I know your favorite number! It's {number}.")
else:
    number = int(input("Enter a number: "))
    content = json.dumps(number)
    path.write_text(content)
    print("Your favorite number has been saved!")