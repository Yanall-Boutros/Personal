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
   return output
# The 0th Array is the lexicographic set of binary based numbers of
# n digits in lexicographic order
n = 4
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

# Finally, repeat this process for each array until reaching an
# an arbitrary depth (replace BC in each sub array with this function

add_depth = N
# replace every BC in N with N
for lex_it in range(1, len(N[1:])+1):
   for measure_it in range(len(N[lex_it])):
      for beat_it in range(len(N[lex_it][measure_it])):
         if type(N[lex_it][measure_it][beat_it]) == type(list()):
            N[lex_it][measure_it][beat_it] = add_depth
