import os

CYAN = "\033[96m"
MAGENTA = "\033[95m"
BLANCO = "\033[97m"
MORADO = "\033[35m"
RESET = "\033[0m"


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def imprimir_color(texto, color):
    print(f"{color}{texto}{RESET}")


def imprimir_titulo(texto):
    print()
    imprimir_color("=" * 46, CYAN)
    imprimir_color(f"  {texto}", CYAN)
    imprimir_color("=" * 46, CYAN)


def imprimir_exito(texto):
    imprimir_color(f"✔ {texto}", BLANCO)


def imprimir_error(texto):
    imprimir_color(f"✘ {texto}", MAGENTA)


def imprimir_info(texto):
    imprimir_color(f"ℹ {texto}", MORADO)


def confirmar(pregunta):
    respuesta = input(f"{pregunta} (s/n): ").strip().lower()
    return respuesta in ("s", "si", "sí")
