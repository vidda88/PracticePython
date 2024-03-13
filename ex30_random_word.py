import random

with open("sowpods.txt") as open_file:
    word_list = open_file.readlines()

print(random.choice(word_list))