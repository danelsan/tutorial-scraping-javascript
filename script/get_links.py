import requests
from bs4 import BeautifulSoup

# URL della pagina
url = "http://web/example_js_link.html"

# Effettua la richiesta HTTP alla pagina
response = requests.get(url)

# Verifica se la richiesta ha avuto successo
if response.status_code == 200:
    # Analizza il contenuto HTML della pagina
    soup = BeautifulSoup(response.text, 'html.parser')

    # Trova tutti gli elementi <a> (link)
    links = soup.find_all('a')

    # Stampa il testo e l'URL di ogni link
    for link in links:
        print(f"Testo: {link.text}, URL: {link.get('href')}")
else:
    print(f"Errore: Impossibile accedere alla pagina (status code: {response.status_code})")
