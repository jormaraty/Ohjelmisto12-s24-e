'''
Määritellään Kissa-luokka,
jolla on kolme ominaisuutta.
'''

class Kissa:
    # määritellään luokan alustaja eli konstruktori
    def __init__(self, name, age):
        self.nimi = name
        self.ikä = age
        # määritellään uusi ominaisuus
        self.omistaja = "Tuntematon"
        # Nyt siis luokan ominaisuuksia ovat
        # nimi, ikä ja omistaja


# pääohjelma
# luon Kissa-tyyppisen olion
eka_kissa = Kissa("Pörri", 3)
# muokataan omistaja-ominaisuuden arvoa
eka_kissa.omistaja = "Heini"
# tulostetaan olion tietoja
print(f"Kissan nimi: {eka_kissa.nimi}, "
      f"omistaja on {eka_kissa.omistaja}")
