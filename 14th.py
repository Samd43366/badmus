list = [11, 45,8, 11, 23, 45, 23, 45, 89]

count_dict = {}

for item in list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

print(count_dict)