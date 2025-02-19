from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Configura opzioni per ChromeDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Esegue il browser in modalità headless
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--remote-debugging-port=9222")

# Inizializza il driver di Chrome
chrome = webdriver.Chrome( options=chrome_options)

try:
    # Carica la pagina
    chrome.get("http://web/example_js_link.html")

    # Trova tutti i link sulla pagina
    links = chrome.find_elements(By.TAG_NAME, "a")

    # Stampa il testo e l'URL di ogni link
    for link in links:
        print(f"Testo: {link.text}, URL: {link.get_attribute('href')}")
finally:
    # Chiude il browser
    chrome.quit()
