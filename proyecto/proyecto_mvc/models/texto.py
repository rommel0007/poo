"""Modelo (MVC) — Ejercicios 2, 4, 9, 13, 16, 20: clases sobre texto y secuencias."""


class AnalizadorTexto:
    """Ej. 2 — Contador de palabras únicas."""

    def __init__(self):
        self.palabras_unicas = set()
        self.palabras_orden = []

    def agregar_palabra(self, palabra):
        self.palabras_unicas.add(palabra)
        self.palabras_orden.append(palabra)

    def contar_palabras(self):
        return len(self.palabras_unicas)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)


class InversorSecuencia:
    """Ej. 4 — Inversor de secuencias (sin usar reversed())."""

    def invertir_lista(self, lista):
        invertida = []
        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])
        return invertida

    def invertir_multiples(self, *listas):
        resultado = {}
        for lista in listas:
            resultado[tuple(lista)] = self.invertir_lista(lista)
        return resultado


class AnalizadorString:
    """Ej. 9 — Validador de caracteres."""

    VOCALES = "aeiouAEIOU"

    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        return letra in self.VOCALES

    def contar_por_tipo(self, texto):
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto
        vocales = consonantes = digitos = 0
        for caracter in texto:
            if caracter.isdigit():
                digitos += 1
            elif caracter.isalpha():
                if self.solo_vocales(caracter):
                    vocales += 1
                else:
                    consonantes += 1
        return {"vocales": vocales, "consonantes": consonantes, "digitos": digitos}


class CombinadorListas:
    """Ej. 13 — Combinador de listas (intercalado)."""

    def intercalar(self, lista1, lista2):
        resultado = []
        largo = max(len(lista1), len(lista2))
        for i in range(largo):
            if i < len(lista1):
                resultado.append(lista1[i])
            if i < len(lista2):
                resultado.append(lista2[i])
        return resultado

    def intercalar_multiples(self, *listas):
        resultado = []
        largo = max(len(lista) for lista in listas)
        for i in range(largo):
            for lista in listas:
                if i < len(lista):
                    resultado.append(lista[i])
        return resultado


class CodificadorCesar:
    """Ej. 16 — Codificador/Decodificador César."""

    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        if not letra.isalpha():
            return letra
        base = ord('A') if letra.isupper() else ord('a')
        return chr((ord(letra) - base + desplazamiento) % 26 + base)

    def codificar_palabra(self, palabra, desplazamiento):
        codificada = "".join(self.codificar_letra(c, desplazamiento) for c in palabra)
        self.historial[palabra] = codificada
        return codificada


class AnalizadorPatrones:
    """Ej. 20 — Analizador de patrones en textos."""

    def __init__(self):
        self._todas_las_palabras = set()

    def encontrar_palabras(self, texto, patron):
        palabras = texto.split()
        self._todas_las_palabras.update(palabras)
        return [p for p in palabras if p.startswith(patron)]

    def agrupar_por_longitud(self, texto):
        palabras = texto.split()
        self._todas_las_palabras.update(palabras)
        agrupado = {}
        for palabra in palabras:
            agrupado.setdefault(len(palabra), []).append(palabra)
        return agrupado

    def palabras_unicas(self):
        return self._todas_las_palabras
