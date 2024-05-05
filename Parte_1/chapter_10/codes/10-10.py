from pathlib import Path

path = Path('book.txt')

content = path.read_text(encoding='utf-8')

print(content.count('-'))