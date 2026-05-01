import re
from typing import Dict, List
from datetime import datetime
import csv

DEPARTAMENTOS_VALIDOS = ['VEN', 'ADM', 'TEC', 'LOG', 'RHH']
SERIES_VALIDAS = ['A', 'B', 'C', 'D', 'E']

def validar_producto(codigo: str) -> Dict:
    resultado = {
        "valido" : False,
        "categoria" : None,
        "numero" : None,
        "pais" : None,
    }

    patron = r'^([A-Z]{3})-(\d{4})-([A-Z]{2})$'
    match = re.match(patron, codigo)

    if match:
        resultado["valido"] = True
        resultado["categoria"] = match.group(1)
        resultado["numero"] = match.group(2)
        resultado["pais"] = match.group(3)

    return resultado

def validar_envio(codigo: str) -> Dict:
    resultado={
        "valido": False,
        "fecha": None,
        "secuencial": None

    }

    patron = r'^ENV-(202[0-9]|2030)-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-(\d{6})$'
    match = re.match(patron, codigo)

    if match:
        anio, mes, dia, sec = match.groups()

        try:
            datetime(int(anio), int(mes), int(dia))
        except:
            return resultado
        
        resultado["valido"] = True
        resultado["fecha"] = f"{anio}-{mes}-{dia}"
        resultado["secuencial"] = sec
    
    return resultado

def validar_empleado(codigo: str) -> Dict:
    resultado = {
        "valido" : False,
        "departamento" : None,
        "numero" : None

    }

    patron = r'^EMP-([A-Z]{3})-([1-9]\d{3})$'
    match = re.match(patron, codigo)

    if match:
        depto, num = match.groups()

        if depto in DEPARTAMENTOS_VALIDOS:
            resultado["valido"] = True
            resultado["departamento"] = depto
            resultado["numero"] = num

    return resultado

def validar_factura(codigo: str) -> Dict:
    resultado = {
        "valido" : False,
        "serie": None,
        "numero" : None
    }

    patron = r'FAC-([A-E])-(\d{6})$'
    match = re.match(patron, codigo)

    if match:
        serie, num = match.groups()

        if serie in SERIES_VALIDAS:
            resultado["valido"] = True
            resultado["serie"] = serie
            resultado["numero"] = num
    return resultado

def validar_codigo(codigo: str) -> Dict:
    resultado = {
        "codigo" : codigo,
        "tipo" : "desconocido",
        "valido" : False,
        "detalles" : {}
    }

    if codigo.startswith("ENV-"):
        resultado["tipo"] = "envio"
        res = validar_envio(codigo)

    elif codigo.startswith("EMP-"):
        resultado["tipo"] = "empleado"
        res = validar_empleado(codigo)

    elif codigo.startswith("FAC-"):
        resultado["tipo"] = "factura"
        res = validar_factura(codigo)

    elif re.match(r'^[A-Z]{3}-', codigo):
        resultado["tipo"] = "producto"
        res = validar_producto(codigo)
    
    else: 
        res = {"valido" : False}
    
    resultado["valido"] = res["valido"]

    if res["valido"]:
        detalles = res.copy()
        detalles.pop("valido")
        resultado["detalles"] = detalles
    
    return resultado

def procesar_lote(codigos: List[str]) -> Dict:
    resultado = {
        "total" : 0,
        "validos" : 0,
        "invalidos" : 0,
        "por_tipo" : {
            "producto" : {"total": 0, "validos": 0},
            "envio" : {"total": 0, "validos": 0},
            "empleado" : {"total": 0, "validos": 0},
            "factura" : {"total": 0, "validos": 0},
            "desconocido" : {"total": 0, "validos": 0} 
            
        },
        "detalle" : []
    }

    for codigo in codigos:
        res = validar_codigo(codigo)

        resultado["total"] += 1
        resultado["detalle"].append(res)

        tipo = res["tipo"]
        resultado["por_tipo"][tipo]["total"] += 1

        if res["valido"]:
            resultado["validos"] += 1
            resultado["por_tipo"][tipo]["validos"] += 1
        else: 
            resultado["invalidos"] += 1

    return resultado

def mostrar_resultado(resultado: Dict) -> None:
    estado = "✓" if resultado["valido"] else "✗"
    print(f"{estado} {resultado['codigo'] :<30} | Tipo: {resultado['tipo']:<12}")

    if resultado["valido"] and resultado["detalles"]:
        detalles = ", ".join(
            f"{k}: {v}" for k, v in resultado["detalles"].items() if v
        )
        print(f"   └── {detalles}")

def mostrar_reporte(reporte: Dict) -> None:
    print("=" * 60)
    print("                 REPORTE DE VALIDACION")
    print("=" * 60)

    print(f"\n Total procesados: {reporte['total']}")
    print(f"Validos: {reporte['validos']} ({reporte['validos']/reporte['total'] * 100:.1f}%)")
    print(f"Invalidos: {reporte['invalidos']} ({reporte['invalidos']/reporte['total'] * 100:.1f}%)")

    print("\n Desglose por tipo:")
    print("-" * 40)

    for tipo, stats in reporte["por_tipo"].items():
        if stats["total"] > 0:
            tasa = stats["validos"] / stats["total"] * 100
            print(f"   {tipo.capitalize():<12}: {stats['validos']:>3}/{stats['total']:<3} ({tasa:.0f}% validos)")

    print("\n" + "=" * 60)


def sugerir_correccion(codigo: str) -> str:
    return codigo.upper()

def validar_fecha_real(anio: int, mes: int, dia: int) -> bool:
    try: 
        datetime(anio, mes, dia)
        return True
    except:
        return False
    
def exportar_resultados(reporte: Dict, archivo: str) -> None:
    with open(archivo, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["codigo", "tipo", "valido", "detalles"])

        for item in reporte["detalle"]:
            writer.writerow([
                item["codigo"],
                item["tipo"],
                item["valido"],
                str(item["detalles"])
            ])


if __name__ == "__main__":

    CODIGOS_PRUEBA = [
    # Productos
    "TEC-0001-MX",
    "ALI-9999-US",
    "ROB-1234-CA",
    "tec-0001-MX",
    "TEC-001-MX",
    "TECH-0001-MX",

    # Envíos
    "ENV-2024-03-15-001234",
    "ENV-2025-12-01-999999",
    "ENV-2019-03-15-001234",
    "ENV-2024-13-15-001234",
    "ENV-2024-03-32-001234",

    # Empleados
    "EMP-VEN-1234",
    "EMP-TEC-9999",
    "EMP-ADM-1000",
    "EMP-VEN-0123",
    "EMP-XXX-1234",
    "EMP-VEN-123",

    # Facturas
    "FAC-A-123456",
    "FAC-E-000001",
    "FAC-B-999999",
    "FAC-F-123456",
    "FAC-A-12345",
    "FAC-a-123456",

    # Desconocidos
    "XXX-1234",
    "RANDOM-CODE"
]
    print(len(CODIGOS_PRUEBA))

    reporte = procesar_lote(CODIGOS_PRUEBA)
    mostrar_reporte(reporte)
    exportar_resultados(reporte, "resultados.csv")
    