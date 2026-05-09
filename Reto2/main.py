import sys

def fahrenheit_a_celsius(f):
    """Convierte fahrenheit a celsius"""
    return (f - 32) * 5/9
 
def clasificar_temperatura(celsius):
    """Clasifica las temperaturas segun rangos definidos"""
    if celsius < 0:
        return "Congelado"
    elif celsius <= 15:
        return "Frio"
    elif celsius <= 25:
        return "Templado"
    elif celsius <= 35:
        return "Calido"
    else:
        return "Extremo"
    
def main():
    lineas = sys.stdin.read().strip().split("\n")

    print("ciudad,temperatura_celsius,clasificacion")

    for linea in lineas [1:]:
        partes = linea.split(",")

        if len(partes) != 3:
            continue
        ciudad, temp_str, unidad = partes

        ciudad = ciudad.strip()
        temp_str = temp_str.strip()
        unidad = unidad.strip().upper()

        try:
            temperatura = float(temp_str) 
        except ValueError: 
            continue

        if unidad not in ["C", "F"]:
            continue

        if unidad == "F":
            temperatura = fahrenheit_a_celsius(temperatura)

        clasificacion = clasificar_temperatura(temperatura)

        print(f"{ciudad},{temperatura:.1f},{clasificacion}")

if __name__ == "__main__":
    main() 
