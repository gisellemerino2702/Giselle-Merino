from models.producto import Producto
from utils.validators import validar_producto
from utils.io import leer_inventario, escribir_reporte

ARCHIVO_INVENTARIO = "data/inventario.csv"
ARCHIVO_REPORTE = "outputs/reporte_inventario.csv"

def crear_productos(datos_raw):
    productos = []
    skus_vistos = set()

    for d in datos_raw:

        if d.get("sku") in skus_vistos:
            continue

        valido, error = validar_producto(
            d.get("sku"),
            d.get("nombre"),
            d.get("categoria"),
            d.get("precio"),
            d.get("stock"),
            d.get("stock_minimo"),
        )

        if not valido:
            print(f"[IGNORADO] {error}")
            continue

        producto = Producto(
            d["sku"],
            d["nombre"],
            d["categoria"],
            float(d["precio"]),
            int(d["stock"]),
            int(d["stock_minimo"]),
        )

        productos.append(producto)
        skus_vistos.add(d["sku"])

    return productos

def filtrar_reorden(productos):
    return[p for p in productos if p.necesita_reorden()]

def ordenar(productos):
    return sorted(
        productos, 
        key=lambda p: p.unidades_faltantes(), 
        reverse=True
    )

def main():
    print("=====SISTEMA DE INVENTARIO=====")

    datos = leer_inventario(ARCHIVO_INVENTARIO)
    print(f"Leidos: {len(datos)} registros")

    productos = crear_productos(datos)
    print(f"Validos: {len(productos)}")

    reorden = filtrar_reorden(productos)
    print(f"Necesitan reorden: {len(reorden)}")

    reorden = ordenar(reorden)

    print("\n ---- REPORTE ----")
    for p in reorden:
        print(p)
    
    escribir_reporte(reorden, ARCHIVO_REPORTE)

    print("\nReporte generado correctamente")


if __name__ == "__main__":
    main()

