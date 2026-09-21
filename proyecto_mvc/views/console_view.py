"""Vista (MVC) — Toda la entrada/salida de consola vive aquí.

La Vista NUNCA contiene lógica de negocio: solo muestra datos que
recibe del Controlador y recolecta datos que el usuario escribe.
"""


class ConsoleView:

    def mostrar_titulo(self, texto):
        print("\n" + "=" * 60)
        print(texto)
        print("=" * 60)

    def mostrar_menu(self, opciones):
        self.mostrar_titulo("APP MVC — 40 Ejercicios de Clases y Colecciones")
        for numero, nombre in opciones:
            print(f"  {numero:>2}. {nombre}")
        print("   0. Salir")

    def pedir_opcion(self):
        return input("\nElige una opción: ").strip()

    def mostrar_resultado(self, titulo, entrada, salida):
        print(f"\n--- {titulo} ---")
        print(f"Entrada : {entrada}")
        print(f"Salida  : {salida}")

    def mostrar_mensaje(self, mensaje):
        print(mensaje)

    def mostrar_error(self, mensaje):
        print(f"[ERROR] {mensaje}")

    def pausar(self):
        input("\nPresiona ENTER para volver al menú...")
