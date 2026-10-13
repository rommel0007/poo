# Gestión de Clientes - POO y JSON (patrón MVC)

CRUD de consola en Python que guarda los clientes en `clientes.json`.

## Archivos
- `cliente.py`: clase `Cliente` con validación en propiedades y fecha de registro automática.
- `modelo.py`: lectura/escritura JSON y operaciones CRUD.
- `vista.py`: menú, tabla y ficha por consola.
- `controlador.py`: une vista y modelo, y maneja los errores de validación.
- `main.py`: punto de entrada (`python main.py`).

## Reglas
- Cédula: 10 dígitos, sin repetirse.
- Teléfono: 7 a 10 dígitos. Correo con formato válido.
- Se guarda `fecha_registro` automáticamente. Se usa `ciudad` en lugar de dirección.
- Listado ordenado por apellido y búsqueda por texto (nombre, apellido o ciudad).

## Pruebas sugeridas
Crear, listar, buscar por cédula y por texto, modificar, borrar, probar datos inválidos (cédula corta, correo sin @) y reiniciar para comprobar la persistencia.
