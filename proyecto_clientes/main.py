from shared.herramientas import (
    imprimir_titulo, imprimir_exito, imprimir_error, imprimir_info, confirmar
)
from views import ClienteController


class MenuClientes:
    """VISTA: muestra, pide y presenta. No decide reglas del negocio."""

    TITULO = "SISTEMA DE GESTIÓN DE CLIENTES"     # atributo de clase
    ETIQUETA = "cliente"                          # cómo se llama el registro en los mensajes
    ANCHO = 85

    def __init__(self, controlador=ClienteController):
        # ATRIBUTOS DE INSTANCIA: estado de ESTE menú
        self.__controlador = controlador
        self.__activo = True
        # DICCIONARIO tecla -> (texto, método). Reemplaza al if/elif largo.
        self.__opciones = {
            "1": (f"Crear {self.ETIQUETA}", self.crear),
            "2": ("Ver todos", self.listar),
            "3": ("Buscar", self.buscar),
            "4": ("Ver por id", self.ver_por_id),
            "5": ("Actualizar", self.actualizar),
            "6": ("Eliminar", self.eliminar),
            "7": ("Estadísticas", self.estadisticas),
            "8": (f"{self.ETIQUETA.capitalize()}s por ciudad", self.por_ciudad),
            "0": ("Salir", self.salir),
        }

    # ===== ACCESO PARA SUBCLASES =====
    @property
    def controlador(self):
        return self.__controlador

    def agregar_opcion(self, tecla, texto, metodo):
        """Agrega una opción al menú dejando 'Salir' siempre al final."""
        salir = self.__opciones.pop("0")
        self.__opciones[tecla] = (texto, metodo)
        self.__opciones["0"] = salir

    # ===== ESTÁTICOS: utilidades de pantalla, no dependen del menú =====
    @staticmethod
    def pausa():
        input("\nPresione Enter para continuar...")

    @staticmethod
    def pedir_entero(etiqueta):
        """Devuelve un entero o None si el usuario escribió cualquier otra cosa."""
        try:
            return int(input(etiqueta))
        except ValueError:
            return None

    @staticmethod
    def mostrar_resultado(exito, mensaje):
        if exito:
            imprimir_exito(mensaje)
        else:
            imprimir_error(mensaje)

    # ===== MÉTODOS DE INSTANCIA =====
    def mostrar_tabla(self, clientes):
        print(f"{'ID':<5}{'NOMBRE':<25}{'EMAIL':<28}{'CIUDAD':<15}{'TELÉFONO':<12}")
        print("-" * self.ANCHO)
        for cliente in clientes:
            print(f"{cliente.id:<5}{cliente.nombre_completo:<25}"
                  f"{cliente.email:<28}{cliente.ciudad:<15}{cliente.telefono:<12}")
        print("-" * self.ANCHO)
        imprimir_info(f"Total: {len(clientes)} {self.ETIQUETA}(s)")

    def crear(self):
        imprimir_titulo(f"CREAR NUEVO {self.ETIQUETA.upper()}")
        # Recorro la TUPLA de campos del Modelo: si el Modelo cambia, el formulario también
        datos = {}
        for campo in self.__controlador.MODELO.CAMPOS:
            datos[campo] = input(f"{campo.capitalize()}: ")

        exito, mensaje = self.__controlador.crear(datos)
        self.mostrar_resultado(exito, mensaje)
        self.pausa()

    def listar(self):
        imprimir_titulo(f"LISTA DE {self.ETIQUETA.upper()}S")
        registros = self.__controlador.listar()
        if not registros:
            imprimir_info(f"Todavía no hay {self.ETIQUETA}s. Use la opción 1 para crear el primero.")
        else:
            self.mostrar_tabla(registros)
        self.pausa()

    def buscar(self):
        imprimir_titulo(f"BUSCAR {self.ETIQUETA.upper()}")
        termino = input("Texto a buscar: ")
        encontrados = self.__controlador.buscar(termino)
        if not encontrados:
            imprimir_info(f"Ningún {self.ETIQUETA} coincide con '{termino}'.")
        else:
            self.mostrar_tabla(encontrados)
        self.pausa()

    def ver_por_id(self):
        imprimir_titulo(f"VER {self.ETIQUETA.upper()} POR ID")
        id_registro = self.pedir_entero(f"Id del {self.ETIQUETA}: ")
        if id_registro is None:
            imprimir_error("El id debe ser un número entero")
            return self.pausa()

        objeto = self.__controlador.obtener(id_registro)
        if objeto is None:
            imprimir_error(f"No existe un {self.ETIQUETA} con id {id_registro}")
        else:
            for clave, valor in objeto.a_diccionario().items():
                print(f"  {clave.capitalize():<12}: {valor}")
            imprimir_info(f"Dominio del email: {objeto.dominio_email}")
            imprimir_info(f"Iniciales: {objeto.iniciales}")
        self.pausa()

    def actualizar(self):
        imprimir_titulo(f"ACTUALIZAR {self.ETIQUETA.upper()}")
        id_registro = self.pedir_entero(f"Id del {self.ETIQUETA}: ")
        if id_registro is None:
            imprimir_error("El id debe ser un número entero")
            return self.pausa()

        objeto = self.__controlador.obtener(id_registro)
        if objeto is None:
            imprimir_error(f"No existe un {self.ETIQUETA} con id {id_registro}")
            return self.pausa()

        imprimir_info(f"Editando a {objeto.nombre_completo}")
        print("Deje en blanco el campo que no quiera cambiar.\n")

        cambios = {}
        for campo in self.__controlador.MODELO.CAMPOS:
            actual = getattr(objeto, campo)          # lee la PROPIEDAD
            nuevo = input(f"{campo.capitalize()} [{actual}]: ").strip()
            if nuevo:
                cambios[campo] = nuevo

        self.mostrar_resultado(*self.__controlador.actualizar(id_registro, cambios))
        self.pausa()

    def eliminar(self):
        imprimir_titulo(f"ELIMINAR {self.ETIQUETA.upper()}")
        id_registro = self.pedir_entero(f"Id del {self.ETIQUETA}: ")
        if id_registro is None:
            imprimir_error("El id debe ser un número entero")
            return self.pausa()

        objeto = self.__controlador.obtener(id_registro)
        if objeto is None:
            imprimir_error(f"No existe un {self.ETIQUETA} con id {id_registro}")
            return self.pausa()

        imprimir_info(f"Se eliminará: {objeto}")
        if confirmar("¿Confirma la eliminación?"):
            self.mostrar_resultado(*self.__controlador.eliminar(id_registro))
        else:
            imprimir_info("Operación cancelada")
        self.pausa()

    def estadisticas(self):
        imprimir_titulo("ESTADÍSTICAS")
        datos = self.__controlador.estadisticas()
        print(f"  Clientes registrados : {datos['total']}")
        print(f"  Ciudades distintas   : {len(datos['ciudades'])} -> {', '.join(datos['ciudades'])}")
        print(f"  Dominios de email    : {', '.join(datos['dominios'])}")
        print(f"  Sin teléfono         : {len(datos['sin_telefono'])}")
        self.pausa()

    def por_ciudad(self):
        imprimir_titulo("CLIENTES POR CIUDAD")
        for ciudad, nombres in self.__controlador.agrupar_por_ciudad().items():
            print(f"  {ciudad}: {', '.join(nombres)}")
        self.pausa()

    def salir(self):
        self.__activo = False          # cambia el estado del objeto
        imprimir_info("¡Hasta luego! 👋")

    def mostrar_menu(self):
        imprimir_titulo(self.TITULO)
        for tecla, (texto, _metodo) in self.__opciones.items():
            print(f"  {tecla}. {texto}")
        print()

    def ejecutar(self):
        """El bucle principal: vive mientras __activo sea True."""
        while self.__activo:
            self.mostrar_menu()
            tecla = input("Seleccione una opción: ").strip()

            if tecla not in self.__opciones:
                imprimir_error("Opción no válida")
                self.pausa()
                continue

            _texto, metodo = self.__opciones[tecla]
            metodo()          # el diccionario guarda el método: aquí se ejecuta


if __name__ == "__main__":
    try:
        MenuClientes().ejecutar()      # se crea el objeto y se lo pone a correr
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
