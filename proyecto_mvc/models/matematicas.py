"""Modelo (MVC) — Ejercicios 5, 12, 15, 18: clases sobre números y coordenadas."""


class ClasificadorSigno:
    """Ej. 5 — Clasificador de números positivos, negativos y ceros."""

    def __init__(self):
        self.positivos = []
        self.negativos = []
        self.ceros = []

    def signo(self, numero):
        if numero > 0:
            return "positivo"
        if numero < 0:
            return "negativo"
        return "cero"

    def separar(self, *numeros):
        self.positivos = []
        self.negativos = []
        self.ceros = []
        for numero in numeros:
            tipo = self.signo(numero)
            if tipo == "positivo":
                self.positivos.append(numero)
            elif tipo == "negativo":
                self.negativos.append(numero)
            else:
                self.ceros.append(numero)
        return {"positivos": self.positivos, "negativos": self.negativos, "ceros": self.ceros}

    def cantidad_por_signo(self):
        return (len(self.positivos), len(self.negativos), len(self.ceros))


class GeneradorTablas:
    """Ej. 12 — Generador de tablas de multiplicar con tuplas."""

    def tabla(self, base, limite=10):
        return tuple(base * i for i in range(1, limite + 1))

    def tablas_multiples(self, *bases):
        resultado = {}
        for base in bases:
            resultado[base] = self.tabla(base)
        return resultado

    def suma_tabla(self, base, limite=10):
        return sum(self.tabla(base, limite))


class Factorizador:
    """Ej. 15 — Factores primos, MCD y MCM."""

    def factores_primos(self, numero):
        factores = {}
        divisor = 2
        while numero > 1:
            while numero % divisor == 0:
                factores[divisor] = factores.get(divisor, 0) + 1
                numero //= divisor
            divisor += 1
        return factores

    def mcd(self, a, b):
        while b:
            a, b = b, a % b
        return abs(a)

    def mcm(self, a, b):
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // self.mcd(a, b)

    def mcd_multiples(self, *numeros):
        resultado = 0
        for numero in numeros:
            resultado = self.mcd(resultado, numero)
        return resultado


class CalculadorPerimetro:
    """Ej. 18 — Perímetro de polígonos a partir de puntos 2D."""

    def __init__(self):
        self.perimetros = []

    def distancia(self, p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

    def perimetro(self, *puntos):
        if len(puntos) < 3:
            return 0
        total = 0
        for i in range(len(puntos)):
            siguiente = puntos[(i + 1) % len(puntos)]
            total += self.distancia(puntos[i], siguiente)
        self.perimetros.append(total)
        return total

    def punto_medio(self, p1, p2):
        return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

    def punto_mas_lejano(self, referencia, *puntos):
        if not puntos:
            return None
        return max(puntos, key=lambda punto: self.distancia(referencia, punto))
