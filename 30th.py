def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("First Call:")
print_info(name="Alice", age=30, city="New York")

print("\nSecond Call:")
print_info(course="Python", level="Beginner", duration="6 weeks")
