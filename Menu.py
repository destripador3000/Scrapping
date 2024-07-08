from Boletin import Boletin
from Vulnerabilidad import Vulnerabilidad
class Menu():
    def menu(self):
        vulnerabilidad=Vulnerabilidad()
        boletin=Boletin()
        continuar=True
        while continuar:        
        
            print("""
            # {}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}
            # {}________                     __           .__                    .___               {}
            # {}\______ \    ____    _______/  |_ _______ |__|______ _____     __| _/ ____ _______  {}
            # {} |    |  \ _/ __ \  /  ___/\   __\\_  __ \|  |\____ \\__  \   / __ | /  _ \\_  __ \ {}
            # {} |    `   \\  ___/  \___ \  |  |   |  | \/|  ||  |_> >/ __ \_/ /_/ |(  <_> )|  | \/ {}
            # {}/_______  / \___  >/____  > |__|   |__|   |__||   __/(____  /\____ | \____/ |__|    {}
            # {}        \/      \/      \/                    |__|        \/      \/                {}
            # {}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}      
            
            1) Buscar últimas vulnerabilidades (CVE) en la NATIONAL VULNERABILITY DATABASE
            2) Buscar Boletines de la COLCERT (Incidentes de ciberseguridad en Colombia)
            0) Salir\n
            """)
            opc=int(input("Escribe la opción: "))
            
            if opc==1:
                vulnerabilidad.vulnerabilidad()
            elif opc==2:
                boletin.boletines()
            elif opc==0:
                continuar=False
            else:
                print("Opción no válida...")
        
        
