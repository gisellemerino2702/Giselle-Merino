# README

## Descripción

Este programa en Python procesa líneas de texto desde la entrada estándar (`stdin`), limpia caracteres inválidos de cada valor y realiza una suma de números enteros truncados.

El programa:

- Lee múltiples líneas de entrada
- Separa los valores usando comas
- Elimina caracteres no válidos
- Convierte los valores a números
- Trunca los decimales
- Suma los resultados
- Imprime el total por cada línea procesada

---

## Características

- Limpieza automática de caracteres inválidos
- Soporte para números negativos y decimales
- Procesamiento eficiente de grandes volúmenes de datos
- Manejo de líneas vacías
- Lectura desde `stdin`

---

## Estructura del programa

### `sacar_num(texto)`

Limpia un valor individual dejando únicamente:

- números
- punto decimal (`.`)
- signo negativo (`-`)

---

### `total(linea)`

Procesa una línea completa:

1. Divide por comas
2. Limpia cada valor
3. Convierte a número
4. Trunca decimales usando `int()`
5. Suma todos los valores

---

### `final()`

Lee línea por línea desde `stdin` y muestra el resultado correspondiente.

---

## Ejemplo de entrada

```text
10,20,30
5.9,2.1
abc10,-3.7
```

## Ejemplo de salida

```text
60
7
7
```

---

## Ejecución

Ejecutar el programa desde terminal:

```bash
python programa.py < entrada_completa.txt
```

---
