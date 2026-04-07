def leer_inventario(ruta_archivo):
    productos = []

    with open(ruta_archivo, 'r', encoding= 'utf-8') as f:
        lineas = f.readlines()

    if not lineas:
        return productos
    
    encabezados = lineas[0].strip().split(',')

    for linea in lineas[1:]:
        lineas = linea.strip()
        if not linea:
            continue

        valores = linea.split(',')

        #validar num. de columnas

        if len(valores) != len(encabezados):
            continue

        productos.append(dict(zip(encabezados, valores)))

    return productos

def escribir_reporte(productos, ruta_archivo):
    with open(ruta_archivo, 'w', encoding= 'utf-8') as f:

        f.write("sku,nombre,categoria,stock_actual,stock_minimo,unidades_faltantes,valor_inventario\n")

        for p in productos:
            linea = (
                f"{p.sku},{p.nombre},{p.categoria},"
                f"{p.stock},{p.stock_minimo},"
                f"{p.unidades_faltantes()},{p.valor_inventario():.2f}"
            )

            f.write(linea + "\n")