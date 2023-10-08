from gestor_de_facturas import GestorDeFacturas

if __name__ == "__main__":
    input_folder = r'C:\Users\marcs\OneDrive\Escritorio\dir\projects\ParserGS\resources\facturas'
    output_folder = r'C:\Users\marcs\OneDrive\Escritorio\dir\projects\ParserGS\resources\parsed'
    template_folder = r'C:\Users\marcs\OneDrive\Escritorio\dir\projects\ParserGS\resources\template'

    gestor = GestorDeFacturas(input_folder, output_folder, template_folder)
    gestor.procesar_facturas()
