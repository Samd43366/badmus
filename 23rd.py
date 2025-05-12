a = int(input("Enter a number: "))
b  = int(input("Enter another number: "))

def add_sub(a, b):
    return a + b, a - b
print("The sum is:", add_sub(a, b))

add_sub(a, b)