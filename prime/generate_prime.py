_current_prime_list = []


def _is_prime(n):
    for i in _current_prime_list:
        if n % i == 0:
            return False
    return True


def next_prime():
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
