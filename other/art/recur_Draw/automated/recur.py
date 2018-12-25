import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
# -----------------------------------------------------------------------
# function definitions
# -----------------------------------------------------------------------
# f1 is chosen 1 percent of the time
def f1(x, y, a, b):
   return (a, b*y)
# f2 is chosen 85% of the time
def f2(x_n, y_n, a, b, c, d, e):
   return ((a*x_n + b*y_n), (c*x_n + d*y_n + e))
# f3 is chosen 7% of the time
def f3(x, y, a, b, c, d, e):
   return ((a*x + b*y), (c*x + d*y + e))
# f4 is chosen 7% of the time
def f4(x, y, a, b, c, d, e):
   return ((a*x + b*y), (c*x + d*y + e))
# Generalize variables which alter functions (plus/minus valus,
# multiplier factor, in how many functions, probability of calling a
# function, swapping x with y
# Linear transformation functions
# -----------------------------------------------------------------------
# define linear transformation parameters
# -----------------------------------------------------------------------
prob_f2 = 0.14
prob_f3 = 0.93
prob_f4 = 1 - prob_f3
prob_f1 = 0.99
x_col = 0
y_col = 1
f1_cx1 = 0
f1_cy1 = 0.16
f2_cx1 = 0.85
f2_cx2 = 0.04
f2_cy1 = -0.04
f2_cy2 = 0.85
f2_y2a = 1.6
f3_cx1 = 0.2
f3_cx2 = -0.26
f3_cy1 = 0.23
f3_cy2 = 0.22
f3_y2a = 1.6
f4_cx1 = -0.15
f4_cx2 = 0.28
f4_cy1 = 0.26
f4_cy2 = 0.24
f4_y2a = 0.44
sign_change = [1, -1] # 1 means yes, sign_change[1] multiplies num by -1
multiplier = [1]
for i in range(2):
   for j in range(2, 11):
      multiplier.append(j**sign_change[i])
# -----------------------------------------------------------------------
# define order to iterate values
# -----------------------------------------------------------------------
# guess changing which values first have the least overall effect.
# iterate through a lexicographic ordering of which change in values
# is currently enabled
graph_num = 0
# start with linear factors being multiplied by elems in mulitplier
# at digit 0, which ranges from length of multiplier
# at digit 1, apply a sign change.
# at digit 2, apply digit 0s operation but on probability factors instead
# at digit 3, trinary digit corresponds to value of x and y (convert to
#             binary and assign digit to column
# end with iterating through possible column value inputs
for x_c, y_c in [(0, 1), (1, 0), (0, 0), (1, 1)]:
   # before, apply multipliers to probability possibilities
   for prob_factor in multiplier:
      # then apply sign change
      for posneg in sign_change:
         # first apply multiplication 
         for factor in multiplier:
            # run functions to generate graphs. Factor is initiall 1
            # so we start with barsley fern ideally
            # -----------------------------------------------------------
            # Produce Random Data
            # -----------------------------------------------------------
            np.random.seed(19680801)
            prob_data = np.random.rand(10000)
            coors = list()
            # Base Case, x_0 = 0, y_0 = 0
            coors.append((0, 0))
            i = 0
            factor *= posneg
            for rand_number in prob_data:
               if rand_number > (prob_f1 * prob_factor):
                  coors.append(f1(coors[i][x_c],
                                  coors[i][y_c],
                                  factor*f1_cx1, factor * f1_cy1)
                              )
                  i += 1
               if rand_number > (prob_f2 * prob_factor):
                  coors.append(f3(coors[i][x_c],
                                  coors[i][y_c],
                                  factor * f2_cx1, factor * f2_cx2,
                                  factor * f2_cy1, factor * f2_cy2,
                                  factor * f2_y2a)
                              )
                  i += 1
               if rand_number > (prob_f3 * prob_factor):
                  coors.append(f2(coors[i][x_c],
                                  coors[i][y_c],
                                  factor * f3_cx1, factor * f3_cx2,
                                  factor * f3_cy1, factor * f3_cy2,
                                  factor * f3_y2a)
                              )
                  i += 1
               if rand_number < (prob_f4 * prob_factor):
                  coors.append(f4(coors[i][x_c],
                                  coors[i][y_c],
                                  factor * f4_cx1, factor * f4_cx2,
                                  factor * f4_cy1, factor * f4_cy2,
                                  factor * f4_y2a)
                              )
                  i += 1
            x_data = list()
            y_data = list()
            for tup in coors:
               x_data.append(tup[0])
               y_data.append(tup[1])
            x_data = np.array(x_data)
            y_data = np.array(y_data)
            plt.plot(x_data, y_data, marker=".",
                     markersize=1, linestyle="None")
            plt.axis('off')
            plt.savefig(str(graph_num)+".pdf")
            graph_num += 1
