# Take input from the user for the range of numbers
n = int(input("Enter a number: "))

# Initialize the previous number to 0 
previous_num = 0

# Loop through numbers from 0 to n-1
for current_num in range(n):
    # Calculate the sum of the current number and the previous number 
    sum = previous_num + current_num

    # Print the current number, previous number, and their sum in a formatted way
    print(f"{current_num:14} {previous_num:16} {sum}")
    
    # Update the previous number to the current number for the next iteration
    previous_num = current_num