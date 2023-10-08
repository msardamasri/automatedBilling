import pdfplumber
import re


class ExtractorPDF:
    @staticmethod
    def extract_data_from_pdf(pdf_path):
        with pdfplumber.open(pdf_path) as pdf:
            texto_completo = ""
            for page in pdf.pages:
                texto_completo += page.extract_text()
            datos_factura = {
                'Autofacturacion': ExtractorPDF.extraer_numero(texto_completo.split('\n')[10]),
                'Fecha_servicio': ExtractorPDF.extract_date(texto_completo.split('\n')[12]),
                'Total': ExtractorPDF.extract_total(texto_completo.split('\n')[17]),
                'Direccion_servicio': texto_completo.split('\n')[13],
                'Referencia': texto_completo.split('\n')[14],
            }
            return datos_factura

    @staticmethod
    def extraer_numero(cadena):
        patron = r'\b\d+\b'
        match = re.search(patron, cadena)
        return match.group() if match else None

    @staticmethod
    def extract_date(text):
        pattern = r"\b\d{4}\.\d{2}\.\d{2}\b"
        match = re.search(pattern, text)
        return match.group() if match else None

    @staticmethod
    def extract_total(text):
        pattern = r"\b(\d+,\d+)\b"
        match = re.search(pattern, text)
        return match.group() if match else None
