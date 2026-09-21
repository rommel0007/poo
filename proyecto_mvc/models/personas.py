"""Modelo (MVC) — Ejercicios 1, 6, 7, 8, 14, 17: clases sobre personas y registros."""


class ValidadorPuntajes:
    """Ej. 1 — Validador de puntajes (0 a 10) con promedio."""

    def __init__(self):
        self.puntajes = []

    def validar_puntaje(self, puntaje):
        return 0 <= puntaje <= 10

    def cargar_puntajes(self, *args):
        for puntaje in args:
            if self.validar_puntaje(puntaje):
                self.puntajes.append(puntaje)
        return self.puntajes

    def mejor_puntaje(self):
        if not self.puntajes:
            return None
        return max(self.puntajes)

    def promedio(self):
        if not self.puntajes:
            return 0
        return sum(self.puntajes) / len(self.puntajes)


class GestorVentas:
    """Ej. 6 — Estadísticas de ventas diarias."""

    def __init__(self):
        self.ventas = []

    def registrar_venta(self, monto):
        self.ventas.append(monto)

    def registrar_multiples(self, *montos):
        for monto in montos:
            self.registrar_venta(monto)

    def venta_maxima(self):
        if not self.ventas:
            return None
        return max(self.ventas)

    def venta_minima(self):
        if not self.ventas:
            return None
        return min(self.ventas)

    def total(self):
        return sum(self.ventas)


class GestorAlturas:
    """Ej. 7 — Mapeador de alturas."""

    def __init__(self):
        self.personas = {}

    def agregar_persona(self, nombre, altura):
        self.personas[nombre] = altura

    def personas_mas_altas(self, altura_minima):
        return [nombre for nombre, altura in self.personas.items() if altura >= altura_minima]

    def altura_promedio(self):
        if not self.personas:
            return 0
        return sum(self.personas.values()) / len(self.personas)


class Aulas:
    """Ej. 8 — Asignador de estudiantes a aulas."""

    def __init__(self):
        self.aulas = {}

    def crear_aula(self, nombre_aula):
        self.aulas[nombre_aula] = []

    def agregar_estudiante(self, aula, estudiante):
        if aula not in self.aulas:
            return False
        self.aulas[aula].append(estudiante)
        return True

    def aula_menos_ocupada(self):
        if not self.aulas:
            return None
        return min(self.aulas, key=lambda nombre: len(self.aulas[nombre]))

    def total_estudiantes(self):
        return sum(len(estudiantes) for estudiantes in self.aulas.values())


class RegistroPeliculas:
    """Ej. 14 — Mapeo de películas a puntuación."""

    def __init__(self):
        self.puntuaciones = {}

    def registrar(self, pelicula, puntuacion):
        self.puntuaciones[pelicula] = puntuacion

    def peliculas_recomendadas(self, puntuacion_minima):
        return [pelicula for pelicula, punto in self.puntuaciones.items() if punto >= puntuacion_minima]

    def mejor_pelicula(self):
        if not self.puntuaciones:
            return None
        nombre = max(self.puntuaciones, key=lambda pelicula: self.puntuaciones[pelicula])
        return (nombre, self.puntuaciones[nombre])


class AgrupadorSalarios:
    """Ej. 17 — Grupo de salarios por rango."""

    def __init__(self):
        self.agrupado = {}

    def clasificar_salario(self, salario):
        if salario < 500:
            return "bajo"
        if salario < 1500:
            return "medio"
        return "alto"

    def agrupar_por_categoria(self, *salarios):
        self.agrupado = {}
        for salario in salarios:
            categoria = self.clasificar_salario(salario)
            self.agrupado.setdefault(categoria, []).append(salario)
        return self.agrupado

    def salario_promedio_categoria(self, categoria):
        salarios = self.agrupado.get(categoria, [])
        if not salarios:
            return 0
        return sum(salarios) / len(salarios)
