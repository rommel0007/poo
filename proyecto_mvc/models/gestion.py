"""Modelo (MVC) — Ejercicios 3, 10, 11, 19: clases de gestión con diccionarios."""


class GestorCuentas:
    """Ej. 3 — Gestor de cuentas bancarias con saldos."""

    def __init__(self):
        self.cuentas = {}

    def abrir_cuenta(self, titular, saldo_inicial=0):
        self.cuentas[titular] = saldo_inicial

    def depositar(self, titular, monto):
        if titular not in self.cuentas or monto <= 0:
            return False
        self.cuentas[titular] += monto
        return True

    def retirar(self, titular, monto):
        if titular in self.cuentas and 0 < monto <= self.cuentas[titular]:
            self.cuentas[titular] -= monto
            return True
        return False

    def saldo_total(self):
        return sum(self.cuentas.values())

    def cuentas_con_saldo_mayor(self, minimo):
        return [titular for titular, saldo in self.cuentas.items() if saldo > minimo]


class Agenda:
    """Ej. 10 — Agenda de citas (fecha, descripción)."""

    def __init__(self):
        self.citas = []

    def agregar_cita(self, fecha, descripcion):
        self.citas.append((fecha, descripcion))

    def citas_del_dia(self, fecha):
        return [cita[1] for cita in self.citas if cita[0] == fecha]

    def cancelar_cita(self, descripcion):
        self.citas = [cita for cita in self.citas if cita[1] != descripcion]

    def total_citas(self):
        return len(self.citas)


class UrnaVotos:
    """Ej. 11 — Urna de votos con ganador."""

    def __init__(self):
        self.votos = {}

    def votar(self, candidato):
        self.votos[candidato] = self.votos.get(candidato, 0) + 1

    def ganador(self):
        if not self.votos:
            return None
        return max(self.votos, key=lambda cand: self.votos[cand])

    def votos_candidato(self, candidato):
        return self.votos.get(candidato, 0)

    def total_votos(self):
        return sum(self.votos.values())


class Biblioteca:
    """Ej. 19 — Biblioteca de libros con préstamos."""

    def __init__(self):
        self.catalogo = {}

    def agregar_libro(self, titulo, copias):
        self.catalogo[titulo] = self.catalogo.get(titulo, 0) + copias

    def prestar_libro(self, titulo):
        if self.catalogo.get(titulo, 0) > 0:
            self.catalogo[titulo] -= 1
            return True
        return False

    def devolver_libro(self, titulo):
        if titulo not in self.catalogo:
            return False
        self.catalogo[titulo] += 1
        return True

    def libros_agotados(self):
        return [titulo for titulo, copias in self.catalogo.items() if copias == 0]
