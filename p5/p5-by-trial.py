def _divisible_by_all_numbers_below(n, test):
    for num in range(1, n+1):
        if test % num != 0: return False
    return True


found = False
for t in range(2520, 999_999_999):
    if _divisible_by_all_numbers_below(20, t):
        print("Smallest number divisible by numbers from 1 to 20 is", t)
        found = True
        break
print("The number has been found:", found)
# Not finding any number by upper limit of 999_999
# Smallest number divisible by numbers from 1 to 20 is  232_792_560