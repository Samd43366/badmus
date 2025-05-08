#function to calculate product and sum of two numbers
def product_or_sum(a, b):
    product = a * b # Calculate product of a and b
    sum_result = a + b # Calculate sum of  a and b
    #Check if product is less than or equal to 1000
    #If product is less than or equal to 1000, return product
    if product <= 1000:
        return product 
    else:
        #Otherwise, return sum of a and b
        return sum_result
    
    # Take input for the first number and second number from the user 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# call the funtion and print the result 
result = product_or_sum(a, b)
print("Result:", result)