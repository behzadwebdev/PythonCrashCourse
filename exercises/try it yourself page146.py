################# 8-9
#def show_messages(message_list):
#    for message in message_list:
#        print(message)
#show_messages(messages)
############## 8-10
def send_message(message_list, sent_messages):
    while message_list:
        current_message = message_list.pop(0)
        print(current_message)
        sent_messages.append(current_message)
messages = ['hi', 'how are you?' , 'thank\'s']
send_messages = []
send_message(messages, send_messages)

print("\nmain message list(message):", messages)
print("send message list(send_message):", send_messages)
################## 8-11
print("----------------------------------------------------------------------------------------------------")
def send_message(message_list, sent_messages):
    while message_list:
        current_message = message_list.pop(0)
        print(current_message)
        sent_messages.append(current_message)
messages = ['hi', 'how are you?' , 'thank\'s']
send_messages = []
send_message(messages[:], send_messages)

print("\nmain message list(message):", messages)
print("send message list(send_message):", send_messages)
