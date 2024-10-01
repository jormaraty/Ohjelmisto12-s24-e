'''
Vastaukset tehtäviin löytyvät tiedostosta V1
'''

# 1. Onko if-ehto 'if x > 5 or x <= 10' tosi/True jos x = 11?

# 2. Mitä seuraava tulostaa?
luku = 1
while luku % 5 > 0:
    print(luku)
    luku += 3
print(luku)

# 3. Mitkä alla olevista muodostavat lista-rakenteen?
lista1 = (1, 3, 5, -1)
lista2 = [1, 2, -3, 4]
lista3 = [1, 'toka', 3, 4]


# 4. Mitä seuraava tulostaa?
nimet = ['Anna', 'Matti']
nimet.append('Tiina')
nimet.append('Mikko')
nimet.remove('Matti')

print(nimet)
print(nimet[1:3])
print(nimet[-1])


# 5. Mitä seuraava tulostaa?
people = ("Matti", "Pekka", "Anne")
anne, maija, pekka = people
print(anne)
print(people[1])
print(people)
