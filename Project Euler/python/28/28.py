#find sum of diags
def up_right(n):
   return (2*n + 1)**2

def up_left(n):
   return up_right(n) - 2*n

def down_left(n):
   return up_left(n) - 2*n

def down_right(n):
   return down_left(n) - 2*n

def sum_diag(n):
   return up_right(n) + up_left(n) + down_left(n) + down_right(n)
n = 1
total = 1
while (2*n + 1 <= 1001):
   total += sum_diag(n)
   n += 1

print (total)
