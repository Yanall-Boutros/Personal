# import statements
import numpy as np
import matplotlib.pyplot as plt
# function definitions
def chi_squared(ydata, y_bestfit, sigma):
    cs = np.sum(((ydata - y_bestfit)**2)/(sigma**2))
    csr = cs / 18
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

# initalize variables
current = np.array([0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00])
voltage = np.array([15.10, 30.70, 44.30, 58.00, 76.10, 86.00, 108.5, 120.0, 132.5, 152.0, 170.0, 174.0, 194.0, 215.0, 227.0, 231.0, 240.0, 245.0, 252.0, 255.0])
volt_err = np.array([1.00, 1.00, 1.00, 2.50, 2.50, 2.50, 2.50, 2.50, 5.00, 5.00, 5.00, 7.50, 7.50, 7.50, 7.50, 7.50, 10.00, 10.00, 10.00, 10.00])

# run linfit
results = linfit(current, voltage, volt_err)
print("Slope = "+ str(results[0]))
print("intercept = "+ str(results[1]))
print("sigma_slope = "+ str(results[2]))
print("sigma_intercept = "+ str(results[3]))
# create a plot containing the data points with y-error bars. current on x
# axis, voltage on y. Include a line of best fet, title and label with units
# and a legend

# create error bars
plt.errorbar(current, 
             voltage,
             yerr=volt_err,
             marker='.',
             color="red",
             LineStyle='none')
# plot line of best fit
volt_bestfit = results[1]+results[0]*current
plt.plot(current, volt_bestfit, '--')

# label axes, title, add legend
plt.xlabel("Current (A)")
plt.ylabel("Voltage (V)")
plt.title("Voltage vs Curent")
plt.legend(['Estimated Voltage (best fit)', 'Measured Voltage'])

plt.savefig("Boutros, Yanall - Voltage vs Current.pdf")

# determine chi squared
csAndcsr = chi_squared(voltage, volt_bestfit, volt_err)
print(csAndcsr)
