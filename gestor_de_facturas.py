import os
from extractor_pdf import ExtractorPDF
from modificator_excel import ModificatorExcel
from persistencia import Persistencia
import time


class GestorDeFacturas:
    def __init__(self, input_folder, output_folder, template_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.template_folder = template_folder

    def procesar_facturas(self):
        pdf_files = [file for file in os.listdir(
            self.input_folder) if file.lower().endswith('.pdf')]
        for pdf_file in pdf_files:
            ruta_pdf = os.path.join(self.input_folder, pdf_file)
            datos_factura = ExtractorPDF.extract_data_from_pdf(ruta_pdf)

            archivo_path = os.path.join(
                self.template_folder, 'num.txt')
            numero = Persistencia.leer_numero(archivo_path)
            numero += 1
            Persistencia.guardar_numero(numero, archivo_path)

            ruta_template = os.path.join(
                self.template_folder, 'template.xlsx')
            libro_excel = ModificatorExcel.modify_template_with_data(
                ruta_template, datos_factura, numero)

            nombre_archivo_salida = f'Factura nº {numero}.xlsx'
            ruta_output = os.path.join(
                self.output_folder, nombre_archivo_salida)
            Persistencia.guardar_en_excel(libro_excel, ruta_output)
            Persistencia.imprimir_excel(ruta_output)

            time.sleep(15)

            os.remove(ruta_pdf)
