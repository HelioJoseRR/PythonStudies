def make_shirt(size, message):
    print(f"Size is {size} and message is {message}!")

"""Positional"""

make_shirt("Large", "Hello, World")
make_shirt(18, "Hello, World")

"""Keyword"""

make_shirt(message='Hello, World', size='Large')