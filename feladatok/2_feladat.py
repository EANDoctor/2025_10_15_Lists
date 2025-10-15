"""
2. Feladat
A program generáljon 10 darab véletlenszámot [1;3] intervallumon, ezeket tárolja egy listában, a lista tartalmát írja ki a képernyőre! A felhasználónak legyen lehetősége megadni egy számot [1;3] intervallumon, és a program törölje ennek a számnak valamennyi előfordulását a listából, majd írja ki a módosított listát a képernyőre!
"""
import os
import random as r

numbers = []

for i in range(1,11):
    random = r.randint(1,3)
    numbers.append(random)

user = int(input("Adj meg egy számot 1 és 3 között!: "))

if user in numbers:
    while user in numbers:
        numbers.remove(user)
else:
    print("A megadott opciókból válassz!")

print(numbers)

# Clear screen for Windows
input()
os.system('cls')
quit()