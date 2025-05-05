def product_or_sum(a, b):
    product = a * b
    sum_result = a + b
    if product <= 1000:
        return product 
    else:
        return sum_result
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
result = product_or_sum(a, b)
print("Result:", result)