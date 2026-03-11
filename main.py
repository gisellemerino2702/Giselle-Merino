import sys #para leer datos desde la entrada (stdin).
import re #limpiar caracteres invalidos.
def sacar_num(texto):
    texto = texto.strip()
    limpio = re.sub(r"[^0-9\.-]", "", texto)
    if limpio == "" or limpio == "-" or limpio == ".":
        return 0
    
    try:
        return int(float(limpio))
    except: 
        return 0
    
def total(linea):
    linea = linea.strip()
    if linea == "":
        return 0
    parte = linea.split(",")
    tot = 0
    for p in parte:
        valor = sacar_num(p)
        tot += valor
    return tot

def final(*args):
    for lineas in sys.stdin:
        resultado = total(lineas)
        print(f"Resultados: {resultado}")

if __name__ == "__main__":
    print(f"INGRESE LOS VALORES SEPARADOS POR COMAS: \n")
    final()