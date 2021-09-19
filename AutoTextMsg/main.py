import os
import time

def get_words(file_path):
    with open(file_path, 'r') as f:
        text = f.readlines()[0]
        words = text.split()
    return words

def send_message(phone_number, message):
    os.system('osascript send.script {} "{}"'.format(phone_number, message))

if __name__ == '__main__':
    words = get_words('bee.txt')
    for word in words:
        send_message("8329418522", word)
        time.sleep(2)

# Raeleens number "0276454604"
# Emma T number "0224801767"
# PJ's number "0224371458"
# Kyra's number "0223133622"
# zyra's number ""
