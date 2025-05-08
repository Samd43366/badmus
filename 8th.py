# Define a function to generate a Fibonacci sequence
def sequeance():
    sequeance = []  # Initialize an empty list to store the sequence
    a, b = 0, 1  # Initialize the first two numbers of the Fibonacci sequence
    
    # Loop to generate the first 10 numbers of the Fibonacci sequence
    for i in range(10):
        sequeance.append(a)  # Append the current number to the sequence
        a, b = b, a + b  # Update 'a' and 'b' to the next two numbers in the sequence
    
    return sequeance  # Return the generated sequence

# Call the function and print the Fibonacci sequence
print(sequeance())