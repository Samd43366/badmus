roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

valid_rolls = sample_dict.values()

filtered_rolls = [roll for roll in roll_number if roll not in valid_rolls]
print("Filtered roll numbers:", filtered_rolls)