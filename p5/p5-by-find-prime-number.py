smallest_from_1_to_10 = 2520
prime_with_power_from_1_to_20 = {2: 4, 3: 2, 5: 1, 7: 1, 11: 1, 13: 1, 17: 1, 19: 1}

smallest_number = 1
for (k, v) in prime_with_power_from_1_to_20.items():
    smallest_number = smallest_number * k ** v

print("smallest number is", smallest_number)
# smallest number is 232792560