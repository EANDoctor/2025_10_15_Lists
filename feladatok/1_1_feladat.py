"""
1.1 Feladat
A program tároljon egy listában színeket. Kérjen be a felhasználótól egy színt, és állapítsa meg, hogy a megadott szín már szerepel-e az adott listában. A vizsgálat eredményéről tájékoztassa a program a felhasználót, és írja ki egymás mellé vesszővel elválasztva a lista által tartalmazott színeket!
"""

szinek = ["piros", "fehér", "zöld", "sárga"]

felhasznalo = input("Kérek egy színt: ")


if felhasznalo in szinek:
    print("A szín már szerepel a listában!")
else:
    print("A szín még nincsen a listában!")

print(f"A lista elemei:\n {", ".join(szinek)}")