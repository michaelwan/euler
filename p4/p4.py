def _is_palindromic(n):
    length = len(str(n))
    digits = [0] * (length+1)
    remaining = n
    for i in reversed(range(1, length+1)):
        mod = 10 ** (i-1)
        digits[length - i] = remaining // mod
        remaining = remaining % mod
    for i in range(1,length+1):
        if digits[i-1] != digits[length - i]:
            return False
    return True


last = 1
factor_a, factor_b = 1,1
for a in reversed(range(100, 1000)):
    for b in reversed(range(100, 1000)):
        number = a * b
        if _is_palindromic(number):
            print("Found two numbers ", a, ", ", b, " that produced palindromic number ", number)
            found = True
            break
    if number > last:
        last = number
        factor_a = a
        factor_b = b
print("Largest palindromic found is ", last, " which is product of ", factor_a, factor_b)
