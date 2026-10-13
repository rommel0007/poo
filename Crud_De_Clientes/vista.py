class VistaClientes:
    CAMPOS = ('nombre', 'apellido', 'telefono', 'correo', 'ciudad')

    def menu(self, total):
        print('\n' + '*' * 44)
        print(f'*{"GESTIÓN DE CLIENTES":^42}*')
        print(f'*{f"Clientes registrados: {total}":^42}*')
        print('*' * 44)
        print(' [1] Nuevo cliente')
        print(' [2] Ver todos (ordenados por apellido)')
        print(' [3] Buscar por cédula')
        print(' [4] Buscar por nombre, apellido o ciudad')
        print(' [5] Modificar cliente')
        print(' [6] Borrar cliente')
        print(' [0] Salir')
        return input('Elija una opción: ').strip()

    def pedir_datos(self, cliente=None):
        """Devuelve solo los campos escritos; en modificación, vacío = conservar."""
        datos = {}
        for campo in self.CAMPOS:
            pista = f' (actual: {cliente[campo]})' if cliente else ''
            valor = input(f'{campo.capitalize()}{pista}: ').strip()
            if valor or not cliente:
                datos[campo] = valor
        return datos

    def mostrar_tabla(self, clientes):
        print(f'\n{"Cédula":<12}{"Cliente":<26}{"Teléfono":<12}{"Ciudad":<14}')
        print('-' * 64)
        for c in clientes:
            nombre = f"{c['apellido']} {c['nombre']}"
            print(f"{c['cedula']:<12}{nombre:<26}{c['telefono']:<12}{c['ciudad']:<14}")
        print(f'\nResultados: {len(clientes)}')

    def mostrar_ficha(self, c):
        print('\n+' + '-' * 40)
        print(f"| Cédula    : {c['cedula']}")
        print(f"| Cliente   : {c['nombre']} {c['apellido']}")
        print(f"| Teléfono  : {c['telefono']}")
        print(f"| Correo    : {c['correo']}")
        print(f"| Ciudad    : {c['ciudad']}")
        print(f"| Registrado: {c['fecha_registro']}")
        print('+' + '-' * 40)

    def mensaje(self, texto):
        print(f'\n>> {texto}')
