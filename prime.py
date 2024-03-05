def check_prime(num):
    count = 0
    for x in range(1,num+1):
        if num % x == 0:
            count += 1
    return count

number = int(input("Enter your number: "))
if check_prime(number) > 2:
    print("Not prime.")
else:
    print("PRIME!")

