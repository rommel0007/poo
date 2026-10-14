import json
import os
from estudiante import Estudiante


class ModeloEstudiantes:
    def __init__(self, archivo='estudiantes.json'):
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
                if texto in f"{r['nombre']} {r['apellido']} {r['carrera']}".casefold()]

    def crear(self, **datos):
        estudiante = Estudiante(**datos)
        if self.buscar(estudiante.cedula):
            raise ValueError('Ya existe un estudiante con esa cédula.')
        if any(r['correo'] == estudiante.correo for r in self.registros):
            raise ValueError('Ese correo ya está registrado.')
        self.registros.append(estudiante.a_diccionario())
        self._escribir()
        return estudiante

    def listar(self):
        return sorted(self.registros, key=lambda r: (r['apellido'], r['nombre']))

    def actualizar(self, cedula, **cambios):
        actual = self.buscar(cedula)
        if actual is None:
            return False
        validado = Estudiante(**{**actual, **cambios})
        if any(r['correo'] == validado.correo and r is not actual for r in self.registros):
            raise ValueError('Ese correo ya está registrado.')
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

    def resumen_por_carrera(self):
        conteo = {}
        for r in self.registros:
            conteo[r['carrera']] = conteo.get(r['carrera'], 0) + 1
        return dict(sorted(conteo.items()))
