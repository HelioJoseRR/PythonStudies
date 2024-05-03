def show_messages(message_list):
    while message_list:
        print(message_list.pop())

def send_messages(message_list, sent_messages):
    while message_list:
        current_message = message_list.pop()
        print(current_message)
        sent_messages.append(current_message)

msg = ['Hello amigo', 'How are you?', 'I am fine']
sent = []

send_messages(msg, sent)

show_messages(sent)
show_messages(msg)