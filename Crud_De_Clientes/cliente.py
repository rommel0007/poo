from datetime import date


class Cliente:
    """Cliente con validación de datos y fecha de registro automática."""

    def __init__(self, cedula, nombre, apellido, telefono, correo, ciudad, fecha_registro=None):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.ciudad = ciudad
        self.fecha_registro = fecha_registro or date.today().isoformat()

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
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        valor = self._texto(valor, 'El teléfono')
        if not (valor.isdigit() and 7 <= len(valor) <= 10):
            raise ValueError('El teléfono debe tener entre 7 y 10 dígitos.')
        self._telefono = valor

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
    def ciudad(self):
        return self._ciudad

    @ciudad.setter
    def ciudad(self, valor):
        self._ciudad = self._texto(valor, 'La ciudad').title()

    def a_diccionario(self):
        return {
            'cedula': self.cedula,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'telefono': self.telefono,
            'correo': self.correo,
            'ciudad': self.ciudad,
            'fecha_registro': self.fecha_registro,
        }
