n = int(input("Enter a number: "))
previous_num = 0
for current_num in range(n):
    sum = previous_num + current_num
    print(f"{current_num:14} {previous_num:16} {sum}")
    previous_num = current_num