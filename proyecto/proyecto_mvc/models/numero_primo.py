"""Modelo (MVC) — Ejercicio 0 (modelo resuelto de la guía)."""


class NumeroPrimo:
    """Valida números primos y guarda historial de verificaciones."""

    def __init__(self):
        self.historial = []

    def es_primo(self, numero):
        self.historial.append(numero)
        if numero < 2:
            return False
        for divisor in range(2, int(numero ** 0.5) + 1):
            if numero % divisor == 0:
                return False
        return True

    def primos_en_rango(self, *args):
        primos = []
        for numero in args:
            if self.es_primo(numero):
                primos.append(numero)
        return primos

    def cantidad_verificados(self):
        return len(self.historial)

    def limpiar_historial(self):
        self.historial = []
