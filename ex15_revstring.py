def split_string(str):
    newstr = str.split()
    revstr = newstr[-1::-1]
    print(" ".join(revstr))

string = str(input("Please enter a string with multiple words: "))
split_string(string)
