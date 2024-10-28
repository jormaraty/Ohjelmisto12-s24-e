'''
Tässä on alkua tehtävään 1.
Tästä ratkaisusta puuttuu jotakin...
Älä kopioi, vaan katso tarvittaessa mallia.
'''
class Julkaisu:
    def __init__(self, name):
        self.nimi = name

class Kirja(Julkaisu):
    def __init__(self, name, writer, pages):
        super().__init__(name)
        self.kirjailija = writer
        self.sivumäärä = pages

    def tulosta_tiedot(self):
        print("- Kirjan tiedot:")
        print(f"Nimi: {self.nimi}")
        print(f"Kirjailija: {self.kirjailija}")
        print(f"Sivuja {self.sivumäärä} kpl")

kirjaA = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
kirjaA.tulosta_tiedot()