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

def chi_squared(ydata, y_bestfit, sigma):
    cs = np.sum(((ydata - y_bestfit)**2)/(sigma**2))
    csr = cs / (len(ydata)-1)
    return (cs, csr)

def W(n, xdata, ydata, yerror):
    w_of_n = np.sum(((xdata**n)*ydata)/(yerror**2))
    return w_of_n

def U(n, xdata, yerror):
    u_of_n = np.sum((xdata**n)/(yerror**2))
    return u_of_n
    

def linfit(xdata, ydata, yerror):
    # output an array of four values in the form (slope, intercept, sigma_slope, sigma_intercept)
    # U_n = \sum [x_i^n divided by \sig_i ^ 2]
    # W_n - \sum [y_i x_i^n divided by \sig_i^2]
    # D = U_0 * U_2 - U_1\^2
    U_0 = U(0, xdata, yerror)
    U_1 = U(1, xdata, yerror)
    U_2 = U(2, xdata, yerror)
    W_0 = W(0, xdata, ydata, yerror)
    W_1 = W(1, xdata, ydata, yerror)
    
    D = U_0*U_2 - (U_1**2)
    slope = ((U_0*W_1) - (U_1*W_0))/D
    intercept = (U_2*W_0 - U_1*W_1)/D
    sigma_slope = (U_0/D)**0.5 # sigma_slope might be squared
    sigma_intercept = (U_2/D)**0.5 # intercept might be squared
    
    return np.array([slope, intercept, sigma_slope, sigma_intercept])

# variable initalization and data
ccw_theta = np.array([
                      40, 40.5, 41, 41.5, 42.5, 44, 44.5, 48,
                      48.5, 49.5, 50, 53, 56
                    ])

ccw_arc = np.array([
                    26, 19, 10, 0, 17, 10, 22, 3, 26, 5, 0, 0, 2
                  ])

cw_theta = np.array([
                     25, 24.5, 24, 24, 22.5, 21, 20.5, 17, 16.5,
                     16, 15.5, 12.5, 9.5
                   ])

cw_arc = np.array([
                   4, 12 ,23, 3, 9, 24, 25, 22, 5, 0, 9, 1, 1
                 ])

m = np.array([
              1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2
            ])

colors = np.array([
                   447.148, 471.314, 492.193, 501.567, 587.592, 706.519,
                   706.571, 447.148, 471.314, 492.193, 501.567, 587.592,
                   706.519
                 ])
ccw_angle = ccw_theta + (ccw_arc/60)
cw_angle = cw_theta + (cw_arc/60)

# fix for deviation
deviation = 32.5 + 10/60
ccw_angle_fixed = np.absolute(ccw_theta - deviation)
cw_angle_fixed = np.absolute(cw_theta - deviation)

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

print("\n\n\n\n\n\n\n")
theta_avg_hi = theta_avg + (10/60)
theta_avg_lo = theta_avg - (10/60)
theta_d_hi = ((d(m, colors, theta_avg_hi)**-1)*1000000)
theta_d_lo = ((d(m, colors, theta_avg_lo)**-1)*1000000)
print(np.average(theta_d_hi))
print(np.average(theta_d_lo))

