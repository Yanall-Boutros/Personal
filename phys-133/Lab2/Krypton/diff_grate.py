# Yanall Boutros
# yboutros
# Lab 2
# diff_grating.py
# Estimates the value of d for our diffraction grating given a set of
# # values of theta and lambda

# import statements
import numpy as np
# function definitions
def d(m, l, t):
   # m = order, l = lambda/wavelength, t = theta/angle
   # d = ml/sin(theta)
   return ((m*l)/np.sin(t))

# variable initalization and data
ccw_deg = np.array([40.5, 40.5, 42.5, 43])

ccw_arc = np.array([3, 22, 11, 20])

cw_deg = np.array([25.5, 25.5, 23.5, 23])

cw_arc = np.array([17, 3, 23 ,10])

deviation = 33 + 28/60

m = np.array([1, 1, 1, 1])

# saved as nm
colors = np.array([
                   467.35, 496.25, 565.64, 605.86
                 ])
ccw_angle = ccw_deg + (ccw_arc/60)
cw_angle = cw_deg + (cw_arc/60)

# fix for deviation
ccw_angle_fixed = np.absolute(ccw_angle - deviation)
cw_angle_fixed = np.absolute(cw_angle - deviation)

# convert to radians
ccw_angle_fixed = np.deg2rad(ccw_angle_fixed)
cw_angle_fixed = np.deg2rad(cw_angle_fixed)
theta_avg = (ccw_angle_fixed + cw_angle_fixed)/2
theta_diff = (ccw_angle_fixed - cw_angle_fixed)/2

# calculate an array of values for d
ccw_d = d(m, colors, ccw_angle_fixed)
cw_d = d(m, colors, cw_angle_fixed)
theta_d = d(m, colors, theta_avg)

# convert from spacing to slits
ccw_d = (ccw_d**-1)
cw_d = (cw_d**-1)
theta_d = (theta_d**-1)
ccw_d *= 1000000
cw_d *= 1000000
theta_d *= 1000000

print("Clock Wise angles = \n", cw_angle_fixed)
print("Counter clock wise angles = \n", ccw_angle_fixed)
print("Average angles = \n", theta_avg)
print("Average diff = \n", theta_diff)
print("cw_d = \n", cw_d)
print("ccw_d = \n", ccw_d)
print("theta_d = \n", theta_d)

ccw_d_avg = np.average(ccw_d)
cw_d_avg = np.average(cw_d)
theta_d_avg = np.average(theta_d)

ccw_d_std = np.std(ccw_d)
cw_d_std = np.std(cw_d)
theta_d_std = np.std(theta_d)
print("\nccw_d_avg = ", ccw_d_avg, " ccw_d_std = ", ccw_d_std)
print("\ncw_d_avg = ", cw_d_avg, " cw_d_std = ", cw_d_std)
print("\ntheta_d_avg = ", theta_d_avg, "theta_d_std = ", theta_d_std)
