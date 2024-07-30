import os
import json
import csv
from io import StringIO
from openpyxl import load_workbook
import ipdb

def main():
    # Ruta de la carpeta que contiene los archivos JSON
    json_folder_path = os.path.join(os.getcwd(), 'files/ecovidrio/json')

    # Obtener la lista de archivos JSON en la carpeta
    json_files = [f for f in os.listdir(json_folder_path) if f.endswith('.json')]

    # Ruta del archivo Excel predefinido
    excel_file_path = os.path.join(os.getcwd(), 'files/ecovidrio/excel/FDE_Ventas_2023 Plantilla2.xlsm')

    # Cargar el archivo Excel existente
    workbook = load_workbook(excel_file_path, keep_vba=True)
    sheet = workbook.active

    # Variable de control para la celda
    initial_row = 6  # Comienza en la fila 6

    # Recorrer los archivos JSON
    for json_file in json_files:
        # Leer el contenido del archivo JSON
        json_file_path = os.path.join(json_folder_path, json_file)
        with open(json_file_path, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                continue  # Saltar a la siguiente iteración si falla la decodificación

            # Extraer la información de "SmartEscrow OCR" basado en la estructura real
            ipdb.set_trace()  # Añadir punto de interrupción aquí para inspeccionar `data`
            processes = data.get("processes", {})
            smart_escrow_ocr = processes.get("SmartEscrow OCR", {})
            result = smart_escrow_ocr.get("result", {})
            ocr_result = result.get("answer", "")

            if ocr_result:
                # Procesar el contenido de "answer"
                csv_data = StringIO(ocr_result)
                reader = csv.DictReader(csv_data, delimiter=';')
                data = [row for row in reader]

                # Realizar las asignaciones correspondientes
                initial_row = assign_answer_to_excel(sheet, data, initial_row)

    # Guardar el archivo Excel modificado
    workbook.save(excel_file_path)

def assign_answer_to_excel(sheet, data, initial_row):
    # Definir las variables de los campos del archivo CSV en la columna que corresponde al Excel
    cell_mapping = {
        'A': 'Codigo_UV',
        'B': 'Desc_UV',
        # Añade aquí más mapeos según necesites
    }

    # Asignar los valores del archivo CSV a las celdas correspondientes
    for i, row in enumerate(data):
        for column, field in cell_mapping.items():
            cell = f"{column}{initial_row + i}"
            value = row.get(field, '')
            sheet[cell] = value

    return initial_row + len(data)

if __name__ == "__main__":
    main()
