import sys 
def main():
    productos = {}

    primera_linea = True
    for linea in sys.stdin:
        linea = linea.strip()

        if primera_linea:
            primera_linea = False
            continue

        if not linea:
            continue

        partes = linea.split(',')

        if len(partes) != 4:
            continue

        fecha, producto, cantidad_str, precio_str = partes

        try:
            cantidad = int(cantidad_str)
            precio = float(precio_str)
        except ValueError:
            continue

        if producto not in productos:
            productos[producto] = {
                "Unidades" : 0,
                "Ingreso" : 0.0
            } 
        
        productos[producto]["Unidades"] += cantidad
        productos[producto]["Ingreso"] += cantidad * precio

    for producto in productos:

        unidades = productos[producto]["Unidades"]
        ingreso = productos[producto]["Ingreso"]

        if unidades > 0:
            promedio = ingreso / unidades
        else:
            promedio = 0
            
        productos[producto]["promedio"] = promedio
    
    lista_ordenada = sorted(
        productos.items(),
        key=lambda x: x[1]["Ingreso"],
        reverse=True
    )

    print("Producto, Vendido, Total_ingresado, Promedio")

    for nombre, datos in lista_ordenada:

        unidades = datos["Unidades"]
        unidades = datos["Ingreso"]
        promedio = datos["promedio"]

        print(f"{nombre},{unidades},{ingreso:.2f},{promedio:.2f}")

if __name__ == "__main__":
    main()