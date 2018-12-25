import numpy as np
import matplotlib as plt
p_dnl = 0
p_dil = 0
p_ynl = 0
p_mrc = 0
p_mny = 0
p_grt = 0
p_mia = 0
p_ray = 0

pvec =[p_dil,
       p_dnl,
       p_ynl,
       p_mrc,
       p_mny,
       p_grt,
       p_mia,
       p_ray]
def dishes_per_day(p_person):
    return 3*p_person

prob_pos = np.linspace(0, 1, 11)

# make a graph of how the total dishes over time per person, and added
# together contribute via each10% increment per persons prob
for p_person in pvec:
    for prob in prob_pas:
        p_person = prob
        

