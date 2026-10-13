import json
import os
from cliente import Cliente


class ModeloClientes:
    def __init__(self, archivo='clientes.json'):
        self.ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), archivo)
        self.registros = self._leer()

    def _leer(self):
        if not os.path.exists(self.ruta):
            return []
        try:
            with open(self.ruta, 'r', encoding='utf-8') as f:
                datos = json.load(f)
            return datos if isinstance(datos, list) else []
        except (json.JSONDecodeError, OSError):
            print('Aviso: el archivo JSON no se pudo leer; se parte de una lista vacía.')
            return []

    def _escribir(self):
        with open(self.ruta, 'w', encoding='utf-8') as f:
            json.dump(self.registros, f, indent=2, ensure_ascii=False)

    def buscar(self, cedula):
        return next((r for r in self.registros if r['cedula'] == cedula), None)

    def buscar_texto(self, texto):
        texto = texto.strip().casefold()
        return [r for r in self.registros
                if texto in f"{r['nombre']} {r['apellido']} {r['ciudad']}".casefold()]

    def crear(self, **datos):
        cliente = Cliente(**datos)
        if self.buscar(cliente.cedula):
            raise ValueError('Ya existe un cliente con esa cédula.')
        self.registros.append(cliente.a_diccionario())
        self._escribir()
        return cliente

    def listar(self):
        return sorted(self.registros, key=lambda r: (r['apellido'], r['nombre']))

    def actualizar(self, cedula, **cambios):
        actual = self.buscar(cedula)
        if actual is None:
            return False
        validado = Cliente(**{**actual, **cambios})
        actual.update(validado.a_diccionario())
        self._escribir()
        return True

    def eliminar(self, cedula):
        actual = self.buscar(cedula)
        if actual is None:
            return False
        self.registros.remove(actual)
        self._escribir()
        return True

    def total(self):
        return len(self.registros)
