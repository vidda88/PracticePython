def draw_grid(width, height):
    for x in range(height):
        print(" ---" * width)
        print("|   " * width,end="")
        print("|")
    print(" ---" * width)

w = int(input("Please enter width: "))
h = int(input("Please enter height: "))
draw_grid(w, h)
