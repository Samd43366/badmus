first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

if first_set.issubset(second_set):
    print("First set is a subset of the second set")

elif first_set.issuperset(second_set):
    print("First set is a superset of the second set")

else:
    print("Neither set is a subset or superset of the other")