from scipy.spatial.distance import cityblock

def distanta_manhattan_manual(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectorii trebuie să aiba aceeasi dimensiune!")
    return sum(abs(a - b) for a, b in zip(v1, v2))

def distanta_manhattan_scipy(v1, v2):
    return cityblock(v1, v2)