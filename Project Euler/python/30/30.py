# define an unordered mapping containng an int to int to ^ 5
d = dict()
for i in range(10):
   d[str(i)] = i**5

def sumdigs(n):
   total = 0
   for char in str(n):
      total += d[char]
   if n == total: return True
   return False

yessum = list()
num = 100
while(True):
   if sumdigs(num): yessum.append(num)
   num += 1
   print(yessum)
   print(sum(yessum))
