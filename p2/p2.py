def _next_fib_number(first, second):
    return first + second

def _even_number(n):
    return n%2 == 0

def _calculate_fibs(limit):
    fib_number = [1, 2]
    even_fib_number = [2]
    next = _next_fib_number(*fib_number[len(fib_number) - 2: len(fib_number)])
    while(next < limit):
        fib_number.append(next)
        if(_even_number(next)):
            even_fib_number.append(next)
        next = _next_fib_number(*fib_number[len(fib_number) - 2: len(fib_number)])
    return even_fib_number

def _sum(list):
    sum = 0
    for n in list:
        sum = sum + n
    return sum


print('Sum of all even fibonacci number below 4 million: ', _sum(_calculate_fibs(4_000_000)))


