import numpy as np
def prime_num_dict(n):
    # generate a dictionary where each key i represents the ith number 
    # and its value is either 0 (not prime) or 1 (prime). i ranges to n
    prime_list = np.ones(n)
    prime_list[0] = 0
    for num in range(2,n):
        if prime_list[num] == 1: #if we have a prime
            i = 2 # every multiple of that prime is not prime
            while (num * i) < n:
                prime_list[num*i] = 0
                i += 1
    return prime_list
def next_permutation(n):
    # take the zeroth number, move it to the end
    return n[1:len(n)]+n[0]
def is_circular_prime(num, prime_list):
    for i in range(len(str(num))+1):
       if not prime_list[int(num)]:
           # the digit is not prime
           return False
       num = next_permutation(str(num))
    return True
primes = prime_num_dict(999999)
count = 0
for number in range(2, len(primes)):
    if primes[number]:
       if is_circular_prime(int(number), primes):
           print(number)
           count += 1
print(count)
