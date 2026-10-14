from controlador import ControladorEstudiantes

if __name__ == '__main__':
    try:
        ControladorEstudiantes().ejecutar()
    except (KeyboardInterrupt, EOFError):
        print('\nPrograma interrumpido.')
