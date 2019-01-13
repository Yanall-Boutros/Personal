import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import csv
with open('data.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

dayvals = []
weekvals = []

for elem in data:
    dayvals.append(int(elem[1]))
    if type(elem[4]) is not None and elem[4] is not '':
       weekvals.append(int(elem[4]))

with open('dc.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

day_n = []
day_a_n = []
day_b_n = []

for elem in data:
    day_n.append(int(elem[0]))
    day_a_n.append(float(elem[1]))
    day_b_n.append(float(elem[2]))

with open('wc.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

week_n = []
week_a_n = []
week_b_n = []

for elem in data:
    week_n.append(int(elem[0]))
    week_a_n.append(float(elem[1]))
    week_b_n.append(float(elem[2]))

days = np.linspace(0, len(dayvals), len(dayvals))
weeks = np.linspace(0, len(weekvals), len(weekvals))

plt.plot(days, dayvals, marker='.', markersize=2,
        linestyle='-', linewidth=0.5)
plt.xlabel("Day $n$")
plt.ylabel("Number of Fixit Tickets by Day")
plt.savefig("days.png")

plt.figure()

plt.plot(weeks, weekvals, marker='.', markersize=2,
        linestyle='--', linewidth=1)
plt.xlabel("Week $n$")
plt.ylabel("Number of Fixit Tickets by Week")
plt.savefig("Weeks.png")
plt.figure()
# Graph the first few terms of the fourier series
# f(x) = a_0/2 + a_n(cosnpix/l) + b_n(sin(npix/l))
fdays = np.linspace(1, len(day_n), len(day_n))
fweeks = np.linspace(1, len(week_n), len(week_n))
l = len(dayvals)
wl = len(weekvals)
a0half = day_a_n[0]/2
weeka0half = week_a_n[0]/2
fx = np.zeros(len(day_n))
fxweek = np.zeros(len(week_n))
fnlist = []
fnweeklist = []
for n in week_n:
    fnweeklist.append([])
    for week in fweeks:
        fnweeklist[n].append(
                week_a_n[n]*np.cos(np.pi*n*week/wl) +
                week_b_n[n]*np.sin(n*np.pi*week/wl)
                )
    if n < 10:
        plt.plot(fdays, fnweeklist[n],
                marker='.', markersize=1,
                linestyle='--', linewidth=0.5,
                label=('term ' + str(n) + ' in Fourier series'))
        plt.xlabel("Time (July 27, 2015 to January 7, 2019")
        plt.ylabel("Counts")
plt.legend(loc=1)
plt.title("Fourier Series decomposition (weeks)")
plt.savefig("weeknterms.png")
plt.figure()

for n in range(len(fnweeklist)):
    fxweek += fnweeklist[n]
fxweek += weeka0half*np.ones(len(fnweeklist))

plt.plot(fweeks, fxweek, marker='.', markersize=1,
        linestyle='--', linewidth=0.5)
plt.xlabel("Time (July 27, 2015 to January 7, 2019")
plt.ylabel("Counts")
plt.title("Fourier series representation (weeks)")
plt.savefig("fweek.png")
plt.figure()
for n in day_n:
    fnlist.append([])
    for day in fdays:
        fnlist[n].append(
                day_a_n[n]*np.cos(np.pi*n*day/l) +
                day_b_n[n]*np.sin(n*np.pi*day/l)
                )
    if n < 10:
        plt.plot(fdays, fnlist[n],
                marker='.', markersize=1,
                linestyle='--', linewidth=0.5,
                label=('term ' + str(n) + ' in Fourier series'))
        plt.xlabel("Time (July 27, 2015 to January 7, 2019")
        plt.ylabel("Counts")
plt.legend(loc=1)
plt.title("Fourier series decomposition (days)")
plt.savefig("daynterms.png")
plt.figure()
for n in range(len(fnlist)):
    fx += fnlist[n]
fx += a0half*np.ones(len(fnlist))
plt.plot(fdays, fx, marker='.', markersize=1,
        linestyle='--', linewidth=0.5)
plt.title("Fourier Series approximation on data fed by day")
plt.xlabel("Time (July 27, 2015 to January 7, 2019")
plt.ylabel("Counts")
plt.savefig("fday.png")
