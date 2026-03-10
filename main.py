import sys #para leer datos desde la entrada (stdin).
print(f"INGRESE VALORES: \n")
for line in sys.stdin: # se recorre cada linea que llega desde stdin y el programa seguira leyendo hasta llegar al fin del archivo.
    line = line.strip() #elimina espacios al inicio y al final de la linea.
    if line == "":
        print(0) #si la linea esta vacia o solo tiene espacios imprime 0 y continua a la siguiente linea.
        continue 
    elementos = line.split(",") #separamos los elementos por comas.
    suma = 0 
    for e in elementos: 
        e = e.strip() #elimina espacios antes y despues de cada valor.
        limpio = "" #limpia caracteres invalidos.
        for c in e:
            if c.isdigit() or c == "." or c == "-":
                limpio += c
            if limpio == "" or limpio == "-" or limpio == ".":
                numero = 0
            else:
                numero = float(limpio)
            numero = int(numero)  #truncar decimales        
            suma += numero #suma todos los valores

print(suma)