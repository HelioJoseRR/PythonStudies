from pathlib import Path

names = ''

while True:
    user_name = input('Enter your name: ')
    if user_name == 'q':
        break
    names += user_name + '\n'

path = Path('guest_book.txt')

path.write_text(names)