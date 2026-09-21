"""Modelo (MVC) — Ejercicios 2, 4, 9, 13, 16, 20: clases sobre texto y secuencias."""


class DetectorDuplicados:
    """Ej. 2 — Detector de palabras duplicadas."""

    def __init__(self):
        self.vistas = set()
        self.repetidas = set()
        self.orden = []

    def agregar_palabra(self, palabra):
        if palabra in self.vistas:
            self.repetidas.add(palabra)
        self.vistas.add(palabra)
        self.orden.append(palabra)

    def agregar_multiples(self, *palabras):
        for palabra in palabras:
            self.agregar_palabra(palabra)

    def hay_duplicados(self):
        return len(self.repetidas) > 0

    def palabras_repetidas(self):
        return sorted(self.repetidas)


class RotadorSecuencia:
    """Ej. 4 — Rotador de secuencias hacia la izquierda."""

    def rotar_lista(self, lista, posiciones):
        if not lista:
            return []
        posiciones = posiciones % len(lista)
        rotada = []
        for i in range(len(lista)):
            rotada.append(lista[(i + posiciones) % len(lista)])
        return rotada

    def rotar_multiples(self, posiciones, *listas):
        resultado = {}
        for lista in listas:
            resultado[tuple(lista)] = self.rotar_lista(lista, posiciones)
        return resultado


class ClasificadorCaracteres:
    """Ej. 9 — Clasificador de caracteres por tipo."""

    def __init__(self):
        self.textos_analizados = []

    def es_simbolo(self, caracter):
        return not caracter.isalnum() and not caracter.isspace()

    def contar_por_tipo(self, texto):
        self.textos_analizados.append(texto)
        mayusculas = minusculas = digitos = espacios = simbolos = 0
        for caracter in texto:
            if caracter.isupper():
                mayusculas += 1
            elif caracter.islower():
                minusculas += 1
            elif caracter.isdigit():
                digitos += 1
            elif caracter.isspace():
                espacios += 1
            elif self.es_simbolo(caracter):
                simbolos += 1
        return {
            "mayusculas": mayusculas,
            "minusculas": minusculas,
            "digitos": digitos,
            "espacios": espacios,
            "simbolos": simbolos,
        }


class DivisorBloques:
    """Ej. 13 — Divisor de listas en bloques de tamaño fijo."""

    def dividir_en_bloques(self, lista, tamano):
        if tamano <= 0:
            raise ValueError("El tamaño del bloque debe ser mayor a 0")
        bloques = []
        for i in range(0, len(lista), tamano):
            bloques.append(lista[i:i + tamano])
        return bloques

    def dividir_multiples(self, tamano, *listas):
        resultado = []
        for lista in listas:
            resultado.append(self.dividir_en_bloques(lista, tamano))
        return resultado


class CodificadorNumerico:
    """Ej. 16 — Codificador/Decodificador numérico (a=1 ... z=26)."""

    ABECEDARIO = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self):
        self.historial = {}

    def letra_a_numero(self, letra):
        letra = letra.lower()
        if letra in self.ABECEDARIO:
            return self.ABECEDARIO.index(letra) + 1
        return None

    def palabra_a_numeros(self, palabra):
        numeros = []
        for letra in palabra:
            numero = self.letra_a_numero(letra)
            if numero is not None:
                numeros.append(numero)
        resultado = tuple(numeros)
        self.historial[palabra] = resultado
        return resultado

    def numeros_a_palabra(self, *numeros):
        return "".join(self.ABECEDARIO[n - 1] for n in numeros if 1 <= n <= 26)


class AnalizadorFrases:
    """Ej. 20 — Analizador de frases por sufijo e inicial."""

    def __init__(self):
        self._todas_las_palabras = set()

    def palabras_que_terminan_con(self, texto, sufijo):
        palabras = texto.split()
        self._todas_las_palabras.update(palabras)
        return [p for p in palabras if p.endswith(sufijo)]

    def agrupar_por_inicial(self, texto):
        palabras = texto.split()
        self._todas_las_palabras.update(palabras)
        agrupado = {}
        for palabra in palabras:
            agrupado.setdefault(palabra[0].lower(), []).append(palabra)
        return agrupado

    def palabras_unicas(self):
        return self._todas_las_palabras
