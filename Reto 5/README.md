PERFILADOR DE DATASETS

Herramienta en python que analiza cualquier archivo CSV y genera un reporte automatico de calidad de datos.

REQUISITOS:

Python 3.8 o superior

INSTALACION:

1. Clonar repositorio
git clone https://github.com/gisellemerino2702/Giselle-Merino.git 

cd reto 5

2. Crear ambiente virtual

python -m venv .venv

3. Activar ambiente virtual

# Windows
 .venv\Scripts\activate 
# Linux/Mac 
  source .venv/bin/activate

4. Instalar dependencias

pip install -r requirements.txt


EJECUTAR:

py main.py --input <archivo_entrada.csv> --output <archivo_salida.csv>

EEJEMPLO:

python main.py --input data/ventas.csv --output outputs/perfil_ventas.csv

FORMATO DE SALIDA:

El perfil generado contiene las siguientes columnas:

Columna	               Descripcion
nombre_columna	       Nombre de la columna
tipo_inferido	       Tipo detectado (numerico/texto/fecha/booleano)
total_registros        Total de filas
valores_nulos	       Cantidad de valores vacios
porcentaje_nulos       Porcentaje de nulos
valores_unicos	       Cantidad de valores distintos
porcentaje_unicos	   Porcentaje de unicidad
ejemplo_valor	       Primer valor no nulo

ENTRADA: 

Archivo: data/ventas.csv

csv:
fecha,producto,cantidad,precio,vendedor
2026-01-01,Laptop,2,15000.00,Ana
2026-01-02,Mouse,10,250.00,Bob
2026-01-03,Teclado,,800.00,Ana
2026-01-04,Monitor,3,,Carlos
2026-01-05,Laptop,1,15000.00,

SALIDA:

Archivo: outputs/perfil_ventas.csv

csv:
nombre_columna,tipo_inferido,total_registros,valores_nulos,porcentaje_nulos,valores_unicos,porcentaje_unicos,ejemplo_valor
fecha,fecha,5,0,0.00,5,100.00,2026-01-01
producto,texto,5,0,0.00,4,80.00,Laptop
cantidad,numerico,5,1,20.00,4,80.00,2
precio,numerico,5,1,20.00,3,60.00,15000.00
vendedor,texto,5,1,20.00,3,60.00,Ana

AUTOR:

Gladys Giselle Merino Galindo - Abril 2026
