# Define the first list of numbers
list1 = [10, 20, 25, 30, 35]

# Define the second list of numbers
list2 = [40, 45, 60, 75, 90]

# Create a new list containing:
# - Odd numbers from list1
# - Even numbers from list2
list3 = [num for num in list1 if num % 2 != 0] + [num for num in list2 if num % 2 == 0]

# Print the newly created list
print(f"New list: {list3}")