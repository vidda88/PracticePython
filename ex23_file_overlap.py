with open('happynumbers.txt') as open_happy:
    happy = open_happy.read().split("\n")

with open('primenumbers.txt') as open_prime:
    prime = open_prime.read().split("\n")

print([x for x in happy if x in prime])



