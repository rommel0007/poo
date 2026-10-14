from modelo import ModeloEstudiantes
from vista import VistaEstudiantes


class ControladorEstudiantes:
    def __init__(self):
        self.modelo = ModeloEstudiantes()
        self.vista = VistaEstudiantes()

    def nuevo(self):
        cedula = input('Cédula (10 dígitos): ').strip()
        datos = self.vista.pedir_datos()
        try:
            self.modelo.crear(cedula=cedula, **datos)
            self.vista.mensaje('Estudiante guardado.')
        except ValueError as error:
            self.vista.mensaje(f'No se guardó: {error}')

    def ver_todos(self):
        estudiantes = self.modelo.listar()
        if estudiantes:
            self.vista.mostrar_tabla(estudiantes)
        else:
            self.vista.mensaje('Todavía no hay estudiantes.')

    def buscar_cedula(self):
        estudiante = self.modelo.buscar(input('Cédula: ').strip())
        if estudiante:
            self.vista.mostrar_ficha(estudiante)
        else:
            self.vista.mensaje('No existe ese estudiante.')

    def buscar_texto(self):
        resultados = self.modelo.buscar_texto(input('Texto a buscar: '))
        if resultados:
            self.vista.mostrar_tabla(resultados)
        else:
            self.vista.mensaje('Sin coincidencias.')

    def modificar(self):
        cedula = input('Cédula del estudiante a modificar: ').strip()
        estudiante = self.modelo.buscar(cedula)
        if not estudiante:
            self.vista.mensaje('No existe ese estudiante.')
            return
        self.vista.mostrar_ficha(estudiante)
        print('Deje vacío lo que no quiera cambiar.')
        try:
            self.modelo.actualizar(cedula, **self.vista.pedir_datos(estudiante))
            self.vista.mensaje('Estudiante modificado.')
        except ValueError as error:
            self.vista.mensaje(f'No se modificó: {error}')

    def borrar(self):
        cedula = input('Cédula del estudiante a borrar: ').strip()
        estudiante = self.modelo.buscar(cedula)
        if not estudiante:
            self.vista.mensaje('No existe ese estudiante.')
            return
        self.vista.mostrar_ficha(estudiante)
        if input('¿Borrar definitivamente? (s/n): ').strip().lower() == 's':
            self.modelo.eliminar(cedula)
            self.vista.mensaje('Estudiante borrado.')
        else:
            self.vista.mensaje('Operación cancelada.')

    def resumen(self):
        resumen = self.modelo.resumen_por_carrera()
        if resumen:
            self.vista.mostrar_resumen(resumen)
        else:
            self.vista.mensaje('Todavía no hay estudiantes.')

    def ejecutar(self):
        acciones = {'1': self.nuevo, '2': self.ver_todos, '3': self.buscar_cedula,
                    '4': self.buscar_texto, '5': self.modificar, '6': self.borrar,
                    '7': self.resumen}
        while True:
            opcion = self.vista.menu(self.modelo.total())
            if opcion == '0':
                self.vista.mensaje('Hasta pronto.')
                return
            accion = acciones.get(opcion)
            if accion:
                accion()
            else:
                self.vista.mensaje('Opción no válida.')
