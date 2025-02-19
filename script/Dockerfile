# Utilizza l'immagine ufficiale di Python come base
FROM python:3.9-slim

# Installa le dipendenze di sistema necessarie
RUN apt-get update && apt-get install -y \
    chromium-driver \
    chromium \
    && rm -rf /var/lib/apt/lists/*

# Imposta la directory di lavoro all'interno del container
WORKDIR /app

# Copia il file requirements.txt nella directory di lavoro
COPY requirements.txt .

# Installa le dipendenze Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia il resto del codice dell'applicazione nella directory di lavoro
COPY . .

# Imposta il PATH per chromedriver
ENV PATH="/usr/lib/chromium:/usr/bin/chromedriver:${PATH}"

# Comando per eseguire lo script Python
CMD ["python", "get_links.py"]
