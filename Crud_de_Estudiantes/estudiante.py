from datetime import date

SEMESTRE_MAXIMO = 10


class Estudiante:
    """Estudiante con validación en propiedades y fecha de ingreso automática."""

    def __init__(self, cedula, nombre, apellido, correo, carrera, semestre, fecha_ingreso=None):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.carrera = carrera
        self.semestre = semestre
        self.fecha_ingreso = fecha_ingreso or date.today().isoformat()

    @staticmethod
    def _texto(valor, etiqueta):
        valor = str(valor).strip()
        if not valor:
            raise ValueError(f'{etiqueta} es obligatorio.')
        return valor

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, valor):
        valor = str(valor).strip()
        if not (valor.isdigit() and len(valor) == 10):
            raise ValueError('La cédula debe tener exactamente 10 dígitos.')
        self._cedula = valor

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = self._texto(valor, 'El nombre').title()

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, valor):
        self._apellido = self._texto(valor, 'El apellido').title()

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        valor = self._texto(valor, 'El correo').lower()
        if valor.count('@') != 1 or '.' not in valor.split('@')[1]:
            raise ValueError('El correo no tiene un formato válido.')
        self._correo = valor

    @property
    def carrera(self):
        return self._carrera

    @carrera.setter
    def carrera(self, valor):
        self._carrera = self._texto(valor, 'La carrera').title()

    @property
    def semestre(self):
        return self._semestre

    @semestre.setter
    def semestre(self, valor):
        try:
            valor = int(valor)
        except (TypeError, ValueError):
            raise ValueError('El semestre debe ser un número entero.')
        if not 1 <= valor <= SEMESTRE_MAXIMO:
            raise ValueError(f'El semestre debe estar entre 1 y {SEMESTRE_MAXIMO}.')
        self._semestre = valor

    def a_diccionario(self):
        return {
            'cedula': self.cedula,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'correo': self.correo,
            'carrera': self.carrera,
            'semestre': self.semestre,
            'fecha_ingreso': self.fecha_ingreso,
        }
