"""Controlador (MVC) — Orquesta: recibe la acción del usuario (Vista),
invoca a los Modelos y decide qué mostrar (Vista). No contiene reglas
de negocio (eso vive en /models) ni imprime directamente (eso vive en /views).
"""

from models.numero_primo import NumeroPrimo
from models.matematicas import ClasificadorSigno, GeneradorTablas, Factorizador, CalculadorPerimetro
from models.texto import (
    DetectorDuplicados, RotadorSecuencia, ClasificadorCaracteres,
    DivisorBloques, CodificadorNumerico, AnalizadorFrases,
)
from models.personas import (
    ValidadorPuntajes, GestorVentas, GestorAlturas, Aulas,
    RegistroPeliculas, AgrupadorSalarios,
)
from models.gestion import GestorCuentas, Agenda, UrnaVotos, Biblioteca
# ---- EJERCICIOS AGREGADOS (21-40) — todos juntos en un solo archivo ----
from models.ejercicios_adicionales import (
    CalculadoraIVA, SumadorSerie, GeneradorPotencias,
    CalculadoraArea, VerificadorBisiesto,
    ContadorLetras, LimpiadorTexto, GeneradorUsuarios,
    FormateadorNombres, BuscadorPalabras,
    RegistroClimas, GestorDeudas, ClasificadorTriangulos,
    ConversorRomanos, GestorAmigos,
    GestorAsientos, TablaPuntos, OperadorMatrices,
    ConversorTiempo, ListaInvitados,
)
from views.console_view import ConsoleView


class AppController:

    def __init__(self):
        self.view = ConsoleView()
        # Cada entrada: (número, nombre, método demo)
        self.ejercicios = [
            (0, "Modelo — Números primos", self.demo_ej0),
            (1, "Validador de puntajes con promedio", self.demo_ej1),
            (2, "Detector de palabras duplicadas", self.demo_ej2),
            (3, "Gestor de cuentas bancarias", self.demo_ej3),
            (4, "Rotador de secuencias", self.demo_ej4),
            (5, "Clasificador de números por signo", self.demo_ej5),
            (6, "Estadísticas de ventas diarias", self.demo_ej6),
            (7, "Mapeador de alturas", self.demo_ej7),
            (8, "Asignador de aulas", self.demo_ej8),
            (9, "Clasificador de caracteres", self.demo_ej9),
            (10, "Agenda de citas", self.demo_ej10),
            (11, "Urna de votos", self.demo_ej11),
            (12, "Generador de tablas de multiplicar", self.demo_ej12),
            (13, "Divisor de listas en bloques", self.demo_ej13),
            (14, "Mapeo de películas a puntuación", self.demo_ej14),
            (15, "Factores primos, MCD y MCM", self.demo_ej15),
            (16, "Codificador numérico (a=1 ... z=26)", self.demo_ej16),
            (17, "Grupo de salarios", self.demo_ej17),
            (18, "Perímetro de polígonos", self.demo_ej18),
            (19, "Biblioteca de libros", self.demo_ej19),
            (20, "Analizador de frases", self.demo_ej20),
            # ---- EJERCICIOS AGREGADOS (21-40) — nuevos ----
            (21, "Calculadora de IVA", self.demo_ej21),
            (22, "Sumador de series", self.demo_ej22),
            (23, "Generador de potencias", self.demo_ej23),
            (24, "Calculadora de áreas", self.demo_ej24),
            (25, "Verificador de años bisiestos", self.demo_ej25),
            (26, "Contador de letras", self.demo_ej26),
            (27, "Limpiador de texto", self.demo_ej27),
            (28, "Generador de nombres de usuario", self.demo_ej28),
            (29, "Formateador de nombres", self.demo_ej29),
            (30, "Buscador de palabras", self.demo_ej30),
            (31, "Registro de climas por ciudad", self.demo_ej31),
            (32, "Gestor de deudas", self.demo_ej32),
            (33, "Clasificador de triángulos", self.demo_ej33),
            (34, "Conversor de números romanos", self.demo_ej34),
            (35, "Gestor de amigos", self.demo_ej35),
            (36, "Gestor de asientos", self.demo_ej36),
            (37, "Tabla de posiciones", self.demo_ej37),
            (38, "Operador de matrices", self.demo_ej38),
            (39, "Conversor de tiempo", self.demo_ej39),
            (40, "Lista de invitados", self.demo_ej40),
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
        modelo = ValidadorPuntajes()
        validos = modelo.cargar_puntajes(8, 9.5, 11, 7, -2, 10)
        self.view.mostrar_resultado(
            "Ej. 1 — ValidadorPuntajes",
            "cargar_puntajes(8, 9.5, 11, 7, -2, 10)",
            f"válidos={validos} | mejor={modelo.mejor_puntaje()} | promedio={modelo.promedio()}",
        )

    def demo_ej2(self):
        modelo = DetectorDuplicados()
        modelo.agregar_multiples("sol", "luna", "sol", "mar", "luna")
        self.view.mostrar_resultado(
            "Ej. 2 — DetectorDuplicados",
            'agregar_multiples("sol","luna","sol","mar","luna")',
            f"hay duplicados={modelo.hay_duplicados()} | repetidas={modelo.palabras_repetidas()}",
        )

    def demo_ej3(self):
        modelo = GestorCuentas()
        modelo.abrir_cuenta("Ana", 100)
        modelo.abrir_cuenta("Luis", 40)
        modelo.depositar("Ana", 50)
        pudo_retirar = modelo.retirar("Luis", 100)
        self.view.mostrar_resultado(
            "Ej. 3 — GestorCuentas",
            'abrir_cuenta("Ana",100); abrir_cuenta("Luis",40); depositar("Ana",50); retirar("Luis",100)',
            f"retiro exitoso={pudo_retirar} | saldo total={modelo.saldo_total()} | "
            f"saldo mayor a 100={modelo.cuentas_con_saldo_mayor(100)}",
        )

    def demo_ej4(self):
        modelo = RotadorSecuencia()
        rotada = modelo.rotar_lista([1, 2, 3, 4, 5], 2)
        self.view.mostrar_resultado(
            "Ej. 4 — RotadorSecuencia",
            "rotar_lista([1,2,3,4,5], 2)",
            f"{rotada}",
        )

    def demo_ej5(self):
        modelo = ClasificadorSigno()
        resultado = modelo.separar(4, -3, 0, 7, -8, 0, 2)
        self.view.mostrar_resultado(
            "Ej. 5 — ClasificadorSigno",
            "separar(4,-3,0,7,-8,0,2)",
            f"{resultado} | cantidades (pos,neg,cero)={modelo.cantidad_por_signo()}",
        )

    def demo_ej6(self):
        modelo = GestorVentas()
        modelo.registrar_multiples(120, 85, 240, 60)
        self.view.mostrar_resultado(
            "Ej. 6 — GestorVentas",
            "registrar_multiples(120,85,240,60)",
            f"máxima={modelo.venta_maxima()} | mínima={modelo.venta_minima()} | total={modelo.total()}",
        )

    def demo_ej7(self):
        modelo = GestorAlturas()
        modelo.agregar_persona("Ana", 1.65)
        modelo.agregar_persona("Bob", 1.82)
        modelo.agregar_persona("Eva", 1.74)
        self.view.mostrar_resultado(
            "Ej. 7 — GestorAlturas",
            'agregar_persona("Ana",1.65); ("Bob",1.82); ("Eva",1.74)',
            f"≥1.70 m={modelo.personas_mas_altas(1.70)} | promedio={modelo.altura_promedio():.2f}",
        )

    def demo_ej8(self):
        modelo = Aulas()
        modelo.crear_aula("A1")
        modelo.agregar_estudiante("A1", "Juan")
        modelo.agregar_estudiante("A1", "Pedro")
        modelo.crear_aula("B2")
        modelo.agregar_estudiante("B2", "Luis")
        existe = modelo.agregar_estudiante("C3", "Mario")
        self.view.mostrar_resultado(
            "Ej. 8 — Aulas",
            'aula "A1"=[Juan,Pedro] | aula "B2"=[Luis] | agregar a "C3" (no existe)',
            f"aula menos ocupada={modelo.aula_menos_ocupada()} | "
            f"agregó a C3={existe} | total estudiantes={modelo.total_estudiantes()}",
        )

    def demo_ej9(self):
        modelo = ClasificadorCaracteres()
        conteo = modelo.contar_por_tipo("Hola Mundo 2026!")
        self.view.mostrar_resultado(
            "Ej. 9 — ClasificadorCaracteres",
            'contar_por_tipo("Hola Mundo 2026!")',
            f"{conteo}",
        )

    def demo_ej10(self):
        modelo = Agenda()
        modelo.agregar_cita("lunes", "Dentista")
        modelo.agregar_cita("lunes", "Reunión")
        modelo.agregar_cita("martes", "Gimnasio")
        modelo.cancelar_cita("Reunión")
        self.view.mostrar_resultado(
            "Ej. 10 — Agenda",
            'agregar_cita x3; cancelar_cita("Reunión")',
            f"citas del lunes={modelo.citas_del_dia('lunes')} | total={modelo.total_citas()}",
        )

    def demo_ej11(self):
        modelo = UrnaVotos()
        for candidato in ("Rosa", "Pablo", "Rosa", "Rosa", "Pablo"):
            modelo.votar(candidato)
        self.view.mostrar_resultado(
            "Ej. 11 — UrnaVotos",
            'votar("Rosa") x3; votar("Pablo") x2',
            f"ganador={modelo.ganador()} | votos de Pablo={modelo.votos_candidato('Pablo')} "
            f"| total={modelo.total_votos()}",
        )

    def demo_ej12(self):
        modelo = GeneradorTablas()
        tabla = modelo.tabla(7)
        self.view.mostrar_resultado(
            "Ej. 12 — GeneradorTablas",
            "tabla(7) | suma_tabla(7) | tablas_multiples(2, 3)",
            f"{tabla} | suma={modelo.suma_tabla(7)} | {modelo.tablas_multiples(2, 3)}",
        )

    def demo_ej13(self):
        modelo = DivisorBloques()
        bloques = modelo.dividir_en_bloques([1, 2, 3, 4, 5, 6, 7], 3)
        self.view.mostrar_resultado(
            "Ej. 13 — DivisorBloques",
            "dividir_en_bloques([1,2,3,4,5,6,7], 3)",
            f"{bloques}",
        )

    def demo_ej14(self):
        modelo = RegistroPeliculas()
        modelo.registrar("Matrix", 9)
        modelo.registrar("Shrek", 8)
        modelo.registrar("Cars", 6)
        self.view.mostrar_resultado(
            "Ej. 14 — RegistroPeliculas",
            'registrar("Matrix",9); ("Shrek",8); ("Cars",6)',
            f"recomendadas (≥8)={modelo.peliculas_recomendadas(8)} | mejor={modelo.mejor_pelicula()}",
        )

    def demo_ej15(self):
        modelo = Factorizador()
        factores = modelo.factores_primos(360)
        self.view.mostrar_resultado(
            "Ej. 15 — Factorizador",
            "factores_primos(360) | mcd(48,36) | mcm(4,6) | mcd_multiples(12,18,24)",
            f"{factores} | mcd={modelo.mcd(48, 36)} | mcm={modelo.mcm(4, 6)} "
            f"| mcd múltiple={modelo.mcd_multiples(12, 18, 24)}",
        )

    def demo_ej16(self):
        modelo = CodificadorNumerico()
        numeros = modelo.palabra_a_numeros("hola")
        self.view.mostrar_resultado(
            "Ej. 16 — CodificadorNumerico",
            'palabra_a_numeros("hola")',
            f"{numeros} | decodificado={modelo.numeros_a_palabra(*numeros)}",
        )

    def demo_ej17(self):
        modelo = AgrupadorSalarios()
        grupos = modelo.agrupar_por_categoria(400, 900, 1600, 300, 2000)
        self.view.mostrar_resultado(
            "Ej. 17 — AgrupadorSalarios",
            "agrupar_por_categoria(400,900,1600,300,2000)",
            f"{grupos} | promedio bajo={modelo.salario_promedio_categoria('bajo')}",
        )

    def demo_ej18(self):
        modelo = CalculadorPerimetro()
        perimetro = modelo.perimetro((0, 0), (4, 0), (4, 3))
        self.view.mostrar_resultado(
            "Ej. 18 — CalculadorPerimetro",
            "perimetro((0,0),(4,0),(4,3)) | punto_medio((0,0),(4,2))",
            f"perímetro={perimetro} | punto medio={modelo.punto_medio((0, 0), (4, 2))} "
            f"| más lejano de (0,0)={modelo.punto_mas_lejano((0, 0), (1, 1), (5, 5), (2, 3))}",
        )

    def demo_ej19(self):
        modelo = Biblioteca()
        modelo.agregar_libro("Don Quijote", 1)
        modelo.agregar_libro("Rayuela", 2)
        modelo.prestar_libro("Don Quijote")
        segundo = modelo.prestar_libro("Don Quijote")
        self.view.mostrar_resultado(
            "Ej. 19 — Biblioteca",
            'agregar_libro("Don Quijote",1); ("Rayuela",2); prestar_libro("Don Quijote") x2',
            f"segundo préstamo exitoso={segundo} | agotados={modelo.libros_agotados()}",
        )

    def demo_ej20(self):
        modelo = AnalizadorFrases()
        texto = "casa carro mesa cielo"
        self.view.mostrar_resultado(
            "Ej. 20 — AnalizadorFrases",
            f'palabras_que_terminan_con("{texto}", "a") | agrupar_por_inicial',
            f"{modelo.palabras_que_terminan_con(texto, 'a')} | {modelo.agrupar_por_inicial(texto)}",
        )

    def demo_ej21(self):
        modelo = CalculadoraIVA()
        precios = modelo.precios_con_iva(100, 40, 25)
        self.view.mostrar_resultado(
            "Ej. 21 — CalculadoraIVA",
            "precios_con_iva(100, 40, 25)  (IVA 15%)",
            f"con IVA={precios} | IVA calculados={modelo.historial}",
        )

    def demo_ej22(self):
        modelo = SumadorSerie()
        self.view.mostrar_resultado(
            "Ej. 22 — SumadorSerie",
            "suma_hasta(10) | suma_pares(10) | suma_cuadrados(1,2,3)",
            f"{modelo.suma_hasta(10)} | {modelo.suma_pares(10)} | {modelo.suma_cuadrados(1, 2, 3)}",
        )

    def demo_ej23(self):
        modelo = GeneradorPotencias()
        self.view.mostrar_resultado(
            "Ej. 23 — GeneradorPotencias",
            "potencias(2, 8) | es_potencia_de(2, 64) | es_potencia_de(3, 50)",
            f"{modelo.potencias(2, 8)} | {modelo.es_potencia_de(2, 64)} | {modelo.es_potencia_de(3, 50)}",
        )

    def demo_ej24(self):
        modelo = CalculadoraArea()
        modelo.area_rectangulo(5, 3)
        modelo.area_triangulo(4, 6)
        modelo.area_circulo(2)
        self.view.mostrar_resultado(
            "Ej. 24 — CalculadoraArea",
            "area_rectangulo(5,3); area_triangulo(4,6); area_circulo(2)",
            f"áreas={modelo.calculos} | figura mayor={modelo.figura_mayor()}",
        )

    def demo_ej25(self):
        modelo = VerificadorBisiesto()
        self.view.mostrar_resultado(
            "Ej. 25 — VerificadorBisiesto",
            "bisiestos_en(1900, 2000, 2024, 2026) | dias_del_anio(2024)",
            f"{modelo.bisiestos_en(1900, 2000, 2024, 2026)} | {modelo.dias_del_anio(2024)} días",
        )

    def demo_ej26(self):
        modelo = ContadorLetras()
        self.view.mostrar_resultado(
            "Ej. 26 — ContadorLetras",
            'frecuencia("banana") | letra_mas_comun("banana")',
            f"{modelo.frecuencia('banana')} | más común={modelo.letra_mas_comun('banana')}",
        )

    def demo_ej27(self):
        modelo = LimpiadorTexto()
        limpio = modelo.quitar_espacios_extra("  hola    mundo   feliz ")
        self.view.mostrar_resultado(
            "Ej. 27 — LimpiadorTexto",
            'quitar_espacios_extra("  hola    mundo   feliz ") | quitar_vocales("programacion")',
            f"'{limpio}' | '{modelo.quitar_vocales('programacion')}'",
        )

    def demo_ej28(self):
        modelo = GeneradorUsuarios()
        usuarios = modelo.crear_multiples(("Ana", "Lopez"), ("Alberto", "Lopez"), ("Carlos", "Ruiz"))
        self.view.mostrar_resultado(
            "Ej. 28 — GeneradorUsuarios",
            'crear_multiples(("Ana","Lopez"), ("Alberto","Lopez"), ("Carlos","Ruiz"))',
            f"{usuarios} | total={modelo.total_usuarios()}",
        )

    def demo_ej29(self):
        modelo = FormateadorNombres()
        self.view.mostrar_resultado(
            "Ej. 29 — FormateadorNombres",
            'capitalizar_nombre("juan carlos perez") | iniciales(...)',
            f"'{modelo.capitalizar_nombre('juan carlos perez')}' | {modelo.iniciales('juan carlos perez')}",
        )

    def demo_ej30(self):
        modelo = BuscadorPalabras()
        texto = "el sol y el mar y el cielo"
        self.view.mostrar_resultado(
            "Ej. 30 — BuscadorPalabras",
            f'posiciones("{texto}", "el") | primera_posicion(..., "mar")',
            f"{modelo.posiciones(texto, 'el')} | {modelo.primera_posicion(texto, 'mar')}",
        )

    def demo_ej31(self):
        modelo = RegistroClimas()
        modelo.agregar_temperatura("Lima", 22)
        modelo.agregar_temperatura("Lima", 24)
        modelo.agregar_temperatura("Bogotá", 14)
        modelo.agregar_temperatura("Santiago", 18)
        self.view.mostrar_resultado(
            "Ej. 31 — RegistroClimas",
            'agregar_temperatura("Lima",22); ("Lima",24); ("Bogotá",14); ("Santiago",18)',
            f"promedio Lima={modelo.promedio_ciudad('Lima')} | más cálida={modelo.ciudad_mas_calida()}",
        )

    def demo_ej32(self):
        modelo = GestorDeudas()
        modelo.agregar_deuda("Ana", 100)
        modelo.agregar_deuda("Luis", 250)
        pago = modelo.pagar("Luis", 100)
        self.view.mostrar_resultado(
            "Ej. 32 — GestorDeudas",
            'agregar_deuda("Ana",100); agregar_deuda("Luis",250); pagar("Luis",100)',
            f"pago exitoso={pago} | total deudas={modelo.total_deudas()} | mayor deudor={modelo.mayor_deudor()}",
        )

    def demo_ej33(self):
        modelo = ClasificadorTriangulos()
        conteo = modelo.clasificar_multiples((3, 3, 3), (3, 3, 5), (3, 4, 5), (1, 2, 10))
        self.view.mostrar_resultado(
            "Ej. 33 — ClasificadorTriangulos",
            "clasificar_multiples((3,3,3),(3,3,5),(3,4,5),(1,2,10))",
            f"{conteo}",
        )

    def demo_ej34(self):
        modelo = ConversorRomanos()
        self.view.mostrar_resultado(
            "Ej. 34 — ConversorRomanos",
            'a_romano(2026) | a_entero("MCMXCIV")',
            f"{modelo.a_romano(2026)} | {modelo.a_entero('MCMXCIV')}",
        )

    def demo_ej35(self):
        modelo = GestorAmigos()
        modelo.agregar_amistad("Ana", "Bob")
        modelo.agregar_amistad("Ana", "Eva")
        modelo.agregar_amistad("Luis", "Bob")
        modelo.agregar_amistad("Luis", "Eva")
        self.view.mostrar_resultado(
            "Ej. 35 — GestorAmigos",
            "agregar_amistad: Ana-Bob, Ana-Eva, Luis-Bob, Luis-Eva",
            f"amigos de Ana={sorted(modelo.amigos_de('Ana'))} | "
            f"en común Ana y Luis={sorted(modelo.amigos_en_comun('Ana', 'Luis'))}",
        )

    def demo_ej36(self):
        modelo = GestorAsientos()
        modelo.comprar_asiento(1, 1)
        modelo.comprar_asiento(1, 2)
        repetido = modelo.comprar_asiento(1, 1)
        self.view.mostrar_resultado(
            "Ej. 36 — GestorAsientos",
            "comprar_asiento(1,1); (1,2); (1,1) otra vez | asientos_libres(2,2)",
            f"compra repetida exitosa={repetido} | libres={modelo.asientos_libres(2, 2)} "
            f"| vendidos={modelo.total_vendidos()}",
        )

    def demo_ej37(self):
        modelo = TablaPuntos()
        modelo.registrar_partido("Tigres", "Leones", 2, 1)
        modelo.registrar_partido("Águilas", "Leones", 0, 0)
        modelo.registrar_partido("Tigres", "Águilas", 1, 3)
        self.view.mostrar_resultado(
            "Ej. 37 — TablaPuntos",
            "Tigres 2-1 Leones; Águilas 0-0 Leones; Tigres 1-3 Águilas",
            f"tabla={modelo.tabla()} | líder={modelo.lider()}",
        )

    def demo_ej38(self):
        modelo = OperadorMatrices()
        matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.view.mostrar_resultado(
            "Ej. 38 — OperadorMatrices",
            "matriz 3x3 [[1,2,3],[4,5,6],[7,8,9]]",
            f"suma filas={modelo.sumar_filas(matriz)} | diagonal={modelo.suma_diagonal(matriz)} "
            f"| transpuesta={modelo.transponer(matriz)}",
        )

    def demo_ej39(self):
        modelo = ConversorTiempo()
        self.view.mostrar_resultado(
            "Ej. 39 — ConversorTiempo",
            "segundos_a_hms(3725) | sumar_tiempos((1,30,0),(0,45,30),(2,20,45))",
            f"{modelo.segundos_a_hms(3725)} | {modelo.sumar_tiempos((1, 30, 0), (0, 45, 30), (2, 20, 45))}",
        )

    def demo_ej40(self):
        modelo = ListaInvitados()
        modelo.agregar_invitado("Ana")
        modelo.agregar_invitado("Bob")
        modelo.agregar_invitado("Eva")
        repetido = modelo.agregar_invitado("Ana")
        modelo.confirmar("Ana")
        no_invitado = modelo.confirmar("Zoe")
        self.view.mostrar_resultado(
            "Ej. 40 — ListaInvitados",
            "agregar Ana, Bob, Eva, Ana otra vez; confirmar Ana; confirmar Zoe",
            f"Ana repetida agregada={repetido} | Zoe confirmada={no_invitado} "
            f"| pendientes={sorted(modelo.pendientes())}",
        )
