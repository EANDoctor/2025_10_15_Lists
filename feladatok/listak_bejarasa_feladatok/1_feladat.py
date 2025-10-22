"""
1. Feladat
Készíts egy programot, amely [1; 40] intervallumon kiírja a 3-mal osztható számokat!
"""

oszthato = []
for i in range(1,41):
    if i % 3 == 0 and i % 2 == 0:
        oszthato.append(i)

print(f"hárommal osztható és páros szám: {oszthato}")