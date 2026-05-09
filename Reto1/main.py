import sys #para leer datos desde la entrada (stdin).
import re #limpiar caracteres invalidos.
def sacar_num(texto):
    texto = texto.strip()
    limpio = re.sub(r"[^0-9\.-]", "", texto)
    
    return limpio
    
def total(linea):
    linea = linea.strip()
    if linea == "":
        return 0
    parte = linea.split(",")
    tot = 0
    for p in parte:
        valor = sacar_num(p)
        if valor == "":
            continue
        try:
            numero = float(valor)
            tot += int(numero)

        except ValueError:
            continue

    return tot

def final():
    for lineas in sys.stdin:
        lineas = lineas.strip()
        resultado = total(lineas)
        print(resultado)

if __name__ == "__main__":
    final()
    