import math         # lopun piin tulostusta varten

'''
While-toistorakenne:
Ohjelma kysyy käyttäjältä nimiä ja
tervehtii henkilöä nimellä.
Ohjelma kysyy nimiä kunnes käyttäjä antaa
tyhjän nimen (pelkkä Enter).
'''

nimi = input("Anna nimi (tyhjä lopettaa): ")
while nimi != "":
    print("Hei " + nimi + ", mitä kuuluu?")
    # muista kysyä uusi arvo muuttujalle nimi!!!
    # muuten ikuinen silmukka
    nimi = input("Anna uusi nimi: ")

print("While-toisto loppui")

'''
Desimaaliluvun tulostus halutulla tarkkuudella
Muotoiltu eli formatoitu tulostus
'''
tarkka_pii = math.pi        # piin arvo melko tarkasti

# huomaa 'f' ennen merkkijonon alkua,
# muuttuja merkkijonon keskellä, aaltosulkujen {..} sisällä.
# '\n' on rivinvaihto.

print(f"\nPiin arvo melko tarkasti {tarkka_pii}, eikös vain")

# alla ':.3f' tarkoittaa: 3 numeroa desimaalipisteen jälkeen
print(f"Piin arvo 3 desimaalilla {tarkka_pii:.3f}")
