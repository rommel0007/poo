class VistaEstudiantes:
    CAMPOS = ('nombre', 'apellido', 'correo', 'carrera', 'semestre')

    def menu(self, total):
        print('\n' + '#' * 46)
        print(f'#{"REGISTRO DE ESTUDIANTES":^44}#')
        print(f'#{f"Estudiantes registrados: {total}":^44}#')
        print('#' * 46)
        print(' [1] Nuevo estudiante')
        print(' [2] Ver todos (ordenados por apellido)')
        print(' [3] Buscar por cédula')
        print(' [4] Buscar por nombre, apellido o carrera')
        print(' [5] Modificar estudiante')
        print(' [6] Borrar estudiante')
        print(' [7] Resumen por carrera')
        print(' [0] Salir')
        return input('Elija una opción: ').strip()

    def pedir_datos(self, estudiante=None):
        """Devuelve solo los campos escritos; en modificación, vacío = conservar."""
        datos = {}
        for campo in self.CAMPOS:
            pista = f' (actual: {estudiante[campo]})' if estudiante else ''
            valor = input(f'{campo.capitalize()}{pista}: ').strip()
            if valor or not estudiante:
                datos[campo] = valor
        return datos

    def mostrar_tabla(self, estudiantes):
        print(f'\n{"Cédula":<12}{"Estudiante":<26}{"Carrera":<20}{"Sem.":<5}')
        print('-' * 63)
        for e in estudiantes:
            nombre = f"{e['apellido']} {e['nombre']}"
            print(f"{e['cedula']:<12}{nombre:<26}{e['carrera']:<20}{e['semestre']:<5}")
        print(f'\nResultados: {len(estudiantes)}')

    def mostrar_ficha(self, e):
        print('\n+' + '-' * 40)
        print(f"| Cédula  : {e['cedula']}")
        print(f"| Nombre  : {e['nombre']} {e['apellido']}")
        print(f"| Correo  : {e['correo']}")
        print(f"| Carrera : {e['carrera']}")
        print(f"| Semestre: {e['semestre']}")
        print(f"| Ingreso : {e['fecha_ingreso']}")
        print('+' + '-' * 40)

    def mostrar_resumen(self, resumen):
        print('\nEstudiantes por carrera')
        print('-' * 30)
        for carrera, cantidad in resumen.items():
            print(f'{carrera:<22}{cantidad:>3}')

    def mensaje(self, texto):
        print(f'\n>> {texto}')
