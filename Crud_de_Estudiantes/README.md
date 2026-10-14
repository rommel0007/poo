# Registro de Estudiantes - POO y JSON (patrón MVC)

CRUD de consola en Python que guarda los estudiantes en `estudiantes.json`.

## Archivos
- `estudiante.py`: clase `Estudiante` con validación en propiedades y fecha de ingreso automática.
- `modelo.py`: lectura/escritura JSON, operaciones CRUD, búsqueda y resumen por carrera.
- `vista.py`: menú, tabla, ficha y resumen por consola.
- `controlador.py`: une vista y modelo, y maneja los errores de validación.
- `main.py`: punto de entrada (`python main.py`).

## Reglas
- Cédula: 10 dígitos, sin repetirse. Correo válido y sin repetirse.
- Semestre: número entero de 1 a 10.
- Nombre, apellido y carrera obligatorios.

## Pruebas sugeridas
Crear, listar, buscar por cédula y por texto, modificar, borrar, ver el resumen por carrera, probar datos inválidos (cédula corta, semestre 15, correo repetido) y reiniciar para comprobar la persistencia.
