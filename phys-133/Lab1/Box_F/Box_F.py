# Yanall Boutros
# Phys-133
# Lab 1 - Box_F.py
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
   # Let guess_params[1] = Resistance
   omega = m.pi*2*freq
   a = ((guess_params[1]**-2 + (((omega*guess_params[0])**2)))**0.5)**-1
   return a

def ImpMag(V1, V2, R):
   # ImpCapMag reads as Impedence Magnitude, it is the
   # theoretical equation for calculating the magnitude of impedence
   return ((V1 * R)/V2)

def ImpLeastSquaresFit(xdata, ydata, y_sigma):
   # Least Squares Fit was originally a python program written by Prof.
   # David Smith, I have adapted and altered it to be generalized as an
   # individual function.
   Cap = 8e-9
   Resist = 2300
   guess_params = np.array([Cap, Resist])
   xsmooth = np.linspace(np.min(xdata),np.max(xdata), 1000)
   fsmooth = ImpGuessMagFunc(xsmooth, *guess_params)
   #plt.plot(xsmooth, fsmooth, color='red',
   #         label='Manual Impedance Guess', alpha=0.9)
   popt, pcov = opt.curve_fit(ImpGuessMagFunc, xdata, ydata, sigma=y_sigma,
                              p0=guess_params, absolute_sigma=1)
   for elem in popt:
      print(elem)
   fsmooth_next = ImpGuessMagFunc(xsmooth, *popt)
   plt.plot(xsmooth, fsmooth_next, color='red',
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
   a = omega*guess_params[0]*guess_params[1]
   a = np.arctan(a)
   a /= m.pi
   a *= 360
   a = (-.5*a)+180
   a = 180 - a
   return a

def PhaseLeastSquaresFit(xdata, ydata, y_sigma):
   # Least Squares Fit was originally a python program written by Prof.
   # David Smith, I have adapted and altered it to be generalized as an
   # individual function.
   Cap = 8e-9
   Resist = 2300
   guess_params = np.array([Cap, Resist])
   xsmooth = np.linspace(np.min(xdata),np.max(xdata), 1000)
   fsmooth = PhaseFitFunc(xsmooth, *guess_params)
   #plt.plot(xsmooth, fsmooth, color='red',
   #         label='Manual phase Guess', alpha=0.9)
   popt, pcov = opt.curve_fit(PhaseFitFunc, xdata, ydata, sigma=y_sigma,
                              p0=guess_params, absolute_sigma=1)
   fsmooth_next = PhaseFitFunc(xsmooth, *popt)
   plt.plot(xsmooth, fsmooth_next, color='red',
            label='Line of Best Fit', alpha=0.5)
   plt.legend(loc=3)
   
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
                 489.6, 541.2, 600.2, 803.9, 916.3, 1023.8, 1396.6,
                 1921.7, 2472.5, 2953.2, 3408.5, 5519.7, 7537.6, 9651.6,
                 14558, 34420, 55388, 75216, 96127, 19185
               ])

phase = np.array([
                  177, 176, 176, 175, 174, 173, 166, 166, 162, 158,
                  155, 147, 139, 131, 119, 106, 104, 99.8, 99.7, 112
                ])
 
resist = np.array([
                   700, 700, 700, 700, 700, 700, 700, 700, 700, 1000,
                   1000, 1000, 1000, 1000, 1000, 1000, 1000, 500, 500,
                   500
                 ])

volt1 = np.array([
                  1.52, 1.48, 1.48, 1.48, 1.48, 1.48, 1.52, 1.52, 1.48,
                  1.4, 1.36, 1.36, 1.32, 1.28, 1.2, 0.84, 0.6, 0.8,
                  0.68, 1.48
                ])

volt2 = np.array([
                  0.46, 0.46, 0.46, 0.46, 0.46, 0.46, 0.46, 0.46, 0.46,
                  0.62, 0.64, 0.72, 0.8, 0.9, 1.12, 1.6, 1.7, 1.64,
                  1.68, 0.88
                ])
# Print out the shapes
freq_sigma = np.ones(20)*500
phase_sigma = np.ones(20)*3
resist_sigma = np.ones(20)
volt1_sigma = np.ones(20)*.04
volt2_sigma = np.ones(20)*.04
# Graph for Impedance
# Calculate Z and Z_sigma
Z = ImpMag(volt1, volt2, resist)
Z_sigma = sigz(resist, volt1, volt2, volt1_sigma,volt2_sigma, resist_sigma)

# Plot Raw Data with Error Bars
plt.errorbar(freq, Z, xerr=freq_sigma, yerr=Z_sigma, color='blue',
             marker='.', linestyle='None', label="Impedance",alpha=0.5)

plt.title("Magnitude of Impedance vs. Frequency")

plt.xlabel("Frequency (Hz)")
plt.ylabel("Impedance ($\Omega$)")

# Run Least Squares Fit to generate line of Best
ImpLeastSquaresFit(freq, Z, Z_sigma)
plt.savefig("Box F Impedance.pdf")
# Graph For Phase Difference
# Create New Figure
plt.figure()

# Plot Raw Data with Error Bars
phase = 180 - phase
plt.errorbar(
             freq, phase, xerr=freq_sigma, yerr=phase_sigma,
             color='blue', marker='.', linestyle='None',
             label='Phase Difference', alpha=0.6
            )

plt.title("Phase Difference vs Frequency")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase Difference (Degrees)")
PhaseLeastSquaresFit(freq, phase, phase_sigma)
plt.legend(loc=4)
plt.savefig("Box F Phase.pdf")
