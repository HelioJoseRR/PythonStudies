def show_messages(message_list):
    while message_list:
        print(message_list.pop())

msg = ['Hello amigo', 'How are you?', 'I am fine']

show_messages(msg)