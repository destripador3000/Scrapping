import requests
from bs4 import BeautifulSoup
from Serializador import Serializador


class Vulnerabilidad():
    def vulnerabilidad(self):
        informe=input("Escribe el nombre del archivo a guardar el informe: ")
        
        reporte=Serializador(informe)
        
        r=requests.get("https://nvd.nist.gov/")
        if r.status_code==200:
            soup = BeautifulSoup(r.text, "html.parser")
            content_divs = soup.find_all('div', class_='col-lg-9')
            inicio="Severity"
            for i in content_divs:
                text = i.get_text(separator='\n', strip=True)
                indiceDeInicio =text.find(inicio)
                if indiceDeInicio!=-1:
                    texto=text[indiceDeInicio+8:]
                    print(texto)
            reporte.generate_report(texto)
