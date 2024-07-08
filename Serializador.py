import datetime

class Serializador:
    def __init__(self, file_path):
        self.file_path = file_path
    def generate_report(self, content):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        report_content = f"Informe generado el: {timestamp}\n\n{content}"
        if self.file_path:
            try:
                with open(self.file_path, 'a', encoding="utf-8") as file:
                    file.write(report_content)
                print(f"Reporte generado exitosamente {self.file_path}")
            except IOError as e:
                print(f"Error al generar archivo {self.file_path}: {e}")
        else:
            print(report_content)

