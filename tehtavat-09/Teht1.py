'''
Määritellään Auto-luokka
'''

class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekisteritunnus =rekkari
        self.huippunopeus = huippunopeus
        # määritellään loput ominaisuudet
        self.nopeus = 0
        self. matka = 0


# pääohjelma: luodaan olio ja tulostetaan sen arvot
auto1 = Auto("ABC-123", 142)
print("Auto-tyyppisen olion ominaisuudet:")
print(f"Rekkari: {auto1.rekisteritunnus}")
print(f"HUippunopeus: {auto1.huippunopeus}")
# TODO: tulosta myös tämän hetkinen nopeus ja kuljettu matka
