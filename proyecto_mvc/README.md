# App MVC — 40 Ejercicios de Clases y Colecciones (Python)

Aplicación de consola que organiza en **MVC (Modelo-Vista-Controlador)** las 41
clases: el ejercicio modelo + 20 ejercicios (1-20) + 20 ejercicios adicionales
(21-40) con la misma dificultad y estilo.

## Integrantes del grupo
- (completar nombre — rol/aporte)
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
│   ├── gestion.py              # Ej. 3, 10, 11, 19
│   └── ejercicios_adicionales.py    # Ej. 21-40 (todos juntos aquí)
├── views/
│   └── console_view.py         # VISTA: toda la entrada/salida de consola
└── controllers/
    └── app_controller.py       # CONTROLADOR: conecta Vista y Modelos
```

## Lista de ejercicios

| # | Clase | Descripción |
|---|---|---|
| 0 | `NumeroPrimo` | Números primos con historial (modelo de la guía) |
| 1 | `ValidadorPuntajes` | Valida puntajes de 0 a 10 y calcula promedio |
| 2 | `DetectorDuplicados` | Detecta palabras repetidas con conjuntos |
| 3 | `GestorCuentas` | Cuentas bancarias: depositar, retirar, saldo total |
| 4 | `RotadorSecuencia` | Rota una lista hacia la izquierda |
| 5 | `ClasificadorSigno` | Separa positivos, negativos y ceros |
| 6 | `GestorVentas` | Estadísticas de ventas diarias |
| 7 | `GestorAlturas` | Mapea personas a alturas |
| 8 | `Aulas` | Asigna estudiantes a aulas |
| 9 | `ClasificadorCaracteres` | Cuenta mayúsculas, minúsculas, dígitos, espacios y símbolos |
| 10 | `Agenda` | Citas como tuplas (fecha, descripción) |
| 11 | `UrnaVotos` | Conteo de votos y ganador |
| 12 | `GeneradorTablas` | Tablas de multiplicar con tuplas |
| 13 | `DivisorBloques` | Divide listas en bloques de tamaño fijo |
| 14 | `RegistroPeliculas` | Mapea películas a puntuación |
| 15 | `Factorizador` | Factores primos, MCD y MCM |
| 16 | `CodificadorNumerico` | Codifica letras como números (a=1 ... z=26) |
| 17 | `AgrupadorSalarios` | Agrupa salarios en bajo / medio / alto |
| 18 | `CalculadorPerimetro` | Perímetro de polígonos con puntos 2D |
| 19 | `Biblioteca` | Libros con préstamos y devoluciones |
| 20 | `AnalizadorFrases` | Palabras por sufijo y agrupadas por inicial |
| 21 | `CalculadoraIVA` | IVA y precio final con historial |
| 22 | `SumadorSerie` | Suma hasta n, suma de pares y de cuadrados |
| 23 | `GeneradorPotencias` | Potencias de una base y verificación |
| 24 | `CalculadoraArea` | Áreas de rectángulo, triángulo y círculo |
| 25 | `VerificadorBisiesto` | Años bisiestos y días del año |
| 26 | `ContadorLetras` | Frecuencia de letras y la más común |
| 27 | `LimpiadorTexto` | Quita espacios extra y vocales |
| 28 | `GeneradorUsuarios` | Nombres de usuario únicos con conjuntos |
| 29 | `FormateadorNombres` | Capitaliza nombres y genera iniciales |
| 30 | `BuscadorPalabras` | Posiciones de una palabra en una frase |
| 31 | `RegistroClimas` | Temperaturas por ciudad y ciudad más cálida |
| 32 | `GestorDeudas` | Deudas, pagos y mayor deudor |
| 33 | `ClasificadorTriangulos` | Equilátero, isósceles, escaleno o no válido |
| 34 | `ConversorRomanos` | Enteros a romanos y viceversa |
| 35 | `GestorAmigos` | Amistades y amigos en común (conjuntos) |
| 36 | `GestorAsientos` | Asientos (fila, número) sin repetir |
| 37 | `TablaPuntos` | Tabla de posiciones de un torneo |
| 38 | `OperadorMatrices` | Suma de filas, diagonal y transpuesta |
| 39 | `ConversorTiempo` | Segundos a h:m:s y suma de tiempos |
| 40 | `ListaInvitados` | Invitados, confirmaciones y pendientes |

## Cómo se aplicó MVC

- **Modelo** (`/models`): cada clase tiene su constructor, atributos, métodos que
  reutilizan otros métodos (con `*args`) y las colecciones pedidas: listas,
  tuplas, diccionarios y conjuntos. No hacen `print()` ni `input()`.
- **Vista** (`views/console_view.py`): solo muestra menús y resultados, y
  recoge la opción del usuario. No decide nada ni conoce las clases del modelo.
- **Controlador** (`controllers/app_controller.py`): arma el menú, recibe la
  opción elegida en la Vista, instancia el Modelo correspondiente, ejecuta sus
  métodos con datos de ejemplo y le pasa el resultado a la Vista para
  mostrarlo. Es el único que conoce tanto a Modelo como a Vista.

## Ejecutar

```bash
python3 main.py
```

Se muestra un menú del 0 al 40; cada opción ejecuta la demo de ese ejercicio
con datos de ejemplo y muestra entrada/salida.
