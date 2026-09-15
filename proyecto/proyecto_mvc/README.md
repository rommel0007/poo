# App MVC — 20 Ejercicios de Clases y Colecciones (Python)

Aplicación de consola que organiza en **MVC (Modelo-Vista-Controlador)** las 21
clases descritas en la guía (el ejercicio modelo + los 20 ejercicios propuestos).

## Integrantes del grupo
- Andry — (completar rol/aporte)
- (agregar los demás integrantes según lo indicado en la tarea)

## Estructura del proyecto

```
proyecto_mvc/
├── main.py                     # Punto de entrada, solo arranca el Controlador
├── models/                     # MODELO: lógica de negocio, sin print() ni input()
│   ├── numero_primo.py         # Ej. 0 (modelo de la guía)
│   ├── matematicas.py          # Ej. 5, 12, 15, 18
│   ├── texto.py                # Ej. 2, 4, 9, 13, 16, 20
│   ├── personas.py             # Ej. 1, 6, 7, 8, 14, 17
│   └── gestion.py              # Ej. 3, 10, 11, 19
├── views/
│   └── console_view.py         # VISTA: toda la entrada/salida de consola
└── controllers/
    └── app_controller.py       # CONTROLADOR: conecta Vista y Modelos
```

## Cómo se aplicó MVC

- **Modelo** (`/models`): cada clase de la guía vive aquí exactamente como fue
  especificada (constructor, atributos, métodos que reutilizan otros métodos
  con `*args`/`**kwargs`, y las colecciones pedidas: listas, tuplas,
  diccionarios, conjuntos). No hacen `print()` ni `input()`.
- **Vista** (`views/console_view.py`): solo muestra menús y resultados, y
  recoge la opción del usuario. No decide nada ni conoce las clases del modelo.
- **Controlador** (`controllers/app_controller.py`): arma el menú, recibe la
  opción elegida en la Vista, instancia el Modelo correspondiente, ejecuta sus
  métodos con los datos de ejemplo de la guía, y le pasa el resultado a la
  Vista para mostrarlo. Es el único que conoce tanto a Modelo como a Vista.

## Ejecutar

```bash
python3 main.py
```

Se muestra un menú del 0 al 20; cada opción ejecuta la demo de ese ejercicio
con los datos de ejemplo de la guía y muestra entrada/salida.

## Nota sobre dos discrepancias encontradas en la guía original

Al verificar los 20 ejercicios contra sus ejemplos, dos salidas esperadas en
el PDF/HTML de la guía no coinciden con el enunciado del propio ejercicio
(puede ser útil mencionarlo si preguntan cómo se validó el trabajo):

- **Ej. 19 (Inventario):** con `agregar_stock("pan",50)` y
  `restar_stock("pan",30)` quedan 20 unidades; con `productos_bajo_stock(15)`
  el resultado correcto es `[]` (20 no es menor a 15), no `["pan"]` como
  indica el ejemplo de la guía.
- **Ej. 20 (AnalizadorPatrones):** el diccionario de ejemplo de la guía tiene
  una clave `5` repetida (dict inválido). Agrupando "el gato está aquí" por
  longitud real da `{2: ['el'], 4: ['gato', 'está', 'aquí']}`.

El código implementa la lógica correcta según el enunciado de cada método,
no el ejemplo con error.
