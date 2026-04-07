DESCRIPCION:

Sistema que genera reportes de productos que necesitan reorden apartir de un archivo csv.
El sistema:
-Valida los datos
-Ignora registros incorrectos
-Detecta productos con stock bajo
-Genera reporte de reorden

ESTRUCTURA DEL PROYECTO:

reto-semana-04/
├── main.py
├── README.md
├── .gitignore
├── models/
│   ├── __init__.py
│   └── producto.py
├── utils/
│   ├── __init__.py
│   ├── io.py
│   └── validators.py
├── data/
│   └── inventario.csv
└── outputs/
    └── reporte_inventario.csv


COMO EJECUTAR: 

py main.py

ENTRADA:

data/inventario.csv

csv:
sku,nombre,categoria,precio,stock,stock_minimo
SKU101,Tablet Samsung,Electronica,8000.00,4,10
SKU102,Cargador USB,Cables,250.00,2,20
SKU103,Bocina Bluetooth,Audio,N/A,15,10
SKU104,Disco Duro Externo,Almacenamiento,1500.00,xyz,5
SKU105,Smartwatch Xiaomi,Wearables,3000.00,1,???
SKU106,Camara Web Pro,Video
SKU107,Memoria USB 64GB,Almacenamiento,200.00,0,10,extra


SALIDA:

Archivo: outputs/reporte_inventario.csv

csv:
sku,nombre,categoria,stock_actual,stock_minimo,unidades_faltantes,valor_inventario
SKU102,Cargador USB,Cables,2,20,18,500.00
SKU101,Tablet Samsung,Electronica,4,10,6,32000.00

AUTOR: 

Gladys Giselle Merino Galindo

FECHA DE ENTREGA:

Viernes de la semana 4, 23:59 hrs



