# Yanall Boutros
# yboutros
# Lab 2 - Helium.py
# Given a claculated value of D from the Helium segment of this lab, we
# # take measurements of theta for which wavelengths appear and use that
# # to calculate the actual wavelengths

# import statements
import numpy as np

def l(m, d, t):
   # m = order, d = diffraction grating constant, t = theta/angle
   # l = dsin(theta) / m
   print("m = ", m, "\nd = ", d, "\nt = ", t)
   return (d*np.sin(t))/m

def R(l, guess_n):
   inv_lambda = 1/l
   n_final = (1/2)**2
   n_initial = (1/guess_n)**2
   delta_n = n_final - n_initial
   return inv_lambda / delta_n

# variable initalization and data
ccw_deg = np.array([40.5, 41.5, 44.5])

ccw_arc = np.array([3, 4, 0])

cw_deg = np.array([26, 25, 22])

cw_arc = np.array([1, 2, 2])

m = np.array([1, 1, 1])

d = 1/((294)/1000000)

# add arc minutes
ccw_angle = ccw_deg + (ccw_arc/60)
cw_angle = cw_deg + (cw_arc/60)

# fix for deviation
deviation = 33 + (11/60)
ccw = ccw_angle - deviation
cw = deviation - cw_angle

# convert to radians
ccw_rad = np.deg2rad(ccw)
cw_rad = np.deg2rad(cw)

# get theta
theta = (cw_rad + ccw_rad)/2
theta_diff = (cw_rad - ccw_rad)/2

# calculate lambda
wavehi = l(m, d, theta + 5/60)
wavelo = l(m, d, theta - 5/60)
wavelengths = l(m, d, theta)
print("Theta = ", theta)
print("Theta diff = ", theta_diff)
print("Wavelengths = ", wavelengths)

# fix for nm
wavelengths /= 1000000000
expected = 10967758
for i in [3, 4, 5]:
   R_H = R(wavelengths, i)
   print (R_H)

# manually select values closest 
R_H[0] = 11068285.07570297
R_H[1] = 10905512.68933296
R_H[2] = 10866250.03551875

# print average
print ("R_H Avg = ", np.average(R_H))
print ("hi", wavehi)
print ("lo", wavelo)
