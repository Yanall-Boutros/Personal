d = dict()
def calcchange(n):
   a = n[0] + 2*n[1] + 5*n[2] + 10*n[3] + 20*n[4] + 50*n[5] + 100*n[6] + 200*n[7]
   if (a == 200):
      hush = str()
      for num in n:
         hush += str(num)
      d[hush] = 0
   return a
count = 0
n = [0, 0, 0, 0, 0, 0, 0, 0]
for p100 in range (3):
   for p50 in range (5):
      for p20 in range (11):
         for p10 in range (21):
            for p5 in range (41):
               for p2 in range (101):
                  for p1 in range (201):
                     n[0] = p1
                     if calcchange(n) == 200: count += 1
                     elif calcchange(n) > 200: break
                  n[1] = p2
               n[2] = p5
            n[3] = p10
         n[4] = p20
      n[5] = p50
   n[6] = p100
print(len(d)+1)
