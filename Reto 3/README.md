# Analizador de Ventas

Programa en Python que lee transacciones de ventas desde la entrada estándar (`stdin`), agrupa la información por producto y genera un reporte consolidado ordenado por ingreso total.

---

## Funcionalidades

- Lectura de datos CSV desde `stdin`
- Agrupación de ventas por producto
- Cálculo de:
  - Unidades vendidas
  - Ingreso total
  - Precio promedio
- Ordenamiento descendente por ingreso total
- Manejo de líneas inválidas
- Salida en formato CSV

---

## Formato de Entrada

El programa espera un archivo CSV con el siguiente formato:

```txt
fecha,producto,cantidad,precio_unitario
2026-01-01,Laptop,2,15000.00
2026-01-02,Mouse,10,250.00
2026-01-03,Laptop,1,14500.00