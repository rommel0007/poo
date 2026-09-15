"""Controlador (MVC) — Orquesta: recibe la acción del usuario (Vista),
invoca a los Modelos y decide qué mostrar (Vista). No contiene reglas
de negocio (eso vive en /models) ni imprime directamente (eso vive en /views).
"""

from models.numero_primo import NumeroPrimo
from models.matematicas import AnalizadorNumeros, SelectorRango, DivisorFinder, CalculadorDistancia
from models.texto import (
    AnalizadorTexto, InversorSecuencia, AnalizadorString,
    CombinadorListas, CodificadorCesar, AnalizadorPatrones,
)
from models.personas import (
    Calificador, GestorTemperatura, GestorPersonas, Equipos,
    RegistroNotas, AgrupadorEdades,
)
from models.gestion import CarroCompras, Tareas, ContadorFrecuencia, Inventario
from views.console_view import ConsoleView


class AppController:

    def __init__(self):
        self.view = ConsoleView()
        # Cada entrada: (número, nombre, método demo)
        self.ejercicios = [
            (0, "Modelo — Números primos", self.demo_ej0),
            (1, "Validador de notas con promedio", self.demo_ej1),
            (2, "Contador de palabras únicas", self.demo_ej2),
            (3, "Gestor de compras con totales", self.demo_ej3),
            (4, "Inversor de secuencias", self.demo_ej4),
            (5, "Detector de números pares e impares", self.demo_ej5),
            (6, "Estadísticas de temperatura", self.demo_ej6),
            (7, "Mapeador de edades", self.demo_ej7),
            (8, "Asignador de equipos", self.demo_ej8),
            (9, "Validador de caracteres", self.demo_ej9),
            (10, "Gestor de tareas con prioridad", self.demo_ej10),
            (11, "Contador de frecuencia", self.demo_ej11),
            (12, "Selector de rango con tuplas", self.demo_ej12),
            (13, "Combinador de listas", self.demo_ej13),
            (14, "Mapeo de estudiantes a notas", self.demo_ej14),
            (15, "Divisores de un número", self.demo_ej15),
            (16, "Codificador/Decodificador César", self.demo_ej16),
            (17, "Grupo de edades", self.demo_ej17),
            (18, "Matriz de distancias", self.demo_ej18),
            (19, "Inventario de productos", self.demo_ej19),
            (20, "Analizador de patrones en textos", self.demo_ej20),
        ]

    def ejecutar(self):
        while True:
            opciones = [(n, nombre) for n, nombre, _ in self.ejercicios]
            self.view.mostrar_menu(opciones)
            eleccion = self.view.pedir_opcion()

            if eleccion == "0":
                self.view.mostrar_mensaje("\n¡Hasta luego!")
                break

            encontrado = False
            for numero, nombre, demo in self.ejercicios:
                if eleccion == str(numero):
                    encontrado = True
                    try:
                        demo()
                    except Exception as error:
                        self.view.mostrar_error(str(error))
                    self.view.pausar()
                    break

            if not encontrado:
                self.view.mostrar_error("Opción inválida.")

    # ---------- Demostraciones (una por ejercicio) ----------

    def demo_ej0(self):
        modelo = NumeroPrimo()
        modelo.es_primo(7)
        primos = modelo.primos_en_rango(10, 11, 12, 13, 14, 15)
        self.view.mostrar_resultado(
            "Ej. 0 — Números primos",
            "primos_en_rango(10,11,12,13,14,15)",
            f"{primos} | historial={modelo.historial} | verificados={modelo.cantidad_verificados()}",
        )

    def demo_ej1(self):
        modelo = Calificador()
        validas = modelo.cargar_notas(85, 92, 110, 78, -5, 88)
        self.view.mostrar_resultado(
            "Ej. 1 — Calificador",
            "cargar_notas(85, 92, 110, 78, -5, 88)",
            f"válidas={validas} | promedio={modelo.promedio()}",
        )

    def demo_ej2(self):
        modelo = AnalizadorTexto()
        modelo.agregar_multiples("hola", "mundo", "hola")
        self.view.mostrar_resultado(
            "Ej. 2 — AnalizadorTexto",
            'agregar_multiples("hola","mundo","hola")',
            f"palabras únicas={modelo.contar_palabras()}",
        )

    def demo_ej3(self):
        modelo = CarroCompras()
        modelo.agregar_articulo("pan", 2.50)
        modelo.agregar_articulo("leche", 3.00)
        self.view.mostrar_resultado(
            "Ej. 3 — CarroCompras",
            'agregar_articulo("pan",2.50); agregar_articulo("leche",3.00)',
            f"total={modelo.total_carrito()}",
        )

    def demo_ej4(self):
        modelo = InversorSecuencia()
        self.view.mostrar_resultado(
            "Ej. 4 — InversorSecuencia",
            "invertir_lista([1,2,3])",
            f"{modelo.invertir_lista([1, 2, 3])}",
        )

    def demo_ej5(self):
        modelo = AnalizadorNumeros()
        resultado = modelo.separar(1, 2, 3, 4, 5)
        self.view.mostrar_resultado(
            "Ej. 5 — AnalizadorNumeros",
            "separar(1,2,3,4,5)",
            f"{resultado} | cantidad={modelo.cantidad_pares_impares()}",
        )

    def demo_ej6(self):
        modelo = GestorTemperatura()
        modelo.registrar_multiples(20, 25, 18, 30)
        self.view.mostrar_resultado(
            "Ej. 6 — GestorTemperatura",
            "registrar_multiples(20,25,18,30)",
            f"min={modelo.minima()} max={modelo.maxima()} promedio={modelo.promedio()}",
        )

    def demo_ej7(self):
        modelo = GestorPersonas()
        modelo.agregar_persona("Ana", 28)
        modelo.agregar_persona("Bob", 17)
        self.view.mostrar_resultado(
            "Ej. 7 — GestorPersonas",
            'agregar_persona("Ana",28); agregar_persona("Bob",17)',
            f"mayores de 18={modelo.personas_mayores(18)} | promedio={modelo.edad_promedio()}",
        )

    def demo_ej8(self):
        modelo = Equipos()
        modelo.crear_equipo("A")
        modelo.agregar_jugador("A", "Juan")
        modelo.agregar_jugador("A", "Pedro")
        modelo.crear_equipo("B")
        modelo.agregar_jugador("B", "Luis")
        self.view.mostrar_resultado(
            "Ej. 8 — Equipos",
            'equipo "A"=[Juan,Pedro] | equipo "B"=[Luis]',
            f"equipo con más integrantes={modelo.equipo_mayor_integrantes()}",
        )

    def demo_ej9(self):
        modelo = AnalizadorString()
        conteo = modelo.contar_por_tipo("Hola123")
        self.view.mostrar_resultado(
            "Ej. 9 — AnalizadorString",
            'contar_por_tipo("Hola123")',
            f"{conteo}",
        )

    def demo_ej10(self):
        modelo = Tareas()
        modelo.agregar_tarea("Estudiar", "alta")
        modelo.agregar_tarea("Leer", "baja")
        self.view.mostrar_resultado(
            "Ej. 10 — Tareas",
            'agregar_tarea("Estudiar","alta"); agregar_tarea("Leer","baja")',
            f"prioritarias={modelo.tareas_prioritarias()}",
        )

    def demo_ej11(self):
        modelo = ContadorFrecuencia()
        for elemento in ("a", "b", "a"):
            modelo.agregar_elemento(elemento)
        self.view.mostrar_resultado(
            "Ej. 11 — ContadorFrecuencia",
            'agregar_elemento("a"); agregar_elemento("b"); agregar_elemento("a")',
            f"más frecuente={modelo.elemento_mas_frecuente()}",
        )

    def demo_ej12(self):
        modelo = SelectorRango()
        resultado = modelo.elementos_en_multiples_rangos((1, 3), (2, 4))
        self.view.mostrar_resultado(
            "Ej. 12 — SelectorRango",
            "elementos_en_multiples_rangos((1,3), (2,4))",
            f"{resultado}",
        )

    def demo_ej13(self):
        modelo = CombinadorListas()
        self.view.mostrar_resultado(
            "Ej. 13 — CombinadorListas",
            "intercalar([1,2], [3,4])",
            f"{modelo.intercalar([1, 2], [3, 4])}",
        )

    def demo_ej14(self):
        modelo = RegistroNotas()
        modelo.registrar("Ana", 95)
        modelo.registrar("Bob", 70)
        self.view.mostrar_resultado(
            "Ej. 14 — RegistroNotas",
            'registrar("Ana",95); registrar("Bob",70)',
            f"mejor estudiante={modelo.mejor_estudiante()}",
        )

    def demo_ej15(self):
        modelo = DivisorFinder()
        self.view.mostrar_resultado(
            "Ej. 15 — DivisorFinder",
            "encontrar_divisores(12)",
            f"{modelo.encontrar_divisores(12)} | ¿6 es perfecto?={modelo.es_perfecto(6)}",
        )

    def demo_ej16(self):
        modelo = CodificadorCesar()
        codificada = modelo.codificar_palabra("hola", 3)
        self.view.mostrar_resultado(
            "Ej. 16 — CodificadorCesar",
            'codificar_palabra("hola", 3)',
            f"{codificada} | historial={modelo.historial}",
        )

    def demo_ej17(self):
        modelo = AgrupadorEdades()
        resultado = modelo.agrupar_por_categoria(5, 15, 30, 70)
        self.view.mostrar_resultado(
            "Ej. 17 — AgrupadorEdades",
            "agrupar_por_categoria(5, 15, 30, 70)",
            f"{resultado}",
        )

    def demo_ej18(self):
        modelo = CalculadorDistancia()
        distancia = modelo.distancia_euclidiana((0, 0), (3, 4))
        self.view.mostrar_resultado(
            "Ej. 18 — CalculadorDistancia",
            "distancia_euclidiana((0,0), (3,4))",
            f"{distancia}",
        )

    def demo_ej19(self):
        modelo = Inventario()
        modelo.agregar_stock("pan", 50)
        pudo_restar = modelo.restar_stock("pan", 30)
        bajo_stock = modelo.productos_bajo_stock(15)
        self.view.mostrar_resultado(
            "Ej. 19 — Inventario",
            'agregar_stock("pan",50); restar_stock("pan",30); productos_bajo_stock(15)',
            f"restó={pudo_restar} | bajo stock={bajo_stock}",
        )

    def demo_ej20(self):
        modelo = AnalizadorPatrones()
        resultado = modelo.agrupar_por_longitud("el gato esta aqui")
        self.view.mostrar_resultado(
            "Ej. 20 — AnalizadorPatrones",
            'agrupar_por_longitud("el gato esta aqui")',
            f"{resultado} | únicas={modelo.palabras_unicas()}",
        )
