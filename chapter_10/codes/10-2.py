from pathlib import Path 

path = Path('text_10_1.txt')
contents = path.read_text()

lines = contents.splitlines()

for line in lines:
    print(line.replace('Python', 'C'))