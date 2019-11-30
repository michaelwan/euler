sum_to_100 = 0
sum_of_square_to_100 = 0
for i in range(1,101):
    sum_to_100 = sum_to_100 + i
    sum_of_square_to_100 = sum_of_square_to_100 + i**2

print("difference is", sum_to_100 ** 2 - sum_of_square_to_100)