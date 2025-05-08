# Take input from the user for a number
num = (input("Enter a number: "))

# Check if the number is the same when reversed (palindrome check)
if num == num[::-1]:
    # If the condition is true, the number is a palindrome
    print(f"{num} is a palindrome")
else:
    # If the condition is false, the number is not a palindrome
    print(f"{num} is not a palindrome")