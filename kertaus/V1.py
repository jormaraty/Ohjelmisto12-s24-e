'''
Vastaukset T1-tiedoston tehtäviin.
'''

# 1. Onko if-ehto 'if x > 5 or x <= 10' tosi/True jos x = 11?

'''
Vastaus: if ehto on TOSI

- if-ehdossa on 2 ehtoa, joiden välissä on or
-> riittää että jompi kumpi ehdoista on tosi.
Jos x = 11, niin ehto 'x > 5' on tosi -> koko if-ehto on tosi.
- if-ehto on nyt 'hassu': onkohan if-ehto todellakin tosi kaikilla x arvoilla ;)
'''

# 2. Mitä seuraava tulostaa?
luku = 1
# while-ehdossa pyöritään, kunnes muuttuja 'luku' on jaollinen 5:llä.
while luku % 5 > 0:
    print(luku)
    luku += 3
# huomaa: alla oleva lause suoritetaan aina lopuksi.
print(luku)

'''
Vastaus:
1
4
7
10

- while-toisto tulostaa arvot: 1, 4 ja 7.
- viimeinen print-lause tulostaa arvon: 10
'''

# 3. Mitkä alla olevista muodostavat lista-rakenteen?
lista1 = (1, 3, 5, -1)
lista2 = [1, 2, -3, 4]
lista3 = [1, 'toka', 3, 4]

'''
Vastaus:
Lista2 ja lista 3 ovat lista-rakenteita. Huomaa listan sulut [...]

- lista1 on monikko (tuple). Huomaa normisulut (..)
- lista3 on syntaksisesti oikein, mutta ei suositella numeroita ja tekstiä sekaisin.
'''

# 4. Mitä seuraava tulostaa?
nimet = ['Anna', 'Matti']
nimet.append('Tiina')
nimet.append('Mikko')
nimet.remove('Matti')

print(nimet)
print(nimet[1:3])
print(nimet[-1])

'''
Vastaus:
['Anna', 'Tiina', 'Mikko']
['Tiina', 'Mikko']
Mikko

- append lisää uuden arvon listan loppuun
- remove poistaa yhden alkion listasta, jos alkio löytyy listasta (nyt 'Matti' poistettiin)
    -> poisto ei jätä tyhjää 'koloa' listaan, loput alkiot siirtyväy pykälän eteenpäin. 
- 'print(nimet)' tulostaa koko listan sisällön, huomaa ympärille tulevat sulut [...]
    - tällä Python ilmoittaa että se tulosti listan sisällön
- huomaa väli [1:3]
    - alkuarvo 1 tulee mukaan tulosjoukkoon, loppuarvo 3 EI tule
    -> nyt tulostaan arvot listan indekseistä 1 ja 2 eli 'Tiina' ja 'Mikko'
    -> ympärille sulut [...] koska tulosti osan listan sisällöstä (useita arvoja).
- indeksi [-1]
    - tarkoittaa aina listan viimeistä arvoa, nyt 'Mikko'.
    - huomaa: ei sulkuja, koska tulosti vain yhden solun/alkion sisällön lista-takenteesta.
'''

# 5. Mitä seuraava tulostaa?
people = ("Matti", "Pekka", "Anne")
anne, maija, pekka = people
print(anne)
print(people[1])
print(people)

'''
Vastaus:
Matti
Pekka
('Matti', 'Pekka', 'Anne')

- people on monikko (tuple). Sulut (...) kertovat sen.
    - monikon arvot ovat luonnin jälkeen vakioita eli monikon arvoja ei voi muuttaa.
Huomaa: 
- anne, maija, pekka ovat muuttujia
- "Matti", "Pekka", "Anne" ovat monikon arvoja (merkkijonoja eli tekstiä)
Lause 'anne, maija, pekka = people'
-> muuttuja anne saa arvokseen monikon people 1. arvon eli nyt "Matti", 
   muuttuja maija saa arvokseen monikon 2. arvon eli "Pekka, 
   muuttuja pekka saa arvokseen monikon viimeisen arvon eli nyt "Anne"
print(people) tulostaa monikon koko sisällön
    - Python tulostaa ympärille monikon sulut (...)
 
'''