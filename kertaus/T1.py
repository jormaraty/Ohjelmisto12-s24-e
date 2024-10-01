# Onko if-ehto totta jos x = 11?
x = 11
if x > 5 or x <= 10:
    print("if-ehto on tosi")


# Muista myös esim:
    # while-toistoa ei välttämättä suoriteta kertaakaan
    # while-toisto voi jäädä ikuiseen silmukaan


# Mitä seuraava tulostaa?
luku = 1
while luku % 5 > 0:
    # tänne tullaan, kun ???
    print(luku)
    luku += 3
print(luku)

# Onko kelvollinen listarakenne?
lista1 = (1, 3, 5, -1)
lista2 = [1, 2, -3, 4]
lista3 = [1, 'toka', 3, 4]


# mitä seuraava tulostaa?
nimet = ['Anna', 'Matti']
nimet.append('Tiina')
nimet.append('Mikko')
nimet.remove('Matti')

print(nimet)
print(nimet[1:3])
print(nimet[-1])

# Mitä seuraava tulostaa?
people = ("Matti", "Pekka", "Anne")
anne, maija, pekka = people
print(anne)
print(people[1])
print(people)

