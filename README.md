# ExcelGenerator

Este proyecto contiene varios scripts en Python para generar archivos Excel a partir de diversas fuentes de datos como JSON, respuestas de IA y conectores de datos.

## Índice de Scripts

1. [conversorJsonToCsv.py](#conversorjsontocsvpy)
2. [ecovidrio.py](#ecovidriopy)
3. [excelinput.py](#excelinputpy)
4. [fde.py](#fdepy)
5. [generic.py](#genericpy)
6. [informe.py](#informepy)
7. [main.py](#mainpy)
8. [prueba312.py](#prueba312py)

## Detalles de los Scripts

---

### conversorJsonToCsv.py
Este script convierte archivos JSON a archivos CSV.

---

### ecovidrio.py
Este script realiza operaciones específicas para el proyecto Ecovidrio.

---

### excelinput.py
Este script maneja la entrada de datos desde archivos Excel.

---

### fde.py
Este script realiza operaciones relacionadas con FDE (por favor, proporciona más detalles específicos).

---

### generic.py
Este script contiene funciones genéricas utilizadas en varios otros scripts.

---

### informe.py
**Resumen del Script:**

**Copiar el archivo original:**
Se hace una copia del archivo `FDE_Ventas_2023_3.xlsm` para trabajar sobre ella y se guarda como `FDE_Ventas_2023_8.xlsm`.

**Leer los datos:**
Se leen los datos del archivo copiado y del archivo de ventas en DataFrames utilizando `pandas`.

**Preparar y combinar los datos:**
1. Se eliminan las primeras cuatro filas del archivo `FDE_Ventas_2023_8.xlsm` y se reinicia el índice.
2. Se establecen las columnas correctas utilizando la fila 4 como encabezados.
3. Se renombra la columna 'Ref. Cliente' a 'Ref.Cliente'.
4. Se renombra la columna 'Unnamed: 7' a 'imp' en el archivo de ventas.
5. Se aseguran de que las columnas 'Ref.Cliente' en ambos DataFrames se traten como cadenas.
6. Se combinan los DataFrames en la columna 'Ref.Cliente'.

**Calcular los valores:**
1. Se definen funciones condicionales para calcular los valores de 'Import', 'Nº total' y 'Export' en función de las unidades y la columna 'imp'.
2. Se aplican estas funciones para actualizar el DataFrame combinado.

**Escribir los datos en el archivo Excel:**
1. Se carga el archivo `FDE_Ventas_2023_8.xlsm` utilizando `openpyxl`.
2. Se actualizan las celdas correspondientes en las columnas V, W y X (22, 23, y 24 respectivamente) de la hoja 'FDE'.
3. Se guarda el archivo actualizado.

Este script permite combinar datos de dos fuentes, realizar cálculos específicos y actualizar una plantilla Excel manteniendo las macros intactas.

---

### main.py
Este script es el punto de entrada principal para la ejecución del proyecto.

---

### prueba312.py
Este script se utiliza para pruebas específicas relacionadas con un json individual de Ecovidrio.
