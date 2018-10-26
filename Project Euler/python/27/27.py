# generate a list of primes from 0 to 1000
def is_prime(n):
   if isinstance(n**0.5, complex): return False
   for i in range(2, int(n**0.5) + 1):
      if (n % i == 0):
         return False
   return True

def quad(a, b, n):
   return n**2 + a*n + b

# test is prime
b = list()
for i in range (2, 10000):
   if (is_prime(i)):
      b.append(i)
      b.append(-1*i)

a = list()
for i in range (1, 10000):
   a.append(i)
   a.append(-1*i)

n = 0
n_chain = (0,0,0) # [0] = a, [1] = b, [2] = n
# n^2 + an + b
# increment n, then a, then b
for prime in b:
   for num in a:
      n = 0
      while (is_prime(quad(num, prime, n))):
         n += 1
         if n > n_chain[2]:
            n_chain = (num, prime, n)
print (n_chain)
print (n_chain[0] * n_chain[1])
