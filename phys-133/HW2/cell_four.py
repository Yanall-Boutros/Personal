# produce a list of every prime number from 0 and 100

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if (n % i == 0):
            return False
    return True
primes = list()

for i in range(1, 101):
    if (is_prime(i)):
        primes.append(i)

for num in primes:
    print(num)
