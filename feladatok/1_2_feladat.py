"""
1.2 Feladat
Alakítsuk át az előbbi programot úgy, hogy a program arról adjon tájékoztatást, hogy pontosan hányszor szerepel a felhasználó által megadott szín a listában! Ha a megadott szín nincs még tárolva, továbbra is a "A megadott szín nem szerepel a listában." szöveg jelenjen meg!
"""

szinek = ["piros", "fehér", "zöld", "sárga",]

felhasznalo = input("Kérek egy színt: ")

if felhasznalo in szinek:
    print(f"A szín már szerepel a listában! {szinek.count(felhasznalo)}-szer")
else:
    print("A szín még nincsen a listában!")

print(f"A lista elemei:\n {", ".join(szinek)}")