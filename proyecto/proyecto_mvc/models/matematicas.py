"""Modelo (MVC) — Ejercicios 5, 12, 15, 18: clases sobre números y coordenadas."""


class AnalizadorNumeros:
    """Ej. 5 — Detector de números pares e impares."""

    def __init__(self):
        self.pares = []
        self.impares = []

    def es_par(self, numero):
        return numero % 2 == 0

    def separar(self, *numeros):
        self.pares = []
        self.impares = []
        for numero in numeros:
            if self.es_par(numero):
                self.pares.append(numero)
            else:
                self.impares.append(numero)
        return {"pares": self.pares, "impares": self.impares}

    def cantidad_pares_impares(self):
        return (len(self.pares), len(self.impares))


class SelectorRango:
    """Ej. 12 — Selector de rango con tuplas."""

    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin + 1))

    def elementos_en_multiples_rangos(self, *rangos):
        combinados = set()
        for inicio, fin in rangos:
            combinados.update(self.crear_rango(inicio, fin))
        return sorted(combinados)


class DivisorFinder:
    """Ej. 15 — Divisores de un número."""

    def encontrar_divisores(self, numero):
        divisores = []
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)
        return tuple(divisores)

    def es_perfecto(self, numero):
        divisores_propios = [d for d in self.encontrar_divisores(numero) if d != numero]
        return sum(divisores_propios) == numero

    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}
        for numero in numeros:
            resultado[numero] = self.encontrar_divisores(numero)
        return resultado


class CalculadorDistancia:
    """Ej. 18 — Matriz de distancias (distancia euclidiana entre puntos 2D)."""

    def __init__(self):
        self.distancias_calculadas = []

    def distancia_euclidiana(self, p1, p2):
        distancia = ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
        self.distancias_calculadas.append(distancia)
        return distancia

    def punto_mas_cercano(self, referencia, *puntos):
        mas_cercano = None
        menor_distancia = None
        for punto in puntos:
            distancia = self.distancia_euclidiana(referencia, punto)
            if menor_distancia is None or distancia < menor_distancia:
                menor_distancia = distancia
                mas_cercano = punto
        return mas_cercano
