import sys #para leer datos desde la entrada (stdin).
import re #limpiar caracteres invalidos.
print(f"INGRESE LOS VALORES SEPARADOS POR COMAS: \n")
def sacar_num(texto):
    texto = texto.strip()
    limpio = re.sub(r"[^0-9\.-]", "", texto)
    if limpio == "" or limpio == "-" or limpio == ".":
        return 0
    
    try:
        int(float(limpio))
    except: 
        return 0
    
def total(linea):
    linea = linea.strip()
    if linea == "":
        return 0
    parte = linea.split(",")
    tot = 0
    for p in parte:
        tot += sacar_num(p)
    return tot

def final():
    for lineas in sys.stdin:
        resultado = total(lineas)
        print(resultado)

if __name__ == "main":
    final()