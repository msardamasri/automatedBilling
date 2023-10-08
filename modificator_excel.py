from openpyxl import load_workbook
from datetime import datetime
import re


class ModificatorExcel:

    @staticmethod
    def obtener_fecha_actual():
        fecha_actual = datetime.now()
        fecha_formateada = fecha_actual.strftime('%d/%m/%Y')
        return fecha_formateada

    @staticmethod
    def obtener_desde_y_a_partir(cadena):
        desde_match = re.search(r'Desde:(.*)A:', cadena)
        a_partir_match = re.search(r'A:(.*)', cadena)
        desde = desde_match.group(1).strip() if desde_match else None
        a_partir = a_partir_match.group(1).strip() if a_partir_match else None
        return desde, a_partir

    @staticmethod
    def modify_template_with_data(template_path, data, numero):
        libro_excel = load_workbook(filename=template_path)
        hoja = libro_excel.active
        # data
        input_date_string = data['Fecha_servicio']
        year, month, day = input_date_string.split('.')
        formatted_date = f"{day}/{month}/{year}"
        hoja['A17'] = formatted_date
        # diners
        hoja['H36'] = data['Total']
        # referencia
        hoja['B17'] = data['Referencia']
        # direccion servicio
        desde, a_partir = ModificatorExcel.obtener_desde_y_a_partir(
            data['Direccion_servicio'])
        hoja['C16'] = desde
        hoja['C17'] = a_partir
        # referencia autofacturacion
        hoja['B16'] = data['Autofacturacion']
        # data actual
        fecha_actual = ModificatorExcel.obtener_fecha_actual()
        hoja['B12'] = fecha_actual
        # numero de factura
        hoja['B11'] = numero
        return libro_excel
