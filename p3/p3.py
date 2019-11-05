from datetime import datetime

_current_prime_list = []
_current_factors = {}

def _is_prime(n):
    for i in _current_prime_list:
        if n % i == 0:
            return False
    return True


def _next_prime():
    number = 2
    while True:
        if number == 2:
            _current_prime_list.append(number)
            yield number
            number += 1
        elif _is_prime(number):
            _current_prime_list.append(number)
            yield number
            number += 2
        else:
            number += 2


def _compare_with_multiply_all_factors(n):
    product = 1
    for k in _current_factors.keys():
        product *= k**_current_factors[k]
    if product == n:
        return True
    else:
        return False


def _calculate_exponent_of_factor(n, p):
    exponent = 0
    while n%p == 0:
        exponent += 1
        n = n //p
    return exponent


def _largest_prime_factor(n):
    factor = 1
    for p in _next_prime():
        if _compare_with_multiply_all_factors(n):
            break
        if n % p == 0:
            _current_factors[p] = _calculate_exponent_of_factor(n, p)
            print("Found a prime factor ", p, " with exponent ", _current_factors[p], " at ", datetime.now().time())
            if factor < p:
                factor = p
    return factor


def _largest_prime_factor_recursive(n):
    """
    This is not working because we are generating prime numbers while checking which one
    is a factor for the number. For a number that's a lot larger than the last prime found
    _is_prime() won't be able to tell whether the number is a prime accurately.
    """
    for p in _next_prime():
        if p * _current_prime_list[len(_current_prime_list) - 1] > n:
            break
        if n % p == 0:
            print("Found a prime factor ", p, " at ", datetime.now().time())
            factor = p
            reduced = n // p
            while reduced % p == 0:
                reduced = n // p
            if _is_prime(reduced):
                next_factor = reduced
            else:
                next_factor = _largest_prime_factor_recursive(reduced)
            if next_factor > factor:
                factor = next_factor
    return factor


print("Start time: ", datetime.now().time())
print("Largest prime factor of ", 600_851_475_143, " is ", _largest_prime_factor(600_851_475_143))
print("Finish time: ", datetime.now().time())

'''
The following result is achieved by checking the product of the found factors.
Start time:  11:24:18.951599
Found a prime factor  71  with exponent  1  at  11:24:18.951682
Found a prime factor  839  with exponent  1  at  11:24:18.952555
Found a prime factor  1471  with exponent  1  at  11:24:18.953818
Found a prime factor  6857  with exponent  1  at  11:24:18.978916
Largest prime factor of  600851475143  is  6857
Finish time:  11:24:18.979022
'''

'''
Start time:  17:11:37.413930
Found a prime factor  71  at  17:11:37.414007
Found a prime factor  839  at  17:11:37.414814
Found a prime factor  1471  at  17:11:37.415991
Found a prime factor  6857  at  17:11:37.441477
Largest prime factor of  600851475143  is  6857
Finish time:  17:13:18.080966
'''