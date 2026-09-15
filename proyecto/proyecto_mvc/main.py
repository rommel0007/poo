"""Punto de entrada. Solo arranca el Controlador — no contiene lógica."""

from controllers.app_controller import AppController

if __name__ == "__main__":
    AppController().ejecutar()
