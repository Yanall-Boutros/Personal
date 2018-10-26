from collections import defaultdict
def is_pdgtl(n):
   # returns true if n is pandigital and false otherwise
   char_count = defaultdict(int)
   for c in n:
      if char_count[c] != 0:
         return False
      else: char_count[c] += 1
   return True
def gen_2facs(n):
   # n is a number, generate all factors
   for i in range(2, int((n)**0.5)):
      # The three numbers to consider are n, i, and n/i only if n/i is int
      if n % i == 0:
         all_digs = (str(n)+str(i)+str(n/i))
         if len(all_digs) == 9:
            if is_pdgtl(all_digs):
               return (i, int(n/i), n)
   return None
pandigits = list()
count = 0
for i in range(99999, 987654322):
   if is_pdgtl(str(i)):
      pandigits.append(gen_2facs(i))
