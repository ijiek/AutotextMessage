import os

def get_words(file_path):
    with open(file_path, 'r') as f:
        text = f.readlines()[0]
        words = text.split()
    return words

def send_message(phone_number, message):
    os.system('osascript send.scpt {} "{}"'.format(phone_number, message))

if _name_ == '__main__':
    words = get_words('test.txt')
    for word in words:
        send_message("0276454604", word)
