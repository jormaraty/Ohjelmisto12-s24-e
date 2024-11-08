"""
    Tämä versio käyttää apuna toisessa tiedostossa
    olevaa funktiota.
    Tämä versio kuuntelee porttia 5000.
    Kutsu esim: http://localhost:5000/alkulukuV2/31
    Muuten sama toiminta kuin Teht1.
"""

from flask import Flask
# otetaan mukaan toisesta tiedostosta yksi funktio.
from apufunktiot import tarkistaAlku

app = Flask(__name__)

@app.route('/alkulukuV2/<int:luku>')
def onkoAlku(luku):
    # pyydetään toisen tiedoston funktiota
    # tarkistamaan että onko alkuluku
    onAlkuLuku = tarkistaAlku(luku)

    # muodostetaan vastaus
    vastaus = {
        "Number": luku,
        "isPrime": onAlkuLuku
    }

    # palautetaan vastaus selaimelle
    return vastaus

# määritellään että tätä palvelua
# kuuntelee portti 5000
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
