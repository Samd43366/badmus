# Take input from the user for a number
number = input("Enter a number: ")

try:
    # Convert the input to an integer
    num = int(number)
    
    # Check if the number is divisible by 5
    if num % 5 == 0:
        print(f"{number} is divisible by 5")
    else:
        print(f"{number} is not divisible by 5")
except ValueError:
    # Handle the case where the input is not a valid integer
    print("Please enter a valid integer.")