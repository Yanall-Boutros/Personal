import numpy as np
import matplotlib.pyplot as plt

def W(n, xdata, ydata, yerror):
    w_of_n = 0
    for x,y,s in zip(xdata, ydata, yerror):
        w_of_n += (((x**n)*y)/(s**2))
    return w_of_n

def U(n, xdata, yerror):
    u_of_n = 0;
    for x,y in zip(xdata, yerror):
        u_of_n += ((x**n) / (y**2))

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
    
x = np.array([0., 1., 2., 3., 4., 5.])
y = np.array([-8.0, -12.8, -17.7, -23.3, -27.6, -31.7])
yerr = np.array([0.2, -0.5, -0.9, -1.6, -2.0, -2.5])

results = linfit(x, y, yerr)

print("Results\n"+(72*"-"))
print("slope = %.3f +/- %.3f"%(results[0], results[2]))
print("intercept = %.3f +/- %.3f"%(results[1], results[3]))

plt.errorbar(x, y, yerr=results[3] , marker='o', markersize=3, color="red")
plt.savefig("out1.pdf")
x_bestfit = [0., 1., 2., 3., 4., 5., 6., 7., 8]
y_bestfit = results[0]*x + results[1]

matplotlib.plt(x_bestfit, y_bestfit)

plt.savefig("LineOfBestFit.pdf")
