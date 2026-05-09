# Clasificador de Temperaturas

Este programa en Python lee datos de temperaturas desde la entrada estándar (`stdin`), convierte temperaturas en Fahrenheit a Celsius y clasifica cada ciudad según su temperatura.

## Funcionalidades

- Conversión de Fahrenheit a Celsius
- Clasificación automática de temperaturas
- Validación de datos inválidos
- Ignora líneas incorrectas
- Lectura de múltiples registros desde entrada estándar

---

## Clasificación de temperaturas

| Rango en Celsius | Clasificación |
|---|---|
| Menor a 0°C | Congelante |
| 0°C a 15°C | Frio |
| 16°C a 25°C | Templado |
| 26°C a 35°C | Calido |
| Mayor a 35°C | Extremo |

---

## Formato de entrada

El programa espera datos CSV con el siguiente formato:

```txt
ciudad,temperatura,unidad
CDMX,22,C
Nueva York,50,F
Moscu,-10,C
Miami,95,F
```

---

## Ejemplo de salida

```txt
ciudad,temperatura_celsius,clasificacion
CDMX,22.0,Templado
Nueva York,10.0,Frio
Moscu,-10.0,Congelante
Miami,35.0,Calido
```

---