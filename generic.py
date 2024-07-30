import json
import pandas as pd

# Ruta del archivo JSON
json_file_path = r"C:\Users\soled\Desktop\Ecovidrio\files\DNI.json"

# Leer el archivo JSON
with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Función para aplanar el JSON y manejar listas anidadas
def flatten_json(y, prefix=''):
    out = {}
    if isinstance(y, dict):
        for k, v in y.items():
            out.update(flatten_json(v, prefix + k + '_'))
    elif isinstance(y, list):
        for i, v in enumerate(y):
            out.update(flatten_json(v, prefix + str(i) + '_'))
    else:
        out[prefix[:-1]] = y
    return out

# Extraer las variables desde extractedVariables
extracted_variables = data['verificators']['FinalSummary']['result']['answer']['extractedVariables']

# Aplanar el JSON
flattened_data = flatten_json(extracted_variables)

# Convertir el diccionario a un DataFrame
df_temp = pd.DataFrame([flattened_data])

# Transponer el DataFrame para que las variables sean columnas
df = df_temp.T.reset_index()
df.columns = ['Variable', 'Valor']

# Separar las columnas por guion bajo '_'
split_columns = df['Variable'].str.split('_', expand=True)
split_columns['Valor'] = df['Valor']

# Eliminar las columnas innecesarias
split_columns = split_columns.drop(columns=[0, 1])

# Guardar el DataFrame en un archivo Excel
excel_path = r"C:\Users\soled\Desktop\Ecovidrio\files\finalSummaryDownloadDNI.xlsx"
split_columns.to_excel(excel_path, index=False)

print(f"Excel file created at {excel_path}")
