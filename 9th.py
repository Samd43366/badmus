# Outer loop to iterate through numbers 1 to 10 (rows of the multiplication table)
for i in range(1, 11):  # Loop for each row (1 to 10)
    # Inner loop to iterate through numbers 1 to 10 (columns of the multiplication table)
    for j in range(1, 11):  
        # Print the product of the current row and column numbers
        print(f"{i * j}", end="\t")  # Use tab spacing for better formatting
    # Print a new line after each row
    print()
