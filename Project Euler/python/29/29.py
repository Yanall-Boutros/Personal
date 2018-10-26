# the cardinality of the set of a^b where a and b range from
# n_1 <= a v b <= n_2 the domain is equal n_2 - n_1 + 1
# if n_2 = 100 and n_1 = 2, domain = 99
# the cardinality is therefore equal to domain^2 - # of a^b = b^a
import math
def logfrac(n):
   return float(n)/math.log(float(n))
cardinality = 0

count = 0
a = list()
b = list()
for i in range(2, 101):
   a.append(i)
   b.append(i)

collision = dict()
cardinality = 9801
tups = list()
for alpha in a:
   for beta in b:
      if collision.get(str(alpha**beta)) is None:
         collision[str(alpha**beta)] = 0
      else:
         collision[str(alpha**beta)] += 1
         tups.append((alpha, beta))

print (len(collision))
print (cardinality)
print (cardinality - len(collision))

print(sorted(collision.items()))
print (tups)
