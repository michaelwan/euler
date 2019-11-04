from datetime import datetime

_current_prime_list = []


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


def _largest_prime_factor(n):
    for p in _next_prime():
        if p * _current_prime_list[len(_current_prime_list) - 1] > n:
            break
        if n % p == 0:
            print("Found a prime factor ", p, " at ", datetime.now().time())
            factor = p
    return factor


def _largest_prime_factor_recursive(n):
    """Not working yet"""
    for p in _next_prime():
        if p * _current_prime_list[len(_current_prime_list) - 1] > n:
            break
        if n % p == 0:
            print("Found a prime factor ", p, " at ", datetime.now().time())
            factor = p
            reduced = n / p
            while reduced % p == 0:
                reduced = n / p
            next_factor = _largest_prime_factor(reduced)
            if(next_factor) > factor:
                factor = next_factor
    return factor


print("Start time: ", datetime.now().time())
print("Largest prime factor of ", 600_851_475_143, " is ", _largest_prime_factor(600_851_475_143))
print("Finish time: ", datetime.now().time())


'''
Start time:  17:11:37.413930
Found a prime factor  71  at  17:11:37.414007
Found a prime factor  839  at  17:11:37.414814
Found a prime factor  1471  at  17:11:37.415991
Found a prime factor  6857  at  17:11:37.441477
Largest prime factor of  600851475143  is  6857
Finish time:  17:13:18.080966
'''