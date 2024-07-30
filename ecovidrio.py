import os
import json
from openpyxl import load_workbook

def main():
    # Ruta de la carpeta que contiene los archivos JSON
    json_folder_path = os.path.join(os.getcwd(), 'files/ecovidrio/json')

    # Obtener la lista de archivos JSON en la carpeta
    json_files = [f for f in os.listdir(json_folder_path) if f.endswith('.json')]

    # Ruta del archivo Excel predefinido
    excel_file_path = os.path.join(os.getcwd(), 'files/ecovidrio/excel/FDE_Ventas_2023 Plantilla.xlsm')

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

            # Realizar las asignaciones correspondientes
            initial_row = assign_answer_to_excel(sheet, data, initial_row)

    # Guardar el archivo Excel modificado
    workbook.save(excel_file_path)

def assign_answer_to_excel(sheet, data, initial_row):
    # Búsqueda de variables en ANSWER del model GPT4ose (gpt-4o-2024-05-13)
    answer = {}

    for result in data.get('result', []):
        if result.get('model') == 'GPT4ose (gpt-4o-2024-05-13)' and 'answer' in result:
            answer = result['answer']
            break

    # Definir las variables de los campos del archivo JSON en la columna que corresponde al Excel
    cell_mapping = {
        'A': 'Ref. Cliente',
        'B': 'Nombre Ref. Cliente',
        'C': 'Categoría',
        'D': 'Sector',
        'E': 'Sub-sector',
        'F': 'Bebida / No Bebida',
        'G': 'Tipo de envase según RPP',
        'H': 'COD elemento principal',
        'I': 'COD elemento',
        'J': 'Principal / Auxiliar',
        'K': 'Subtipo de Envase',
        'L': 'Multimaterial',
        'M': 'Material',
        'N': '% de material',
        'O': '% de reciclado',
        'P': 'Color',
        'Q': 'Nº de UD',
        'R': 'Volumen del envase (ml)',
        'S': 'Peso Unitario (kg)',
        'V': 'Nº Total',
        'W': 'Import.',
        'X': 'Export.'
    }

    # Encontrar la longitud máxima de las listas en answer
    max_length = max(len(answer.get(field, [])) for field in cell_mapping.values())

    # Asignar los valores del archivo JSON a las celdas correspondientes
    for i in range(max_length):
        for column, field in cell_mapping.items():
            cell = f"{column}{initial_row + i}"
            values = answer.get(field, [])
            value = values[i] if i < len(values) else ''
            sheet[cell] = value

    return initial_row + max_length

if __name__ == "__main__":
    main()