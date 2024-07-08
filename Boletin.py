import requests
from bs4 import BeautifulSoup
from Serializador import Serializador

class Boletin():
    def boletines(self):
        informe=input("Escribe el nombre del archivo a guardar el informe: ")
        reporte=Serializador(informe)
        r=requests.get("https://www.colcert.gov.co/800/w3-propertyvalue-412601.html")
        if r.status_code==200:
            soup = BeautifulSoup(r.text, "html.parser")
            content_divs = soup.find_all('div', class_='p-4 card')
            
            for i in content_divs:
                text = i.get_text(separator='\n', strip=True)
                print(text)
                print()   
                reporte.generate_report(text)
