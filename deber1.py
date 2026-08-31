#-----------------1-------------------.

#  ESCRIBIR EL CÓDIGO
def estadisticas(numeros, debug=False):
    if not numeros:
        if debug:
            print("[DEBUG] Lista vacía recibida.")
        return {
            "total": 0,
            "promedio": 0,
            "max": None,
            "min": None,
            "pares": 0
        }

    total = 0
    maximo = numeros[0]
    minimo = numeros[0]
    pares = 0

    if debug:
        print(f"[DEBUG INICIAL] max={maximo}, min={minimo}, total={total}, pares={pares}")

    for i, n in enumerate(numeros, start=1):
        total += n
        if n > maximo:
            maximo = n
        if n < minimo:
            minimo = n
        if n % 2 == 0:
            pares += 1

        if debug:
            print(f"  [Paso {i}] Elemento: {n:<2} -> Acumulado={total:<2} | Max={maximo:<2} | Min={minimo:<2} | Pares={pares}")

    promedio = total / len(numeros)

    return {
        "total": total,
        "promedio": promedio,
        "max": maximo,
        "min": minimo,
        "pares": pares
    }

# Uso y casos de prueba
if __name__ == "__main__":
    print("=== CASO 1: Lista de la guía (con depuración) ===")
    datos = [8, 5, 12, 7, 3, 10]
    r = estadisticas(datos, debug=True)
    print("\nResultado obtenido:", r)
    print(f"Promedio: {r['promedio']:.2f}")

    print("\n=== CASO 2: Lista con números negativos ===")
    datos_neg = [-5, -2, -10, -8]
    resultado_neg = estadisticas(datos_neg, debug=False)
    print("Entrada:", datos_neg)
    print("Resultado:", resultado_neg)

    print("\n=== CASO 3: Lista vacía ===")
    resultado_vacio = estadisticas([], debug=False)
    print("Entrada: []")
    print("Resultado:", resultado_vacio)
    
    
    
    
#-----------------2-------------------.




#  ESCRIBIR EL CÓDIGO
def contar_unicas(texto, debug=False):
    # Normalizamos a minúsculas
    texto = texto.lower()

    # Eliminamos signos de puntuación
    for signo in ".,;:!?\"'()":
        texto = texto.replace(signo, "")

    if debug:
        print(f"[DEBUG] Texto limpio: '{texto}'")

    # Contamos con diccionario
    frecuencias = {}
    palabras = texto.split()

    for i, palabra in enumerate(palabras, start=1):
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
        if debug:
            print(f"  [Paso {i}] Palabra: '{palabra:<7}' -> Conteo actual: {frecuencias[palabra]}")

    return frecuencias


# Ejecución de casos de prueba
if __name__ == "__main__":
    print("=== CASO 1: Texto de la guía (con depuración) ===")
    texto = "Python es genial. Python es potente. Python es simple."
    resultado = contar_unicas(texto, debug=True)
    print("\nDiccionario final:")
    for palabra, cant in resultado.items():
        print(f"  {palabra}: {cant}")

    print("\n=== CASO 2: Texto con signos mixtos y mayúsculas ===")
    texto_variado = "¡Hola, mundo! Hola a todos... ¿Mundo?"
    resultado_variado = contar_unicas(texto_variado, debug=False)
    print("Entrada:", texto_variado)
    print("Resultado:", resultado_variado)
    
    
    
    
    
    
#-----------------3-------------------.





import json

# ESCRIBIR EL CÓDIGO
def guardar_config(datos, archivo, debug=False):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=2)
    if debug:
        print(f"[DEBUG] Datos guardados exitosamente en '{archivo}'.")


def cargar_config(archivo, debug=False):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
            if debug:
                print(f"[DEBUG] Archivo '{archivo}' leído con éxito: {datos}")
            return datos
    except FileNotFoundError:
        if debug:
            print(f"[DEBUG] El archivo '{archivo}' no existe. Retornando dict vacío.")
        return {}


# Ejecución de casos de prueba
if __name__ == "__main__":
    nombre_archivo = "config.json"
    config_prueba = {"tema": "oscuro", "idioma": "es"}

    print("=== CASO 1: Guardar configuración ===")
    guardar_config(config_prueba, nombre_archivo, debug=True)

    print("\n=== CASO 2: Cargar configuración existente ===")
    resultado = cargar_config(nombre_archivo, debug=True)
    print("Salida obtenida:", resultado)

    print("\n=== CASO 3: Cargar archivo inexistente (retorno seguro) ===")
    resultado_inexistente = cargar_config("no_existe.json", debug=True)
    print("Salida obtenida:", resultado_inexistente)
    
    
    
    
    
    
#-----------------4-------------------.





# ESCRIBIR EL CÓDIGO
def sin_duplicados(lista, debug=False):
    visto = set()
    resultado = []

    for i, x in enumerate(lista, start=1):
        if x not in visto:
            visto.add(x)
            resultado.append(x)
            if debug:
                print(f"  [Paso {i:2d}] Elemento {x} agregado -> Resultado actual: {resultado}")
        else:
            if debug:
                print(f"  [Paso {i:2d}] Elemento {x} ya existe (duplicado) -> Omitido")

    return resultado


# Alternativa idiomática en Python 3.7+
def sin_duplicados_v2(lista):
    return list(dict.fromkeys(lista))

# Ejecución de casos de prueba
if __name__ == "__main__":
    datos = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

    print("=== CASO 1: Lista con duplicados (Con depuración) ===")
    r = sin_duplicados(datos, debug=True)
    print("\nResultado final obtenido:", r)

    print("\n=== CASO 2: Prueba con función alternativa v2 ===")
    r2 = sin_duplicados_v2(datos)
    print("Resultado con dict.fromkeys:", r2)

    print("\n=== CASO 3: Lista con cadenas de texto ===")
    palabras = ["python", "django", "python", "flask", "django"]
    r_palabras = sin_duplicados(palabras, debug=False)
    print("Entrada:", palabras)
    print("Resultado:", r_palabras)
    
    
    
    
    
#-----------------5-------------------.
    
    
    
    

#  ESCRIBIR EL CÓDIGO
def ejecutar_calculadora():
    operaciones = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b if b != 0 else None,
    }

    while True:
        op = input("Operador (+ - * / o q para salir): ").strip()
        if op == "q":
            print("Calculadora finalizada.")
            break

        if op not in operaciones:
            print("Operador inválido")
            continue

        try:
            a = float(input("a: "))
            b = float(input("b: "))
        except ValueError:
            print("Error: Entrada numérica no válida.")
            continue

        r = operaciones[op](a, b)
        if r is None:
            print("Error: División para cero no definida.")
        else:
            print(f"Resultado: {r}")


# Ejecución
if __name__ == "__main__":
    ejecutar_calculadora()