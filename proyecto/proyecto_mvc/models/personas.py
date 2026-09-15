"""Modelo (MVC) — Ejercicios 1, 6, 7, 8, 14, 17: clases sobre personas y registros."""


class Calificador:
    """Ej. 1 — Validador de notas con promedio."""

    def __init__(self):
        self.notas = []

    def validar_nota(self, nota):
        return 0 <= nota <= 100

    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)
        return self.notas

    def promedio(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)


class GestorTemperatura:
    """Ej. 6 — Estadísticas de temperatura."""

    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def registrar_multiples(self, *temps):
        for temp in temps:
            self.registrar_temperatura(temp)

    def minima(self):
        return min(self.temperaturas)

    def maxima(self):
        return max(self.temperaturas)

    def promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)


class GestorPersonas:
    """Ej. 7 — Mapeador de edades."""

    def __init__(self):
        self.personas = {}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):
        return [nombre for nombre, edad in self.personas.items() if edad >= edad_minima]

    def edad_promedio(self):
        if not self.personas:
            return 0
        return sum(self.personas.values()) / len(self.personas)


class Equipos:
    """Ej. 8 — Asignador de equipos."""

    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        if not self.equipos:
            return None
        return max(self.equipos, key=lambda nombre: len(self.equipos[nombre]))


class RegistroNotas:
    """Ej. 14 — Mapeo de estudiantes a notas."""

    def __init__(self):
        self.notas = {}

    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        return [estudiante for estudiante, nota in self.notas.items() if nota >= nota_minima]

    def mejor_estudiante(self):
        if not self.notas:
            return None
        nombre = max(self.notas, key=lambda estudiante: self.notas[estudiante])
        return (nombre, self.notas[nombre])


class AgrupadorEdades:
    """Ej. 17 — Grupo de edades."""

    def __init__(self):
        self.agrupado = {}

    def clasificar_edad(self, edad):
        if edad < 12:
            return "niño"
        if edad < 18:
            return "adolescente"
        if edad < 65:
            return "adulto"
        return "mayor"

    def agrupar_por_categoria(self, *edades):
        self.agrupado = {}
        for edad in edades:
            categoria = self.clasificar_edad(edad)
            self.agrupado.setdefault(categoria, []).append(edad)
        return self.agrupado

    def edad_promedio_categoria(self, categoria):
        edades = self.agrupado.get(categoria, [])
        if not edades:
            return 0
        return sum(edades) / len(edades)
