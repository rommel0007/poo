from modelo import ModeloClientes
from vista import VistaClientes


class ControladorClientes:
    def __init__(self):
        self.modelo = ModeloClientes()
        self.vista = VistaClientes()

    def nuevo(self):
        cedula = input('Cédula (10 dígitos): ').strip()
        datos = self.vista.pedir_datos()
        try:
            self.modelo.crear(cedula=cedula, **datos)
            self.vista.mensaje('Cliente guardado.')
        except ValueError as error:
            self.vista.mensaje(f'No se guardó: {error}')

    def ver_todos(self):
        clientes = self.modelo.listar()
        if clientes:
            self.vista.mostrar_tabla(clientes)
        else:
            self.vista.mensaje('Todavía no hay clientes.')

    def buscar_cedula(self):
        cliente = self.modelo.buscar(input('Cédula: ').strip())
        if cliente:
            self.vista.mostrar_ficha(cliente)
        else:
            self.vista.mensaje('No existe ese cliente.')

    def buscar_texto(self):
        resultados = self.modelo.buscar_texto(input('Texto a buscar: '))
        if resultados:
            self.vista.mostrar_tabla(resultados)
        else:
            self.vista.mensaje('Sin coincidencias.')

    def modificar(self):
        cedula = input('Cédula del cliente a modificar: ').strip()
        cliente = self.modelo.buscar(cedula)
        if not cliente:
            self.vista.mensaje('No existe ese cliente.')
            return
        self.vista.mostrar_ficha(cliente)
        print('Deje vacío lo que no quiera cambiar.')
        try:
            self.modelo.actualizar(cedula, **self.vista.pedir_datos(cliente))
            self.vista.mensaje('Cliente modificado.')
        except ValueError as error:
            self.vista.mensaje(f'No se modificó: {error}')

    def borrar(self):
        cedula = input('Cédula del cliente a borrar: ').strip()
        cliente = self.modelo.buscar(cedula)
        if not cliente:
            self.vista.mensaje('No existe ese cliente.')
            return
        self.vista.mostrar_ficha(cliente)
        if input('¿Borrar definitivamente? (s/n): ').strip().lower() == 's':
            self.modelo.eliminar(cedula)
            self.vista.mensaje('Cliente borrado.')
        else:
            self.vista.mensaje('Operación cancelada.')

    def ejecutar(self):
        acciones = {'1': self.nuevo, '2': self.ver_todos, '3': self.buscar_cedula,
                    '4': self.buscar_texto, '5': self.modificar, '6': self.borrar}
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
