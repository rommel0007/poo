"""
practica.py - Ejercicios de la sección 14 de la guía.

Ejecutar con:  python practica.py
(Los ejercicios 1 al 3 son código suelto; los 4 al 7 se demuestran usando
 la clase Cliente de models.py; el 8 está en views.py y en el menú, opción 8.)
"""

from models import Cliente

ciudades = ["Quito", "Guayaquil", "Quito", "Cuenca", "Guayaquil"]

# ------------------------------------------------------------------
# EJERCICIO 1 · Quitar duplicados conservando el orden
# Idea: un SET para preguntar rápido "¿ya la vi?" y una LISTA para
# guardar el resultado en el orden en que aparecieron.
# ------------------------------------------------------------------
print("=== Ejercicio 1 ===")
vistas = set()      # conjunto de control
unicas = []         # lista de resultado (conserva el orden)
for ciudad in ciudades:
    if ciudad not in vistas:
        vistas.add(ciudad)
        unicas.append(ciudad)
print(unicas)       # ['Quito', 'Guayaquil', 'Cuenca']

# ------------------------------------------------------------------
# EJERCICIO 2 · Contar con un diccionario
# Idea: la ciudad es la clave y el valor es cuántas veces apareció.
# ------------------------------------------------------------------
print("\n=== Ejercicio 2 ===")
conteo = {}
for ciudad in ciudades:
    conteo[ciudad] = conteo.get(ciudad, 0) + 1   # si no existe, parte de 0
print(conteo)                                     # {'Quito': 2, 'Guayaquil': 2, 'Cuenca': 1}
print("Más repetida:", max(conteo, key=conteo.get))

# ------------------------------------------------------------------
# EJERCICIO 3 · Conjuntos en acción
# ------------------------------------------------------------------
print("\n=== Ejercicio 3 ===")
matematica = {"Ana", "Luis", "Sol", "Marco"}
ingles = {"Luis", "Marco", "Ruth"}

ambas = matematica & ingles          # INTERSECCIÓN: están en las dos
solo_mate = matematica - ingles      # DIFERENCIA: solo en la primera
total = len(matematica | ingles)     # UNIÓN: cuántas personas distintas
print("En las dos:", sorted(ambas))          # ['Luis', 'Marco']
print("Solo en la primera:", sorted(solo_mate))  # ['Ana', 'Sol']
print("Personas distintas:", total)          # 5

# ------------------------------------------------------------------
# EJERCICIO 4 · Propiedad calculada: Cliente.iniciales
# ------------------------------------------------------------------
print("\n=== Ejercicio 4 ===")
ana = Cliente(1, "Ana", "Pérez", "ana@x.com")
print(ana.iniciales)                 # 'A.P.'  (sin paréntesis)

# ------------------------------------------------------------------
# EJERCICIO 5 · Método estático: Cliente.es_telefono_valido
# Se usa SIN crear ningún cliente. También lo usa el setter de telefono.
# ------------------------------------------------------------------
print("\n=== Ejercicio 5 ===")
print(Cliente.es_telefono_valido(""))            # True  (vacío es válido)
print(Cliente.es_telefono_valido("0987654321"))  # True  (10 dígitos)
print(Cliente.es_telefono_valido("123"))         # False (muy corto)
print(Cliente.es_telefono_valido("09A8"))        # False (tiene letras)
try:
    ana.telefono = "123"             # el setter llama a es_telefono_valido
except ValueError as error:
    print("Setter rechazó el dato ->", error)

# ------------------------------------------------------------------
# EJERCICIO 6 · Método de clase (fábrica): Cliente.desde_texto
# Usa cls(...) y no Cliente(...): así funcionaría con una subclase.
# ------------------------------------------------------------------
print("\n=== Ejercicio 6 ===")
luis = Cliente.desde_texto("2, Luis, Mora, luis@x.com")
print(luis, "|", luis.iniciales)


class ClienteVIP(Cliente):
    """Subclase de prueba: demuestra por qué se usa cls y no Cliente."""


vip = ClienteVIP.desde_texto("3, Sol, Ruiz, sol@x.com")
print(type(vip).__name__)            # 'ClienteVIP' (con Cliente(...) sería 'Cliente')

# ------------------------------------------------------------------
# EJERCICIO 7 · Atributo de clase y método de clase: Cliente.resumen
# Habla de TODOS los clientes, por eso no puede ser de instancia:
# necesitaría un objeto que no tiene por qué existir.
# ------------------------------------------------------------------
print("\n=== Ejercicio 7 ===")
print(Cliente.resumen())             # funciona SIN tener ningún objeto en la mano

# ------------------------------------------------------------------
# EJERCICIO 8 · agrupar_por_ciudad() está en views.py (controlador) y
# se ve en el menú de main.py, opción 8. Aquí un ejemplo con datos reales.
# ------------------------------------------------------------------
print("\n=== Ejercicio 8 ===")
print("Ver views.py -> ClienteController.agrupar_por_ciudad()")
print("Y en el menú: python main.py -> opción 8 (Clientes por ciudad)")
