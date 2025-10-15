honapok = ["január", "február", "március", "április", "május", "június"]

#listsa végére hozzáfűzhetsz egy elemet.
honapok.append("július")
print(honapok)

#Elelm eltávolítása listából.
honapok.pop()
print(f"Utolsó hónap törlése után a lista:\n {honapok}")
torolt_honap = honapok.pop()
print(f"Utolsó hónap: {torolt_honap}")
print(honapok)

#törlés adott index alapján
torolt_honap = honapok.pop(0)
print(torolt_honap)

#Törlés érték alapján.
print(honapok.remove("február"))
print(honapok)

#adott indexű helyre beszúrja a megadott elemet.
honapok.insert(0, "február")
print(honapok)

#lista kiürítése:
honapok.clear()
print(honapok)