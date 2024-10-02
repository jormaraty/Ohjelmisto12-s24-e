'''
Vastaukset tehtäviin löytyvät tiedostosta V2
'''

"""
F1 (4p):
Kirjoita seuraavaan funktio, jotta testi tuottaa halutun tuloksen.
Huom: kirjoita vain funktio, ei mitään muuta!

Testi eli pääohjelma:
nimi = "Maija"
print(tervehdi(nimi))

Haluttu tulos:
Hei Maija, mitä kuuluu?

"""

'''
Vastaus:
def tervehdi(nimi):
    return "Hei " + nimi + ", mitä kuuluu?"

Kommentit:
Peruskoodauksella pääohjelma (testi) olisi
    nimi = "Maija"
    tulos = tervehdi(nimi)
    print(tulos)
Edellisestä huomaa paremmin, että pääohjelma kutsuu funktiota tervehdi.
Lisäksi huomataan että funktio tarvitsee yhden parametrin eli alkuarvon.

Kokeessa käytetään lyhyempää koodia eli ns. ahdettua koodausta
    nimi = "Maija"
    print(tervehdi(nimi))
Kokeessa täytyy huomata, että pääohjelma hoitaa tulostuksen, ei funktio.
Funktion kutsu on siis 'piilotettu' print-lauseen sisään!
Opettele ja sisäistä tämä lyhyempi koodaustapa!

Kokeen testaaja menee sekaisin, jos kirjoittaa funktion sisään
print-komennon. Lopputuloksena tulee hankalasti ymmärrettävä virhe.
Kokeen testaaja ei myöskään hyväksy tulosta, 
jos koodisi ei tulosta loppumerkkiä (!, ?, ...) tai välilyönti puuttuu jne.
'''




'''
F2 (vaativa tehtävä)
Kirjoita alla olevaan ohjelmaan puuttuva funktio siten, että ohjelma 
etsii listasta kalleimman maalauksen/taulun ja tulostaa taulun nimen sekä hinnan.

Testi eli pääohjelma:

taulut = [
    {'nimi': 'Meri', 'hinta': 1280},
    {'nimi': 'Tyttö', 'hinta': 3100},
    {'nimi': 'Ilta', 'hinta': 2500},
]

kallein = etsi_kallein(taulut)
print(f"Kallein maalaus: {kallein['nimi']}")
print(f"On hinnaltaan: {kallein['hinta']}€")

# - - - - -
Haluttu tulos:
Kallein maalaus: Tyttö
On hinnaltaan: 3100€
'''

'''
Vastaus:
def etsi_kallein(taulut):
    # alkuarvot: kallein maalaus on listan eka alkio
    kallein_taulu = taulut[0]
    isoin_hinta = kallein_taulu['hinta']

    # käydään koko lista läpi, testataan löytyykö vielä isompi hinta?
    for maalaus in taulut:
        # muuttuja maalaus sisältää aina yhden listan taulun kaikki tiedot
        maalauksen_hinta = maalaus['hinta']
        if maalauksen_hinta > isoin_hinta:
            # löytyi vielä kalliimpi taulu, päivitetään kalleimman taulun tiedot
            kallein_taulu = maalaus
            isoin_hinta = maalauksen_hinta

    # for-toiston jälkeen muuttuja 'kallein_taulu' sisältää kaikki
    # listan kalleimman maalauksen/taulun tiedot.
    # Tämä tieto palautetaan nyt pääohjelmalle
    return kallein_taulu
'''

'''
Kommentit:
- pääohjelman 'taulut' on selkeästi lista.
- listan kukiin alkio on sanakirja (dictionary)
- sanakirja sisältää nyt 2 avainta (nimi ja hinta) sekä niiden arvot.
- vaativa tehtävä, mutta ei mahdoton!
    - pääohjelman kutsusta ('kallein = etsi_kallein(taulut)')
      paljastuu funktion nimi ja että se tarvitsee parametriksi listan.
    - pääohjelman 2 seuraavasta rivistä paljastuu että pääohjelma odottaa
      vastaukseksi yhtä sanakirjaa. 
      Pääohjelma ottaa funktion palauttaman arvon muuttujaan 'kallein'. 
    - Esim. koodinpätkä ( {kallein['nimi'] } viittaa sanakirjaan 
      eli haetaan tietoa muuttujan 'kallein' avaimen 'nimi' avulla.
'''