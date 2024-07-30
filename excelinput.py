import os
import csv
from openpyxl import load_workbook

def main():
    # Ruta de la carpeta que contiene los archivos CSV
    csv_folder_path = os.path.join(os.getcwd(), 'files/ecovidrio/csv')

    # Obtener la lista de archivos CSV en la carpeta
    csv_files = [f for f in os.listdir(csv_folder_path) if f.endswith('.csv')]
    print(f"Archivos CSV encontrados: {csv_files}")  # Comprobación de archivos CSV

    # Ruta del archivo Excel predefinido
    excel_file_path = os.path.join(os.getcwd(), 'files/ecovidrio/excel/FDE_Ventas_2023 Plantilla2.xlsm')

    # Cargar el archivo Excel existente
    workbook = load_workbook(excel_file_path, keep_vba=True)
    sheet = workbook.active

    # Variable de control para la celda
    initial_row = 6  # Comienza en la fila 6

    # Recorrer los archivos CSV
    for csv_file in csv_files:
        # Leer el contenido del archivo CSV
        csv_file_path = os.path.join(csv_folder_path, csv_file)
        print(f"Leyendo archivo CSV: {csv_file_path}")  # Comprobación al leer archivo
        with open(csv_file_path, 'r', encoding='latin-1') as file:
            reader = csv.DictReader(file, delimiter=';')
            data = [row for row in reader]
            print(f"Datos leídos del archivo {csv_file}: {data}")  # Comprobación de datos leídos

            # Realizar las asignaciones correspondientes
            initial_row = assign_answer_to_excel(sheet, data, initial_row)

    # Guardar el archivo Excel modificado
    workbook.save(excel_file_path)

def assign_answer_to_excel(sheet, data, initial_row):
    print(f"Asignando datos al Excel a partir de la fila {initial_row}")  # Comprobación de entrada a la función
    # Definir las variables de los campos del archivo CSV en la columna que corresponde al Excel
    cell_mapping = {
        'A': 'Codigo_UV',
        'B': 'Desc_UV',
        # Añade aquí más mapeos según necesites
    }

    # Asignar los valores del archivo CSV a las celdas correspondientes
    for i, row in enumerate(data):
        print(f"Procesando fila {i + initial_row}: {row}")  # Comprobación dentro del bucle
        for column, field in cell_mapping.items():
            cell = f"{column}{initial_row + i}"
            value = row.get(field, '')
            print(f"Asignando valor {value} a la celda {cell}")  # Comprobación de asignación
            sheet[cell] = value

    return initial_row + len(data)

if __name__ == "__main__":
    main()
