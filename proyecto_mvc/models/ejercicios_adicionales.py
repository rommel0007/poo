"""Modelo (MVC) — EJERCICIOS ADICIONALES (21-40).

Este archivo contiene los 20 ejercicios ADICIONALES, agregados aparte de los 20
primeros (1-20) que están repartidos en matematicas.py, texto.py,
personas.py y gestion.py. Mismo estilo: clases simples, con listas, tuplas,
diccionarios o conjuntos, sin print() ni input() (eso vive en la Vista).
"""

import math


class CalculadoraIVA:
    """Ej. 21 — Calculadora de IVA con historial."""

    def __init__(self):
        self.historial = []

    def calcular_iva(self, precio, tasa=15):
        iva = precio * tasa / 100
        self.historial.append(iva)
        return iva

    def precio_con_iva(self, precio, tasa=15):
        return precio + self.calcular_iva(precio, tasa)

    def precios_con_iva(self, *precios):
        return [self.precio_con_iva(precio) for precio in precios]


class SumadorSerie:
    """Ej. 22 — Sumador de series numéricas."""

    def suma_hasta(self, n):
        return sum(range(1, n + 1))

    def suma_pares(self, limite):
        return sum(range(2, limite + 1, 2))

    def suma_cuadrados(self, *numeros):
        return sum(numero ** 2 for numero in numeros)


class GeneradorPotencias:
    """Ej. 23 — Generador de potencias de una base."""

    def potencias(self, base, cantidad):
        return tuple(base ** i for i in range(cantidad))

    def es_potencia_de(self, base, numero):
        if base < 2 or numero < 1:
            return False
        while numero % base == 0:
            numero //= base
        return numero == 1


class CalculadoraArea:
    """Ej. 24 — Calculadora de áreas de figuras."""

    def __init__(self):
        self.calculos = {}

    def area_rectangulo(self, base, altura):
        area = base * altura
        self.calculos["rectángulo"] = area
        return area

    def area_triangulo(self, base, altura):
        area = base * altura / 2
        self.calculos["triángulo"] = area
        return area

    def area_circulo(self, radio):
        area = round(math.pi * radio ** 2, 2)
        self.calculos["círculo"] = area
        return area

    def figura_mayor(self):
        if not self.calculos:
            return None
        return max(self.calculos, key=lambda figura: self.calculos[figura])


class VerificadorBisiesto:
    """Ej. 25 — Verificador de años bisiestos."""

    def es_bisiesto(self, anio):
        return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

    def bisiestos_en(self, *anios):
        return [anio for anio in anios if self.es_bisiesto(anio)]

    def dias_del_anio(self, anio):
        return 366 if self.es_bisiesto(anio) else 365


class ContadorLetras:
    """Ej. 26 — Contador de frecuencia de letras."""

    def frecuencia(self, texto):
        conteo = {}
        for letra in texto.lower():
            if letra.isalpha():
                conteo[letra] = conteo.get(letra, 0) + 1
        return conteo

    def letra_mas_comun(self, texto):
        conteo = self.frecuencia(texto)
        if not conteo:
            return None
        return max(conteo, key=lambda letra: conteo[letra])


class LimpiadorTexto:
    """Ej. 27 — Limpiador de texto con historial."""

    VOCALES = "aeiouAEIOU"

    def __init__(self):
        self.historial = []

    def quitar_espacios_extra(self, texto):
        resultado = " ".join(texto.split())
        self.historial.append(resultado)
        return resultado

    def quitar_vocales(self, texto):
        resultado = "".join(letra for letra in texto if letra not in self.VOCALES)
        self.historial.append(resultado)
        return resultado

    def limpiar_multiples(self, *textos):
        return [self.quitar_espacios_extra(texto) for texto in textos]


class GeneradorUsuarios:
    """Ej. 28 — Generador de nombres de usuario únicos."""

    def __init__(self):
        self.usuarios = set()

    def crear_usuario(self, nombre, apellido):
        base = (nombre[0] + apellido).lower()
        usuario = base
        contador = 2
        while usuario in self.usuarios:
            usuario = f"{base}{contador}"
            contador += 1
        self.usuarios.add(usuario)
        return usuario

    def crear_multiples(self, *personas):
        return [self.crear_usuario(nombre, apellido) for nombre, apellido in personas]

    def total_usuarios(self):
        return len(self.usuarios)


class FormateadorNombres:
    """Ej. 29 — Formateador de nombres propios."""

    def capitalizar_nombre(self, nombre):
        return " ".join(parte.capitalize() for parte in nombre.split())

    def iniciales(self, nombre):
        return ".".join(parte[0].upper() for parte in nombre.split()) + "."

    def formatear_multiples(self, *nombres):
        return [self.capitalizar_nombre(nombre) for nombre in nombres]


class BuscadorPalabras:
    """Ej. 30 — Buscador de posiciones de una palabra."""

    def __init__(self):
        self.busquedas = []

    def posiciones(self, texto, palabra):
        self.busquedas.append(palabra)
        palabras = texto.split()
        return [i for i, actual in enumerate(palabras) if actual == palabra]

    def primera_posicion(self, texto, palabra):
        encontradas = self.posiciones(texto, palabra)
        return encontradas[0] if encontradas else -1


class RegistroClimas:
    """Ej. 31 — Registro de temperaturas por ciudad."""

    def __init__(self):
        self.temperaturas = {}

    def agregar_temperatura(self, ciudad, temperatura):
        self.temperaturas.setdefault(ciudad, []).append(temperatura)

    def promedio_ciudad(self, ciudad):
        temps = self.temperaturas.get(ciudad, [])
        if not temps:
            return 0
        return sum(temps) / len(temps)

    def ciudad_mas_calida(self):
        if not self.temperaturas:
            return None
        nombre = max(self.temperaturas, key=lambda c: self.promedio_ciudad(c))
        return (nombre, self.promedio_ciudad(nombre))


class GestorDeudas:
    """Ej. 32 — Gestor de deudas y pagos."""

    def __init__(self):
        self.deudas = {}

    def agregar_deuda(self, persona, monto):
        self.deudas[persona] = self.deudas.get(persona, 0) + monto

    def pagar(self, persona, monto):
        if persona not in self.deudas or monto <= 0 or monto > self.deudas[persona]:
            return False
        self.deudas[persona] -= monto
        return True

    def total_deudas(self):
        return sum(self.deudas.values())

    def mayor_deudor(self):
        if not self.deudas:
            return None
        nombre = max(self.deudas, key=lambda p: self.deudas[p])
        return (nombre, self.deudas[nombre])


class ClasificadorTriangulos:
    """Ej. 33 — Clasificador de triángulos por sus lados."""

    def es_valido(self, a, b, c):
        return a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a

    def clasificar(self, a, b, c):
        if not self.es_valido(a, b, c):
            return "no válido"
        if a == b == c:
            return "equilátero"
        if a == b or b == c or a == c:
            return "isósceles"
        return "escaleno"

    def clasificar_multiples(self, *ternas):
        conteo = {}
        for a, b, c in ternas:
            tipo = self.clasificar(a, b, c)
            conteo[tipo] = conteo.get(tipo, 0) + 1
        return conteo


class ConversorRomanos:
    """Ej. 34 — Conversor de números enteros a romanos y viceversa."""

    VALORES = (
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
    )

    def __init__(self):
        self.historial = {}

    def a_romano(self, numero):
        if not 1 <= numero <= 3999:
            raise ValueError("El número debe estar entre 1 y 3999")
        original = numero
        resultado = ""
        for valor, simbolo in self.VALORES:
            while numero >= valor:
                resultado += simbolo
                numero -= valor
        self.historial[original] = resultado
        return resultado

    def a_entero(self, romano):
        total = 0
        posicion = 0
        for valor, simbolo in self.VALORES:
            while romano.startswith(simbolo, posicion):
                total += valor
                posicion += len(simbolo)
        return total


class GestorAmigos:
    """Ej. 35 — Gestor de amistades con conjuntos."""

    def __init__(self):
        self.amigos = {}

    def agregar_amistad(self, persona1, persona2):
        self.amigos.setdefault(persona1, set()).add(persona2)
        self.amigos.setdefault(persona2, set()).add(persona1)

    def amigos_de(self, persona):
        return self.amigos.get(persona, set())

    def amigos_en_comun(self, persona1, persona2):
        return self.amigos_de(persona1) & self.amigos_de(persona2)


class GestorAsientos:
    """Ej. 36 — Gestor de asientos de sala (fila, número)."""

    def __init__(self):
        self.vendidos = set()

    def comprar_asiento(self, fila, numero):
        asiento = (fila, numero)
        if asiento in self.vendidos:
            return False
        self.vendidos.add(asiento)
        return True

    def asientos_libres(self, filas, columnas):
        todos = {(f, c) for f in range(1, filas + 1) for c in range(1, columnas + 1)}
        return sorted(todos - self.vendidos)

    def total_vendidos(self):
        return len(self.vendidos)


class TablaPuntos:
    """Ej. 37 — Tabla de posiciones de un torneo."""

    def __init__(self):
        self.puntos = {}

    def registrar_partido(self, local, visitante, goles_local, goles_visitante):
        self.puntos.setdefault(local, 0)
        self.puntos.setdefault(visitante, 0)
        if goles_local > goles_visitante:
            self.puntos[local] += 3
        elif goles_local < goles_visitante:
            self.puntos[visitante] += 3
        else:
            self.puntos[local] += 1
            self.puntos[visitante] += 1

    def tabla(self):
        return sorted(self.puntos.items(), key=lambda par: par[1], reverse=True)

    def lider(self):
        if not self.puntos:
            return None
        return self.tabla()[0][0]


class OperadorMatrices:
    """Ej. 38 — Operaciones básicas con matrices (listas de listas)."""

    def sumar_filas(self, matriz):
        return [sum(fila) for fila in matriz]

    def suma_diagonal(self, matriz):
        if not matriz:
            return 0
        return sum(matriz[i][i] for i in range(min(len(matriz), len(matriz[0]))))

    def transponer(self, matriz):
        if not matriz:
            return []
        return [[matriz[f][c] for f in range(len(matriz))] for c in range(len(matriz[0]))]


class ConversorTiempo:
    """Ej. 39 — Conversor de segundos a horas, minutos y segundos."""

    def segundos_a_hms(self, segundos):
        horas = segundos // 3600
        minutos = (segundos % 3600) // 60
        resto = segundos % 60
        return (horas, minutos, resto)

    def hms_a_segundos(self, horas, minutos, segundos):
        return horas * 3600 + minutos * 60 + segundos

    def sumar_tiempos(self, *tiempos):
        total = sum(self.hms_a_segundos(*tiempo) for tiempo in tiempos)
        return self.segundos_a_hms(total)


class ListaInvitados:
    """Ej. 40 — Lista de invitados con confirmaciones."""

    def __init__(self):
        self.invitados = set()
        self.confirmados = set()

    def agregar_invitado(self, nombre):
        if nombre in self.invitados:
            return False
        self.invitados.add(nombre)
        return True

    def confirmar(self, nombre):
        if nombre not in self.invitados:
            return False
        self.confirmados.add(nombre)
        return True

    def pendientes(self):
        return self.invitados - self.confirmados
