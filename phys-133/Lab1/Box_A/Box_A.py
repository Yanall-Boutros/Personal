# Yanall Boutros
# Phys-133
# Lab 1 - Box_A.py
# Creates a Graph relating the Phase and Magnitude of Impedence to the
# Frequency recorded, as well as error bars for those values
# Some code was gathered from David Smith, My Lab Partner for Box E
# Lena Eiger and I worked on compiling and debugging other areas of
# code
# July, 2018
# Import Statements
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import math as m
plt.style.use('classic')
import numpy.random as ran
import scipy.optimize as opt
import scipy.stats as stat

# Function Definitions
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

def dzdv1(R, V2):
   # The partial derivative of Z with respect to V1 
   # where Z = |V1|R/|V2|
   retn = R / V2
   return retn

def dzdv2(V1, R, V2):
   # Partial of Z with respect to V2
   retn = V1*R
   retn /= V2
   retn /= V2
   return retn

def dzdvr(V1, V2):
   # Partial of Z with respect to R
   retn = V1 / V2
   return retn

def sigz(R, V1, V2, sigV1, sigV2, sigR):
   # Uses the above function definitions to calculate the error range
   # for Z by using the derivative method
   retn = (dzdv1(R, V2)*sigV1)**2
   retn += (dzdv2(V1, R, V2)*sigV2)**2
   retn += (dzdvr(V1, V2)*sigR)**2
   return retn**0.5

def CapMag(freq, *cap_guess):
   # This function returns the magnitude over a range of frequencies
   # provided a guess for what the capacitance might be
   omega = m.pi*2*freq
   return 1/(omega*cap_guess)

def ImpMag(V1, V2, R):
   # ImpCapMag reads as Impedence Magnitude, it is the
   # theoretical equation for calculating the magnitude of impedence
   return ((V1 * R)/V2)

def LeastSquaresFit(xdata, ydata, y_sigma):
   # Least Squares Fit was originally a python program written by Prof.
   # David Smith, I have adapted and altered it to be generalized as an
   # individual function.
   cap_guess = 8.89e-9
   xsmooth = np.linspace(np.min(freq),np.max(freq), 1000)
   fsmooth = CapMag(xsmooth, cap_guess)
   plt.plot(xsmooth, fsmooth, color='red',
            label='Capacitance Guess', alpha=0.9)
   #popt, pcov = opt.curve_fit(CapMag, xdata, ydata, sigma=y_sigma,
   #                           p0=cap_guess, absolute_sigma=1)
   #fsmooth_next = CapMag(xsmooth, *popt)
   #plt.plot(xsmooth, fsmooth_next, color='cyan',
   #         label='Line of Best Fit', alpha=0.5)
   #plt.legend(loc=1)
   
   # Chi Squared Test for Best Fit Line
   print()
   print(72*'=')
   print('Scipy.Curve_Fit Best Fit Line Chi Squared Test')
   print(72*'-')
   Mag_Fit = CapMag(xdata, cap_guess)
   Chi_Squared = sum( (ydata - Mag_Fit)**2 / y_sigma**2)
   dof = len(ydata) - 2
   Reduced_Chi_Squared = Chi_Squared / float(dof)
   print("Chi-square = ", Chi_Squared)
   print("Degrees of Freedom = ", dof)
   print("Reduced Chi Square = ", Reduced_Chi_Squared)

   print("Probability of exceeding this chi_square = ",
          1.-stat.chi2.cdf(Chi_Squared,dof))
 
   print("Confidence can we reject this model = ",
        stat.chi2.cdf(Chi_Squared,dof))
   print(72*'=')

# Input Data / Initalize variables
freq = np.array([
                 40000, 36320, 33880, 31300, 29180, 26490, 23780, 20270,
                 18850, 15900, 13810, 11460, 8480, 503.5, 544.55, 603.7,
                 655, 708.8, 756.8, 815.8, 3968, 4969, 50440, 60420,
                 70630, 81250, 90900, 101590
                ])

phase = np.array([
                  101, 100, 101, 100, 99, 98.1, 97.5, 96.5, 96.3, 95.6,
                  96.5, 94.1, 93, 96.4, 96.9, 97, 98.6, 96.4, 97.5, 99,
                  103, 113, 89.5, 92.2, 94.6, 99.4, 101, 103
                ]) # conversion to radians

resist = np.array([
                   4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000,
                   4000, 4000, 4000, 4000, 4000, 40000, 40000, 40000,
                   40000, 40000, 40000, 40000, 40000, 700, 700, 700,
                   700, 700, 700
                 ])

volt1 = np.array([
                  0.312, 0.328, 0.352, 0.37, 0.4, 0.432, 0.48, 0.58,
                  0.6, 0.7, 0.78, 0.92, 1.12, 2, 1.92, 1.84, 1.76, 1.68,
                  1.6, 1.52, 0.44, 0.36, 0.024, 0.0208, 0.0192, 0.0176,
                  0.016, 0.0152
                ])

volt2 = np.array([
                  2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.08,
                  2.08, 2.08, 2, 1.92, 2, 2.16, 2.24, 2.32, 2.4, 2.4,
                  2.48, 2.88, 2.88, 0.04, 0.0432, 0.0448, 0.0456,
                  0.0464, 0.0472
                ])

freq_sigma = np.ones(28)*5
phase_sigma = np.ones(28)*3
resist_sigma = np.ones(28)*2
volt1_sigma = np.ones(28)*.4
volt2_sigma = np.ones(28)*.4
# Graph for Impedance
# Calculate Z and Z_sigma
Z = ImpMag(volt1, volt2, resist)
Z_sigma = sigz(resist, volt1, volt2, volt1_sigma,volt2_sigma, resist_sigma)

# Plot Raw Data with Error Bars
plt.errorbar(freq, Z, xerr=freq_sigma, yerr=Z_sigma, color='blue',
             marker='.', linestyle='None', label="Impedance",alpha=0.7)

plt.title("Magnitude of Impedance vs. Frequency")

plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude ($\Omega$)")

# Run Least Squares Fit to generate line of Best
plt.ylim(0, 50000)
LeastSquaresFit(freq, Z, Z_sigma)
plt.savefig("Impedance.pdf")
# Graph For Phase Difference
# Create New Figure
plt.figure()

# Plot Raw Data with Error Bars
plt.errorbar(
             freq, phase, xerr=freq_sigma, yerr=phase_sigma,
             color='blue', marker='.', linestyle='None',
             label='Phase Difference', alpha=0.6
            )

plt.title("Phase Difference vs Frequency")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase Difference (Degrees)")
# run linfit
results = linfit(freq, phase, phase_sigma)
print()
print(72*"=")
print("Function LinFit Results")
print(72*"-")
print("Slope = "+ str(results[0]))
print("intercept = "+ str(results[1]))
print("sigma_slope = "+ str(results[2]))
print("sigma_intercept = "+ str(results[3]))
print(72*'=')

# Create a linear regression line of best fit based on results
xsmooth = np.linspace(np.min(freq),np.max(freq)+20000, 1000)
terrible_fit_max = freq*(results[0]+results[2])
terrible_fit_max += (results[1]+results[3])

terrible_fit = freq*results[0] + results[1]

terrible_fit_min = freq*(results[0]-results[2])
terrible_fit_min += (results[1]-results[3])

plt.plot(freq, terrible_fit_max, '--', color='darkred',
         label="Max Line of Best Fit")
plt.plot(freq, terrible_fit, '--', color='blue',
         label="Line of Best Fit")
plt.plot(freq, terrible_fit_min, '--', color='indianred',
         label="Min Line of Best Fit")
plt.legend(loc=4)
plt.ylim(70, 120)
plt.savefig("PhaseDiff.pdf")

# Chi Squared Test and Analysis for linear regression equation
above = 0
above_spread = 0
below = 0
below_spread = 0
equalTo = 0
in_spread = 0
for deg, guess in zip(phase, terrible_fit):
   if (deg > guess):
      above += 1
   elif (deg < guess):
      below += 1
   else:
      equalTo += 1

for deg, high, low, in zip(phase, terrible_fit_max, terrible_fit_min):
   if (deg <= high and deg >= low):
      in_spread += 1
   elif (deg < low):
      below_spread += 1
   else:
      above_spread += 1

Chi_Tup = chi_squared(phase, terrible_fit, phase_sigma)
print()
print(72*'=')
print(
      "Chi Square Test and Analysis for Linear Regression",
      "Phase Difference"
     )
print(72*'-')
print("Number of Data Points above Line of Best Fit = ", above)
print("Number of Data Points below Line of Best Fit = ", below)
print("Number of Data Points on the Line of Best Fit = ", equalTo)
print(72*'-')
print("Number of Data Points above the Spread = ", above_spread)
print("Number of Data Points below the Spread = ", below_spread)
print("Number of Data Points within the Spread = ", in_spread)
print(72*'-')
print('Chi Squared = ', Chi_Tup[0])
print('Reduced Chi Square = ', Chi_Tup[1])
print(72*'=')
