import pandas as pd
import json

# Cargar datos desde un archivo JSON
with open('C:/Users/soled/Desktop/Ecovidrio/files/conversores/312-final.json', 'r') as file:
    data = json.load(file)

# Crear un DataFrame a partir de los datos JSON
df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo CSV con punto y coma como separador
df.to_csv('C:/Users/soled/Desktop/Ecovidrio/files/conversores/312-final-pc.csv', sep=';', index=False)
