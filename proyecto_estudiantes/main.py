from shared.herramientas import (
    imprimir_titulo, imprimir_exito, imprimir_error, imprimir_info, confirmar
)
from views import ClienteController, EstudianteController


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


class MenuEstudiantes(MenuClientes):
    """VISTA de estudiantes: reutiliza el menú de clientes con otro controlador."""

    TITULO = "SISTEMA DE GESTIÓN DE ESTUDIANTES"
    ETIQUETA = "estudiante"
    ANCHO = 92

    def __init__(self, controlador=EstudianteController):
        super().__init__(controlador)
        # Opciones nuevas: 'Salir' se mantiene siempre al final
        self.agregar_opcion("8", "Agregar nota", self.agregar_nota)
        self.agregar_opcion("9", "Ver promedio", self.ver_promedio)
        self.agregar_opcion("10", "Materias en común", self.materias_en_comun)
        self.agregar_opcion("11", "Inscribir materia", self.inscribir_materia)
        self.agregar_opcion("12", "Materias ofertadas", self.materias_ofertadas)

    # ===== ESTÁTICO =====
    @staticmethod
    def pedir_nota(etiqueta):
        """Devuelve un número (int o float) o None si no es un número."""
        try:
            valor = float(input(etiqueta).replace(",", "."))
        except ValueError:
            return None
        return int(valor) if valor.is_integer() else valor

    # ===== AYUDA: pide un id y devuelve el estudiante (o None tras avisar) =====
    def _pedir_estudiante(self, etiqueta="Id del estudiante: "):
        id_estudiante = self.pedir_entero(etiqueta)
        if id_estudiante is None:
            imprimir_error("El id debe ser un número entero")
            return None
        estudiante = self.controlador.obtener(id_estudiante)
        if estudiante is None:
            imprimir_error(f"No existe un estudiante con id {id_estudiante}")
        return estudiante

    # ===== SOBRESCRITURAS (polimorfismo): mismo nombre, otra presentación =====
    def mostrar_tabla(self, estudiantes):
        print(f"{'ID':<5}{'NOMBRE':<25}{'EMAIL':<28}{'CARNET':<14}{'PROMEDIO':<10}{'ESTADO':<10}")
        print("-" * self.ANCHO)
        for e in estudiantes:
            print(f"{e.id:<5}{e.nombre_completo:<25}{e.email:<28}"
                  f"{e.carnet:<14}{e.promedio:<10}{e.estado:<10}")
        print("-" * self.ANCHO)
        imprimir_info(f"Total: {len(estudiantes)} estudiante(s)")

    def ver_por_id(self):
        imprimir_titulo("VER ESTUDIANTE POR ID")
        estudiante = self._pedir_estudiante()
        if estudiante is not None:
            for clave, valor in estudiante.a_diccionario().items():
                print(f"  {clave.capitalize():<12}: {valor}")
            imprimir_info(f"Promedio: {estudiante.promedio} - {estudiante.estado}")
        self.pausa()

    def estadisticas(self):
        imprimir_titulo("ESTADÍSTICAS")
        datos = self.controlador.estadisticas()
        print(f"  Estudiantes registrados : {datos['total']}")
        print(f"  Materias ofertadas      : {', '.join(datos['materias']) or '-'}")
        print(f"  Aprobados  ({len(datos['aprobados'])})          : {', '.join(datos['aprobados']) or '-'}")
        print(f"  Reprobados ({len(datos['reprobados'])})          : {', '.join(datos['reprobados']) or '-'}")
        self.pausa()

    # ===== OPCIONES NUEVAS =====
    def agregar_nota(self):
        imprimir_titulo("AGREGAR NOTA")
        estudiante = self._pedir_estudiante()
        if estudiante is None:
            return self.pausa()

        imprimir_info(f"Estudiante: {estudiante.nombre_completo}")
        materia = input("Materia: ")
        nota = self.pedir_nota("Nota (0-20): ")
        if nota is None:
            imprimir_error("La nota debe ser un número")
            return self.pausa()

        self.mostrar_resultado(*self.controlador.agregar_nota(estudiante.id, materia, nota))
        self.pausa()

    def ver_promedio(self):
        imprimir_titulo("PROMEDIO DEL ESTUDIANTE")
        estudiante = self._pedir_estudiante()
        if estudiante is None:
            return self.pausa()

        imprimir_info(f"{estudiante.nombre_completo} ({estudiante.carnet})")
        for materia in sorted(estudiante.materias):
            notas = estudiante.notas_de(materia)
            print(f"  {materia:<20}: {notas if notas else 'sin notas'}")
        if not estudiante.materias:
            print("  Todavía no tiene materias.")
        imprimir_info(f"Promedio general: {estudiante.promedio} - {estudiante.estado}")
        self.pausa()

    def materias_en_comun(self):
        imprimir_titulo("MATERIAS EN COMÚN")
        primero = self._pedir_estudiante("Id del primer estudiante: ")
        if primero is None:
            return self.pausa()
        segundo = self._pedir_estudiante("Id del segundo estudiante: ")
        if segundo is None:
            return self.pausa()

        comunes = self.controlador.materias_en_comun(primero.id, segundo.id)
        if comunes:
            imprimir_exito(f"Materias en común: {', '.join(sorted(comunes))}")
        else:
            imprimir_info("No comparten ninguna materia.")
        self.pausa()

    def inscribir_materia(self):
        imprimir_titulo("INSCRIBIR MATERIA")
        estudiante = self._pedir_estudiante()
        if estudiante is None:
            return self.pausa()

        materia = input("Materia: ")
        self.mostrar_resultado(*self.controlador.inscribir_materia(estudiante.id, materia))
        self.pausa()

    def materias_ofertadas(self):
        imprimir_titulo("MATERIAS OFERTADAS")
        materias = self.controlador.materias_ofertadas()
        if not materias:
            imprimir_info("Todavía no hay materias inscritas.")
        else:
            for materia in sorted(materias):
                print(f"  - {materia}")
            imprimir_info(f"Total: {len(materias)} materia(s) distintas")
        self.pausa()


if __name__ == "__main__":
    try:
        MenuEstudiantes().ejecutar()      # mismo menú base, con el controlador de estudiantes
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
