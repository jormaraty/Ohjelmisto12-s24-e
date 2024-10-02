'''
Tämä tiedosto sisältää vastauksia ja kommentteja T3-tiedoston tehtäviin
'''

# 1. Käy läpi python-teorian kohta 8 'Relaatiotietokannan käyttö'
# ja erityisesti sen kohta 'Hakukysely ja tulosjoukon käsittely'
# https://github.com/vesavvo/Python_Ohjelmistoteema/blob/main/08_Relaatiotietokannan_k%C3%A4ytt%C3%B6.md#hakukysely-ja-tulosjoukon-k%C3%A4sittely

'''
Kommentit:
- edellä olevan esimerkin läpikäynti ja ymmärtäminen 
  voi antaa helposti paljon pisteitä
- vastaavan koodin jälkeen on usein jopa hassuja väitteitä:
    - Python-koodin suoritus käynnistää tietokannan.        FALSE
    - koodi muokkaa tietokannan tietoja (SELECT-lause?!?)   FALSE
    - koodi tulostaa 3 ensimmäisen rivin id-arvot           FALSE
    - Python koodissa SELECT-lause voi kohdistua vain yhteen tauluun    FALSE
- usein väite on 1p arvoinen, mutta niitä on yleensä useita.  
'''


# 2. Tee seuraavista lauseista kelvollinen ohjelma,
#    joka hakee tietokannan taulusta dataa ja tulostaa saamansa tiedot.
#    Poimi seuraavista lauseista 6 olennaista kohtaa oikeaan järjestykseen.

'''
print(formatted_db_data)
import mysql.connector
connection = mysql.connector(...)
import mysql.helper
result = cursor.fetchall()
cursor.execute("SELECT etunimi, sukunimi FROM tyontekija WHERE ...")
print(result[0] [1])
result = cursor.getResult()

'''

'''
Vastaus:
# kirjasto joka sisältää tarvittavat palikat tietokannan käsittelyyn
import mysql.connector    

# yhteys tietokantaan
connection = mysql.connector(...)
# luodaan ns. yhteysolio (kursori), jonka avulla kommunikoidaan tietokannan kanssa
cursor = connection.cursor()
# suoritetaan hakulause, kursorin avulla
cursor.execute("SELECT etunimi, sukunimi FROM tyontekija WHERE ...")
# otetaan kursorin saamat kaikki tulosrivit talteen muuttujaan result
result = cursor.fetchall()
# tulostetaan osa result-muuttujan sisältöä (ns. raakatulostus)
print(result[0] [1])

'''

'''
Kommentit:
- edellä olevan yleiskuvan hahmottaminen auttaa jo pitkälle
- yleensä ei kysytä mitään pieniä nippeliasioita
- import-lausetta ei aina ole valinnoissa mukana
    -> aloitetaan tietokantayhteyden luomisesta.

'''