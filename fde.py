import os
import json
from openpyxl import load_workbook

def main():
    # Ruta de la carpeta que contiene los archivos JSON
    json_folder_path = os.path.join(os.getcwd(), 'files/prueba')

    # Obtener la lista de archivos JSON en la carpeta
    json_files = [f for f in os.listdir(json_folder_path) if f.endswith('.json')]

    # Ruta del archivo Excel predefinido
    excel_file_path = os.path.join(os.getcwd(), 'files/prueba/FDE_Ventas_2023 Plantilla_Final.xlsm')

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
        'Q': 'N\u00fam de UD',
        'R': 'Volumen del envase (ml)',
        'S': 'Peso Unitario (kg)',
        'V': 'N\u00fam Total',
        'W': 'Import.',
        'X': 'Export.'
    }

    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                # Asegurarse de que todos los valores sean listas
                filtered_answer = {}
                for k, v in item.items():
                    if v is not None:
                        if not isinstance(v, list):
                            filtered_answer[k] = [v]
                        else:
                            filtered_answer[k] = v

                # Encontrar la longitud máxima de las listas en filtered_answer
                max_length = max(len(filtered_answer.get(field, [])) for field in cell_mapping.values())

                # Asignar los valores del archivo JSON a las celdas correspondientes
                for i in range(max_length):
                    for column, field in cell_mapping.items():
                        cell = f"{column}{initial_row + i}"
                        values = filtered_answer.get(field, [])
                        value = values[i] if i < len(values) else ''
                        sheet[cell] = value

                initial_row += max_length
            else:
                print("Error: El ítem en la lista no es un diccionario.")
                continue
    else:
        print("Error: 'data' no es una lista.")
    
    return initial_row


if __name__ == "__main__":
    main()