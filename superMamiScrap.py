import requests
from bs4 import BeautifulSoup
import csv
import time

BASE_URL = "https://www.dinoonline.com.ar/super/categoria/supermami-bebidas-vinos/_/N-5ctet6"
URL_ACTUAL = BASE_URL

todos_los_vinos= []

n = 0
while True:
    n += 1
    response = requests.get(URL_ACTUAL)
    soup = BeautifulSoup(response.text, "html.parser")

    vinos = soup.find_all("div", class_="product")
    
    for vino in vinos:
        nombre = vino.select_one("div.descripcion.limitRow.tooltipHere")
        precio = vino.find("div", class_="precio-unidad")

        if nombre and precio:
            nombre = nombre.text.strip()
            precio = precio.find("span").text.strip()
            precio = float(re.sub(r"[^\d.]", "", precio.replace(",",".")))

    print("{n} paginas scrapeadas")

    boton_next = soup.find



