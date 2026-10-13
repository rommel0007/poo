from controlador import ControladorClientes

if __name__ == '__main__':
    try:
        ControladorClientes().ejecutar()
    except (KeyboardInterrupt, EOFError):
        print('\nPrograma interrumpido.')
