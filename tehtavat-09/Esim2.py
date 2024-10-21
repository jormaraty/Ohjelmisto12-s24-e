'''
Laajennetaan Kissa-luokkaa
'''

class Kissa:
    # määritellään staattinen luokkamuuttuja
    kissojenLkm = 0

    # määritellään luokan alustaja eli konstruktori
    def __init__(self, name, age, tervehdys = "miau, miau"):
        self.nimi = name
        self.ikä = age
        self.tervehdys = tervehdys
        # määritellään uusi ominaisuus
        self.omistaja = "Tuntematon"
        # Nyt siis luokan ominaisuuksia ovat
        # nimi, ikä, tervehdys ja omistaja

        # päivitetään luokkamuuttujan arvoa yhdellä,
        # HUOM; ei self vaan luokan nimen avulla
        Kissa.kissojenLkm += 1

    def tervehdi(self):
        print(self.tervehdys)


# luom pari kissaa ja pyydän niitä tervehtivään
kissa2 = Kissa("Mirri", 1)
kissa3 = Kissa("Mörkö", 7, "MOOUUU!!!")
kissa2.tervehdi()
kissa3.tervehdi()
print(f"Kissoja on {Kissa.kissojenLkm} kpl")