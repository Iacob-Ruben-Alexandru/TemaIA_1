import math

from scipy.spatial.distance import cityblock

def distanta_manhattan_manual(v1, v2):
    # Calculeaza distanta Manhattan manual.
    man = []
    x = min(len(v1), len(v2))
    for i in range(x):
        man.append(abs(v1[i] - v2[i]))
    return sum(man)

def distanta_manhattan_scipy(v1, v2):
    # Calculeaza distanta Manhattan folosind functia din biblioteca SciPy.
    if(len(v1) != len(v2)):
        if(len(v1) > len(v2)):
            v1 = v1[:len(v2)]
        else:
            v2 = v2[:len(v1)]
    return cityblock(v1, v2)