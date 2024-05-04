from pathlib import Path
import json

number = int(input("Enter a number: "))

path = Path('favorite_number.json')
content = json.dumps(number)
path.write_text(content)

print("Your favorite number has been saved!")