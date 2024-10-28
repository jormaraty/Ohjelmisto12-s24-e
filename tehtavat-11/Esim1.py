class Koira:
    def __init__(self, name, tervehdys = "hau, hau!"):
        self.nimi = name
        self.tervehdys = tervehdys

    def tervehdi(self):
        print(f"{self.tervehdys}")

class RotuKoira(Koira):
    def __init__(self, name, rotu, tervehdys = "hau, hau" ):
        # kutsutaan yliluokan (Koira) alustajaa
        super().__init__(name, tervehdys)
        # määritellään oman luokan 8RotuKoira) uusi ominaisuus
        self.rotu = rotu

    # ylikirjoitetaan Koira-luokan toteutus eli
    # tehdään itse saman niminen metodi
    def tervehdi(self):
        print(f"{self.tervehdys}, rotuni on {self.rotu}")


koira1 = Koira("Rekku")
koira1.tervehdi()
hieno_koira = RotuKoira("Mr Bean", "Mopsi",
                        "vuh, vuh")
hieno_koira.tervehdi()
