# Yanall Boutros
# Phys-133
# Lab 1 - Box_E.py
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

def ImpGuessMagFunc(freq, *guess_params):
   # This function returns the magnitude over a range of frequencies
   # provided a guess for what the capacitance might be
   # Let guess_params[0] = Capacitancee
   # Let guess_params[1] = Inductance
   # Let guesS_params[2] = Resistance
   omega = m.pi*2*freq
   a = (guess_params[2]**2 + (omega*guess_params[1]-((omega*guess_params[0])**-1))**2)**0.5
   return a

def ImpMag(V1, V2, R):
   # ImpCapMag reads as Impedence Magnitude, it is the
   # theoretical equation for calculating the magnitude of impedence
   return ((V1 * R)/V2)

def ImpLeastSquaresFit(xdata, ydata, y_sigma):
   # Least Squares Fit was originally a python program written by Prof.
   # David Smith, I have adapted and altered it to be generalized as an
   # individual function.
   Cap = 1.55e-9
   Induc = 7.2e-3
   Resist = 80
   guess_params = np.array([Cap, Induc, Resist])
   xsmooth = np.linspace(np.min(xdata),np.max(xdata), 1000)
   fsmooth = ImpGuessMagFunc(xsmooth, *guess_params)
   #plt.plot(xsmooth, fsmooth, color='red',
   #         label='Manual Impedance Guess', alpha=0.9)
   popt, pcov = opt.curve_fit(ImpGuessMagFunc, xdata, ydata, sigma=y_sigma,
                              p0=guess_params, absolute_sigma=1)
   fsmooth_next = ImpGuessMagFunc(xsmooth, *popt)
   plt.plot(xsmooth, fsmooth_next, color='black',
            label='Line of Best Fit', alpha=0.5)
   plt.legend(loc=1)
   
   # Chi Squared Test for Best Fit Line
   print()
   print(72*'=')
   print('Scipy.Curve_Fit Best Fit Line Chi Squared Test')
   print(72*'-')
   Mag_Fit = ImpGuessMagFunc(xdata, *popt)
   Chi_Squared = sum( (ydata - Mag_Fit)**2 / y_sigma**2)
   dof = len(ydata) - len(popt)
   Reduced_Chi_Squared = Chi_Squared / float(dof)
   print("Chi-square = ", Chi_Squared)
   print("Degrees of Freedom = ", dof)
   print("Reduced Chi Square = ", Reduced_Chi_Squared)

   print("Probability of exceeding this chi_square = ",
          1.-stat.chi2.cdf(Chi_Squared,dof))
 
   print("Confidence can we reject this model = ",
        stat.chi2.cdf(Chi_Squared,dof))
   print(72*'=')

def PhaseFitFunc(freq, *guess_params):
   omega = 2*m.pi*freq
   a = np.array((1/guess_params[2])*(omega*guess_params[1] - (1/(omega*guess_params[0]))))
   a = np.arctan(a)
   a /= m.pi
   a *= 180
   return -1*a

def PhaseLeastSquaresFit(xdata, ydata, y_sigma):
   # Least Squares Fit was originally a python program written by Prof.
   # David Smith, I have adapted and altered it to be generalized as an
   # individual function.
   Cap = 1.55e-9
   Induc = 7.2e-3
   Resist = 80
   guess_params = np.array([Cap, Induc, Resist])
   xsmooth = np.linspace(np.min(xdata),np.max(xdata), 1000)
   fsmooth = PhaseFitFunc(xsmooth, *guess_params)
   #plt.plot(xsmooth, fsmooth, color='red',
   #         label='Manual phase Guess', alpha=0.9)
   popt, pcov = opt.curve_fit(PhaseFitFunc, xdata, ydata, sigma=y_sigma,
                              p0=guess_params, absolute_sigma=1)
   fsmooth_next = PhaseFitFunc(xsmooth, *popt)
   plt.plot(xsmooth, fsmooth_next, color='red',
            label='Line of Best Fit', alpha=0.5)
   plt.legend(loc=1)
   
   # Chi Squared Test for Best Fit Line
   print()
   print(72*'=')
   print('Scipy.Curve_Fit Best Fit Line Chi Squared Test')
   print(72*'-')
   Mag_Fit = PhaseFitFunc(xdata, *popt)
   Chi_Squared = sum( (ydata - Mag_Fit)**2 / y_sigma**2)
   dof = len(ydata) - len(popt)
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
                 1.256, 2.106, 4.259, 5.952, 7.758, 9.662, 11.12, 14.18,
                 15.97, 16.32, 19.2, 22.38, 24.44, 27.62, 30.05, 32.3, 35.41,
                 37.15, 40.32, 40.98, 41.19, 41.74, 42.66, 43.33, 43.71, 44.01,
                 44.96, 45.79, 46.21, 46.73, 47.17, 47.44, 47.76, 48.69, 48.92,
                 49.36, 49.9, 51.02, 52.14, 53.59, 54.95, 56.18, 57.27, 58.21,
                 59.88, 61.96, 64.57, 67.56, 69.44, 71.53, 73.96, 76.69, 78.99,
                 79.49, 81.97, 84.75, 87.41, 89.45, 91.41, 94.52, 96.53, 99.4,
                 101.2
               ])

phase = np.array([
                  81.8, 82.3, 82.8, 82.3, 82, 81.7, 83, 83.7, 82.8,
                  83.7, 82.7, 82.8, 82.7, 83.9, 83.9, 83.7, 83.1,
                  81.3, 81.2, 80.3, 80.7, 78.7, 77.3, 77.2, 75, 74.9,
                  70.7, 65.3, 57.2, 38.4, 12.2, -1.02, -13.4, -38.1,
                  -45.8, -52.1, -60, -69.5, -73.5, -78.4, -82.3, -83.8,
                  -85.4, -86.3, -87.4, -89.2, -89.7, -92.9, -93.4, 
                  -93.5, -95.9, -98.8, -99.9, -100, -102, -104, -106,
                  -106, -109, -112, -111, -115, -115
                ])

resist = np.array([
                   90.3, 50.3, 24.07, 16.39, 12.39, 9.79, 8.29, 6.2,
                   5.39, 5.29, 4.28, 3.4, 2.998, 2.398, 2.058, 1.73,
                   1.33, 1.15, 0.779, 0.71, 0.689, 0.62, 0.55, 0.479,
                   0.429, 0.4, 0.3133, 0.2358, 0.1822, 0.1328, 0.1023,
                   0.1004, 0.1003, 0.1261, 0.1354, 0.1588, 0.1898,
                   0.2607, 0.334, 0.44, 0.552, 0.643, 0.743, 0.83, 0.933,
                   1.09, 1.3, 1.499, 1.661, 1.799, 1.998, 2.238, 2.398,
                   2.448, 2.668, 2.89, 3.145, 3.36, 3.54, 3.95, 4.12,
                   4.57, 4.69
                  ])

volt1 = np.array([
                  7.44, 7.6, 7.68, 7.84, 7.84, 7.84, 7.92, 8, 8, 7.92,
                  7.92, 8, 8, 8, 8, 8, 7.92, 7.84, 7.84, 7.76, 7.76,
                  7.84, 7.68, 7.6, 7.52, 7.52, 7.2, 7.04, 6.72, 6.16,
                  5.92, 5.76, 5.92, 6.32, 6.48, 6.64, 6.96, 7.28, 7.6,
                  7.92, 8, 8.16, 8.16, 8.24, 8.32, 8.48, 8.56, 8.8, 8.8,
                  9.2, 9.2, 9.28, 9.36, 9.44, 9.6, 9.76, 10.1, 10.3,
                  10.4, 10.7, 10.8, 11.1, 11.4
                ])

volt2 = np.array([
                  8.24, 8.16, 8.16, 8.16, 8.08, 8.08, 8, 8, 8.08, 8.16,
                  8.16, 8.08, 8.16, 8.08, 8.08, 8.08, 8, 8.08, 7.84,
                  7.84, 7.76, 7.76, 7.76, 7.68, 7.6, 7.6, 7.44, 7.12,
                  6.8, 6.32, 5.92, 5.92, 5.92, 6.24, 6.4, 6.72, 6.88,
                  7.36, 7.68, 7.84, 8.16, 8.16, 8.32, 8.32, 8.48, 8.64,
                  8.8, 8.8, 8.96, 9.2, 9.2, 9.44, 9.44, 9.44, 9.6, 9.76,
                  10.1, 10.3, 10.4, 10.9, 10.9, 11.4, 11.4
                 ])
# Print out the shapes
# Unit conversions
freq *= 1000
resist *= 1000

freq_sigma = np.ones(63)*500
phase_sigma = np.ones(63)*3
resist_sigma = np.ones(63)
volt1_sigma = np.ones(63)*.4
volt2_sigma = np.ones(63)*.4
# Graph for Impedance
# Calculate Z and Z_sigma
Z = ImpMag(volt1, volt2, resist)
Z_sigma = sigz(resist, volt1, volt2, volt1_sigma,volt2_sigma, resist_sigma)

# Plot Raw Data with Error Bars
plt.errorbar(freq, Z, xerr=freq_sigma, yerr=Z_sigma, color='blue',
             marker='.', linestyle='None', label="Impedance",alpha=0.7)

plt.title("Magnitude of Impedance vs. Frequency")

plt.xlabel("Frequency (Hz)")
plt.ylabel("Impedance ($\Omega$)")

# Run Least Squares Fit to generate line of Best
ImpLeastSquaresFit(freq, Z, Z_sigma)
plt.ylim(0, 90000)
plt.savefig("Box E Impedance.pdf")
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
PhaseLeastSquaresFit(freq, phase, phase_sigma)
plt.legend(loc=1)
plt.savefig("Box E Phase.pdf")
