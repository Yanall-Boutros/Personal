import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
# Linear transformation functions
# f1 is chosen 1 percent of the time
def f1(x, y):
   return ((0, -0.16*y))
# f2 is chosen 85% of the time
def f2(x_n, y_n):
   return ((0.85*x_n + 0.04*y_n), (-0.04*x_n + 0.85*y_n + 1.6))
# f3 is chosen 7% of the time
def f3(x, y):
   return ((0.2*x - 0.26*y), (0.23*x+0.22*y+1.6))
# f4 is chosen 7% of the time
def f4(x, y):
   return ((-0.15*x + 0.28*y), (0.26*x + 0.24*y + 0.44))

coors = list()
# Base Case, x_0 = 0, y_0 = 0
coors.append((0, 0))
# Produce Random Data
np.random.seed(19680801)
prob_data = np.random.rand(10000)
i = 0
for rand_number in prob_data:
   if int(100*rand_number) > 14:
      coors.append(f2(coors[i][0], coors[i][1]))
      i += 1
   if int(100*rand_number) > 92:
      coors.append(f3(coors[i][0], coors[i][1]))
      i += 1
   if int(100*rand_number) < 7:
      coors.append(f4(coors[i][0], coors[i][1]))
      i += 1
   if int(100*rand_number) > 98:
      coors.append(f1(coors[i][0], coors[i][1]))
      i += 1
x_data = list()
y_data = list()
for tup in coors:
   x_data.append(tup[0])
   y_data.append(tup[1])
x_data = np.array(x_data)
y_data = np.array(y_data)
plt.plot(x_data, y_data, marker=".",markersize=1, linestyle="None")
plt.axis('off')
plt.savefig("Test.pdf")
