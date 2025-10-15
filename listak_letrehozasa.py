honapok = ["január", "február", "március", "április", "május", "június"]

#típusa
print(type(honapok))

#lista hossza: len()
print(len(honapok))

print(honapok[0])
print(honapok[1])
print(honapok[2])
print(honapok[3])

#háturról az első elem
print(f"Utolsó elem a listában. {honapok[-1]}")

#csak 1-es és 2-es elemek kiíratása.
print(honapok[1:3])

#2-es elemmel bezárólag.
print(honapok[:3])

#2-es elemtől végéig.
print(honapok[2:])

#.join(): a lista elemeit egy sztringgé fűzi össze.
print(', ' .join(honapok))

#lista bejárása for range ciklussal.
for i in range(len(honapok)):
    print(honapok[i])

# lista bejárása: for - items.
print("\nHónapok:")
for honap in honapok:
    print(honap)

#