num = int(input("Enter any number: "))
if num > 1:
    for i in range(2, number):
        if (num % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
