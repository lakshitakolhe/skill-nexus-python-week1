print("Even, Odd & Prime Number Checker")

num = int(input("Enter a number: "))

# Even or Odd
if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

# Prime Number Check
if num <= 1:
    print("The number is not Prime")
else:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("The number is Prime")
    else:
        print("The number is not Prime")