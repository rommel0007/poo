"""Modelo (MVC) — Ejercicios 3, 10, 11, 19: clases de gestión con diccionarios."""


class CarroCompras:
    """Ej. 3 — Gestor de compras con totales."""

    def __init__(self):
        self.articulos = {}

    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio

    def total_carrito(self):
        return sum(self.articulos.values())

    def articulos_por_rango(self, precio_min, precio_max):
        return [nombre for nombre, precio in self.articulos.items() if precio_min <= precio <= precio_max]


class Tareas:
    """Ej. 10 — Gestor de tareas con prioridad."""

    def __init__(self):
        self.lista = []

    def agregar_tarea(self, descripcion, prioridad):
        self.lista.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        return [tarea for tarea in self.lista if tarea[1] == "alta"]

    def eliminar_completada(self, descripcion):
        self.lista = [tarea for tarea in self.lista if tarea[0] != descripcion]


class ContadorFrecuencia:
    """Ej. 11 — Contador de frecuencia."""

    def __init__(self):
        self.contador = {}

    def agregar_elemento(self, elemento):
        self.contador[elemento] = self.contador.get(elemento, 0) + 1

    def elemento_mas_frecuente(self):
        if not self.contador:
            return None
        return max(self.contador, key=lambda elem: self.contador[elem])

    def frecuencia_elemento(self, elemento):
        return self.contador.get(elemento, 0)


class Inventario:
    """Ej. 19 — Inventario de productos."""

    def __init__(self):
        self.stock = {}

    def agregar_stock(self, producto, cantidad):
        self.stock[producto] = self.stock.get(producto, 0) + cantidad

    def restar_stock(self, producto, cantidad):
        if self.stock.get(producto, 0) >= cantidad:
            self.stock[producto] -= cantidad
            return True
        return False

    def productos_bajo_stock(self, minimo):
        return [producto for producto, cantidad in self.stock.items() if cantidad < minimo]
