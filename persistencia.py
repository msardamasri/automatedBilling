import os
import win32com.client


class Persistencia:
    @staticmethod
    def guardar_numero(numero, archivo):
        with open(archivo, 'w') as f:
            f.write(str(numero))

    @staticmethod
    def leer_numero(archivo):
        if os.path.exists(archivo):
            with open(archivo, 'r') as f:
                return int(f.read())
        else:
            return 0

    @staticmethod
    def guardar_en_excel(libro_excel, output_path):
        directorio = os.path.dirname(output_path)
        if not os.path.exists(directorio):
            os.makedirs(directorio)
        if os.path.exists(output_path):
            os.remove(output_path)
        libro_excel.save(output_path)

    @staticmethod
    def imprimir_excel(file_path):
        excel = win32com.client.Dispatch("Excel.Application")
        wb = excel.Workbooks.Open(os.path.abspath(file_path))
        wb.PrintOut()
        wb.Close(False)
        excel.Quit()
