import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from util.manhattan import distanta_manhattan_manual, distanta_manhattan_scipy

def citeste_vectori(cale_fisier):
    with open(cale_fisier, 'r') as f:
        linii = f.readlines()
        v1 = [float(x) for x in linii[0].split()]
        v2 = [float(x) for x in linii[1].split()]
    return v1, v2

def executa():
    cale_date = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../date.txt'))
    
    try:
        v1, v2 = citeste_vectori(cale_date)
        
        dm = distanta_manhattan_manual(v1, v2)
        ds = distanta_manhattan_scipy(v1, v2)
        
        print(f"Vectori cititi: \n V1: {v1}\n V2: {v2}")
        print("-" * 30)
        print(f"Rezultat Manual: {dm}")
        print(f"Rezultat SciPy:  {ds}")
        
    except Exception as e:
        print(f"Eroare: {e}")

if __name__ == "__main__":
    executa()