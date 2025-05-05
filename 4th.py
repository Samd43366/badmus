number = (input("Enter a number: "))
try:
    num = int(number)
    if num % 5 == 0:
        print(f"{number} is divisible by 5")
    else:
        print(f"{number} is not divisible by 5")
except ValueError:
     print("Please enter a valid integer.")