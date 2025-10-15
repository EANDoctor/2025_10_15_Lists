honapok = ["január", "február", "március", "április", "május", "június"]
#honapok = [1 , 3 , 5 , 2]

# sorbarendezi a listát
sorted_honapok = sorted(honapok)
print(honapok)
print(sorted_honapok)
# honapok.sort()
# print(honapok)

reversed_honapok = sorted(honapok, reverse=True)
print(reversed_honapok)

# az adott elem első előfordulásának indexe
print(honapok.index("március"))

# NEM listametódus, de így lehet eldönteni, hogy egy elemet tartalmaz-e a lista
print("április" in honapok)


