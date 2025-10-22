mindketto = []
csak_ot = []
csak_harom = []

for i in range(1,101):
    if (i % 3 == 0) and (i % 5 == 0):
        mindketto.append(i)
    elif i % 5 == 0:
        csak_ot.append(i)
    elif i % 3 == 0:
        csak_harom.append(i)


print(f"{mindketto}")
print(f"{csak_ot}")
print(f"{csak_harom}")