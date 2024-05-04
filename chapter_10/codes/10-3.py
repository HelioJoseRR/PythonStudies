from pathlib import Path 


path = Path('text_10_1.txt')

for line in path.read_text().splitlines():
    print(line.replace('Python', 'C'))