"""
Tämä tiedosto sisältää Flask-palveluiden tarvitsemia funktioita.
"""

# Funktio palauttaa tiedon, että onko parametrina saatu numero alkuluku vai ei.
# Funktio palauttaa boolean-tyyppisen vastauksen (True/False)
def tarkistaAlku(arvo):
    tulos = True        # alkuoletus: arvo on alkuluku
    # jaetaan parametrina saatu 'arvo' arvoilla 2,3,4 ... arvo-1.
    # Jos arvo on jaollinen yhdelläkin jakajan arvolla, niin arvo ei ole alkuluku.
    for jakaja in range(2, arvo):
        if arvo % jakaja == 0:
            # jakolasku meni tasan -> parametrina saatu arvo ei ole alkuluku
            tulos = False
            # lopetetaan toistorakenne heti, lopputulos on selvä
            break
    return tulos
