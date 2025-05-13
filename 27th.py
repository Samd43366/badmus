def outer_function(a, b):
    def inner_function():
        return a + b
    result = inner_function() + 5
    return result

output = outer_function(3, 4)
print(output)