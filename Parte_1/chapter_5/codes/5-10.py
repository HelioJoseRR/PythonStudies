usernames = ['admin', 'helio', 'jose', 'karla', 'victor']

new_users = ['admin', 'helio', 'maria', 'davi', 'carlos']

for username in new_users:
    if username.lower() in usernames:
        print(f"Hello {username.title()}, you need to choose a new name.")
    else:
        print(f"Hello {username.title()}, this username is available.")