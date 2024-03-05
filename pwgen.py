import random
import requests

def get_list_of_words(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().splitlines()

def random_pw(str):
    password = ""
    if str == 'w':
        password = random.choice(words)
    if str == 'm':
        password = random.choice(words)
        password = password.replace(password[-1],password[-1].upper())
        password += random.choice(non_letters)
    if str == 's':
        password = random.choice(words)
        password = password.replace(password[-1], password[-1].upper())
        password = password.replace(password[2], password[2].upper())
        password += random.choice(non_letters)
        password += random.choice(non_letters)
    return password

words = get_list_of_words(r'C:\Users\david\PycharmProjects\HelloWorld\venv\wordlist.10000.txt')
non_letters = "0123456789!@#$%^&*()?"
strength = str(input("Would you like a (w)eak, (m)edium, or (s)trong password? ").lower())
print(random_pw(strength))