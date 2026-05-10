import argparse
import sys
import os

def es_valor_nulo(valor):
    if valor is None:
        return True
    if isinstance(valor, str) and valor.strip() == "":
        return True
    return False

def es_numerico(valor):
    try:
        float(str(valor).replace(',', '').strip())
        return True
    except (ValueError, TypeError):
        return False
    
def es_fecha(valor):
    v = str(valor).strip()

    if len(v) >= 10 and v[4] == '-' and v[7] == '-':
        try:
            partes = v[:10].split('-')
            anio = int(partes[0])
            mes = int(partes[1])
            dia = int(partes[2])
            return  1900 <= anio <= 2100 and 1 <= mes <= 12 and 1 <= dia <= 31
        except (ValueError, IndexError):
            return False
    return False

def es_booleano(valor):
    v = str(valor).strip().lower()
    return v in [
        'true', 'false', 
        'yes', 'no',
        'si',
        '1', '0',
        't', 'f'
    ]

def inferir_tipo(valores):
    valores_validos = [v for v in valores if not es_valor_nulo(v)]

    if not valores_validos:
        return "texto"
    
    total = len(valores_validos)
    umbral = 0.8 

    num_fechas = sum(1 for v in valores_validos if es_fecha(v))
    num_booleanos = sum(1 for v in valores_validos if es_booleano(v))
    num_numericos = sum(1 for v in valores_validos if es_numerico(v))

    if num_fechas / total >= umbral:
        return "fecha"
    elif num_booleanos / total >= umbral:
        return "booleano"
    elif num_numericos / total >= umbral:
        return "numerico"
    else:
        return "texto"
    
def perfilar_columna(nombre, valores):
    total = len(valores)
    nulos = sum(1 for v in valores if not es_valor_nulo(v))

    valores_no_nulos = [
        v for v in valores
        if not es_valor_nulo(v)
    ]

    unicos = len(set(valores_no_nulos))
    ejemplo = valores_no_nulos[0] if valores_no_nulos else ""

    tipo = inferir_tipo(valores)

    porcentaje_nulos = (
        round((nulos / total) * 100, 2) 
        if total > 0 else 0.00
    )
    porcentaje_unicos = (
        round((unicos / total) * 100, 2) 
        if total > 0 else 0.00
    )
    return{
        "nombre_columna" : nombre,
        "tipo_inferido" : tipo,
        "total_registros" : total,
        "valores_nulos" :nulos,
        "porcentaje_nulos" : porcentaje_nulos,
        "valores_unicos" : unicos,
        "porcentaje_unicos" : porcentaje_unicos,
        "ejemplo_valor" : ejemplo
    }

def leer_csv(ruta):
    try: 
        with open(ruta, 'r', encoding= 'utf-8') as f:
            lineas = f.readlines()
    except FileNotFoundError:
        print(f"Error: No se encontro el archivo {ruta}")
        sys.exit(1)

    if not lineas:
        return [], []
    
    encabezados = lineas[0].strip().split(',')

    filas = []
    for linea in lineas[1:]:
        if linea.strip():
            filas.append(linea.strip().split(','))
    return encabezados, filas

def escribir_csv(ruta, perfiles):
    columnas = [
        "nombre_columna", "tipo_inferido", "total_registros",
        "valores_nulos", "porcentaje_nulos", "valores_unicos",
        "porcentaje_unicos", "ejemplo_valor"
    ]

    with open(ruta, 'w', encoding= 'utf-8') as f:
        f.write(','.join(columnas) + '\n')

        for p in perfiles:
            fila = [
                str(p["nombre_columna"]),
                str(p["tipo_inferido"]),
                str(p["total_registros"]),
                str(p["valores_nulos"]),
                f"{p['porcentaje_nulos']:.2f}",
                str(p["valores_unicos"]),
                f"{p['porcentaje_unicos']:.2f}",
                str(p["ejemplo_valor"]),
            ]
            f.write(','.join(fila) + '\n')

def main():
    parser = argparse.ArgumentParser(description="perfilador de csv")
    parser.add_argument("--input", "-i", required=True)
    parser.add_argument("--output", "-o", required=True)

    args = parser.parse_args()

    print(f"Perfilando archivo: {args.input}")

    encabezados, filas = leer_csv(args.input)

    if not encabezados:
        print("Error: archivo vacio")
        sys.exit(1)

    print(f"Columnas: {len(encabezados)}")
    print(f"Registros: {len(filas)}")

    perfiles = []

    for i, col in enumerate(encabezados):
        valores = [fila[i] if i < len(fila) else "" for fila in filas]
        perfiles.append(perfilar_columna(col, valores))
    
    os.makedirs(os.path.dirname(args.output), exist_ok=True)

    escribir_csv(args.output, perfiles)

    print(f"Perfil generado en: {args.output}")
    print("PROCESO COMPLETO")

if __name__ == "__main__":
    main() 