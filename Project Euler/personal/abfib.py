global_dict = dict()
def abfib(a, n):
   bc = range(a)
   if n < a:
      return bc[n]
   if global_dict.get((a,n)) is not None:
      return global_dict[(a,n)]
   else:
      total = 0
      for sub in range(1, a+1):
         total += abfib(a, n-sub)
      global_dict[(a, n)] = total
      return total
for j in range(2, 500):
   storage = list()
   print(72*"=")
   print("Abfib with ", j, "base cases")
   print(72*"=")
   for i in range(601):
      storage.append(abfib(j, i))
      print (storage[i])
   print (storage[-1]/storage[-2])
