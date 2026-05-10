# Sistema de Inventario con Clase `Producto`

## Descripción

Este proyecto implementa una clase llamada `Producto` en Python para representar productos dentro de un inventario.

La clase permite:

- Registrar información básica de un producto.
- Verificar si necesita reabastecimiento.
- Calcular unidades faltantes.
- Obtener el valor total del inventario.
- Mostrar información legible del producto.

---

## Esctructura del proyecto

reto-semana-04/
├── main.py
├── README.md
├── .gitignore
├── models/
│   ├── __init__.py
│   └── producto.py
├── utils/
│   ├── __init__.py
│   ├── io.py
│   └── validators.py
├── data/
│   └── inventario.csv
└── outputs/
    └── reporte_inventario.csv

---    

## Estructura de la Clase

La clase `Producto` contiene los siguientes atributos:

| Atributo | Descripción |
|---|---|
| `sku` | Identificador único del producto |
| `nombre` | Nombre del producto |
| `categoria` | Categoría del producto |
| `precio` | Precio unitario |
| `stock` | Cantidad disponible |
| `stock_minimo` | Nivel mínimo permitido |

---

## Métodos

### `necesita_reorden()`

Verifica si el producto necesita reabastecimiento.

```python
producto.necesita_reorden()
```

Retorna:

- `True` si el stock es menor al mínimo.
- `False` en caso contrario.

---

### `unidades_faltantes()`

Calcula cuántas unidades faltan para alcanzar el stock mínimo.

```python
producto.unidades_faltantes()
```

---

### `valor_inventario()`

Calcula el valor total del inventario del producto.

```python
producto.valor_inventario()
```

Fórmula:

```python
precio * stock
```

---

### `__str__()`

Muestra información legible del producto.

Ejemplo:

```python
[OK] A001: Laptop - Stock: 15/10
```

o

```python
[REORDEN] A001: Laptop - Stock: 5/10
```

---

## Ejemplo de Uso

```python
producto = Producto(
    "A001",
    "Laptop",
    "Electrónica",
    15000.0,
    5,
    10
)

print(producto)

print(producto.necesita_reorden())
print(producto.unidades_faltantes())
print(producto.valor_inventario())
```

---

## Requisitos

- Python 3.x

---

## Autor

Proyecto desarrollado en Python para práctica de Programación Orientada a Objetos (POO).

