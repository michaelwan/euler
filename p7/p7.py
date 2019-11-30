from prime.generate_prime import next_prime

n = 0
for p in next_prime():
    n = n + 1
    if n == 10001:
        print("10001 prime number is", p)
        break
