def get_largest():
    var = []
    largest = 0
    amount = int(input("How many numbers? "))
    for x in range(amount):
        var.append(int(input("Number: ")))
    for x in var:
        if x > largest:
            largest = x
    return largest

print(get_largest())