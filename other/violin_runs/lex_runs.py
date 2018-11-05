import numpy
def rtn_binary_list(n):
   B = []
   for i in range(2**n):
      number = str((format(i, 'b')))
      while(len(number) < n):  # a 4 digit number still needs 4 zeros
         number = '0' + number
      n_as_array_of_digs = []
      for char in number:
         n_as_array_of_digs.append(int(char))
      n_as_array_of_digs.reverse()
      B.append(n_as_array_of_digs)
   return B

def b_it_to_elem_swap(four_vec):
   elems = []
   elem = len(four_vec)
   for bin_num in four_vec:
      elem -= 1
      if bin_num == 1: elems.append(elem)
      else: elems.append(None)
   return elems

def index_to_hash(array):
   r = ""
   for elem in array:
      if type(elem) == type(list()):
         r += "BC"
      else:
         r += str(elem)
   return r
def print_rhythms(N):
   # N is the array of arrays of measures, where a measure could
   # possibly contain a sub N (i.e base case variable BC)
   output = ""
   i = 0
   for list_permute in N:
      for measure in list_permute:
         output += "\n"
         for beat in measure:
            if type(beat) == type(list()):
               output += " BC "
            else:
               output += " " + str(beat) + " "
         output += "\n"
      output += "\n" + 72*"=" + "\n"
      output += str(i) + "\n"
      output += 72*"=" + "\n"
      i += 1
   print(output)
# The 0th Array is the lexicographic set of binary based numbers of
# n digits in lexicographic order
n = int(input("Enter the number of beats per measure: "))
BC = rtn_binary_list(n)
Lex_Iter = rtn_binary_list(n)
N = []
N.append(BC) #N[0] = BC
# The 1st Array is the Previous array but every column selection in
# lexicographic order is replaced with an empty list. i.e
# [0, 0, 0, 0] -> [0, 0, 0, BC]
# [0, 0, 0, 1] -> [0, 0, 0, BC]
# [0, 0, 1, 0] -> [0, 0, 1, BC]
# [0, 0, 1, 1] -> [0, 0, 1, BC]
for b_it in Lex_Iter[1:]:
   N_1 = rtn_binary_list(n)
   swap_vals = b_it_to_elem_swap(b_it)
   for swap_val in swap_vals:
      for measure_it in range(len(N_1)):
         if swap_val is None:
            continue
         elif type(swap_val) == type(int()):
            N_1[measure_it][swap_val] = rtn_binary_list(n)
   N.append(N_1)
   
# The nth array is the nth-1st array but digits with a 1 in base_2(n)
# correspond to which columns get replaced with BC Lists
# n = 5 -> base2_5 -> 0101
# [0, 0, 0, 0] -> [0, BC, 0, BC]
# [0, 0, 0, 1] -> [0, BC, 0, BC]
# [0, 0, 1, 0] -> [0, BC, 1, BC]
# [0, 0, 1, 1] -> [0, BC, 1, BC]
# There are 2**n elements in each array, and 2**n arrays storing all
# the possible combinations


# now remove all duplicate entries
for lex_it in range(1, len(N[1:])+1):
   measure_it = 0
   dups = dict()
   del(dups)
   dups = dict()
   while measure_it < (len(N[lex_it])):
      if dups.get(index_to_hash(N[lex_it][measure_it])) is None:
         dups[index_to_hash(N[lex_it][measure_it])] = 0
      else:
         N[lex_it].pop(measure_it)
         measure_it -= 1 
      measure_it += 1
# Finally, have the BC array serve as an array back to N, satisfying
# the recursive memory management aspect
add_depth = N
# replace every BC in N with N
for lex_it in range(1, len(N[1:])+1):
   for measure_it in range(len(N[lex_it])):
      for beat_it in range(len(N[lex_it][measure_it])):
         if type(N[lex_it][measure_it][beat_it]) == type(list()):
            N[lex_it][measure_it][beat_it] = add_depth

# N is an infinite array, N[i] contains the lexicographic permutation
# from base case, and is of cardinality 2^n. N[i][j] contains the measure
# and is constant of cardinality n. N[i][j][k] is either a 0 (no beat),
# a 1 (yes beat), or is or some subdivision based on one of the 
# permutations of N.

# In general, b_it_to_elem_swap(base_2(i+1))) gives the indices of
# k for which subdivision occurs.

# N[i][j][k] == N[i][j][k][i'][j'][k'] == 
# N[i][j][k][i'][j'][k'][i''][j''][k'']
# let max(num(primes)) following any index be m. The measure j therefore
# has at worst one beat which subdivides n^m times
