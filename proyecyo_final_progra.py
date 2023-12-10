# -*- coding: utf-8 -*-
"""Proyecyo_final_progra.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BbWa7BySQK4_RsiEMTUs5aotgdhgjPxA

# Proyecto final juego busca minas

## Estudiantes:  Cristian Vega / Gabriel Corrales

# Diseño del Tablero

En el siguiente bloque de codigo podemos observar que se crea la tupla "tablero" en la cual le asignamos la informacipon del tablero, por ejemplo cantidad de filas, columnas y seguidamente todo el resto de la info (minas y numeros).
"""

# Tupla con la información del tablero
tablero = (
    (9, 9),
    ('*', 1, 0, 0, 1, 2, 2, 1, 0),
    (2, 2, 1, 0, 1, '*', '*', 2, 0),
    (1, '*', 1, 0, 1, 3, '*', 2, 0),
    (1, 1, 1, 1, 1, 2, 1, 1, 0),
    (0, 0, 1, 2, '*', 1, 0, 0, 0),
    (0, 0, 1, '*', 2, 1, 0, 0, 0),
    (0, 0, 1, 1, 1, 1, 1, 2, 1),
    (0, 0, 0, 0, 0, 1, '*', 3, '*'),
    (0, 0, 0, 0, 0, 1, 1, 3, '*')
)

# Creamos el archivo "tablreo.txt" y le cargamos la información anterior
with open("tablero.txt", "w") as archivo:
#Por medio de este "for" lo iteramos para ver el table en el formato deseado cuando se imprime
    for fila in tablero:
        fila_str = ",".join(map(str, fila))
        archivo.write(f"{fila_str}\n")

# Notificación de la cración del tablero
print("Archivo 'tablero.txt' creado exitosamente.\n")
print("^----------------------------------------------------^")

#Lectura previa del tablero
archivo = open("tablero.txt", "r")
filas_columnas = int(archivo.readline().strip().split(',')[0])
print(f"Tablero de {filas_columnas} columnas y {filas_columnas} filas: ")
print("\n")
print(archivo.read())
archivo.close()
print("^----------------------------------------------------^")

"""# Carga de datos al tablero

En el siguiente bloque de codigo podemos observar que se define una función llamada **"cargar_tablero()"** que se encarga de cargar un tablero desde un archivo llamado "tablero.txt" por lo que lee el archivo una unica vez.
"""

def cargar_tablero():
    tablero = []  # Tablero inicia en blanco
    filas = columnas = 0  # Filas y columnas inician en 0
    # Lectura del archivo
    try:
        with open("tablero.txt", "r") as archivo:
            filas, columnas = map(int, archivo.readline().strip().split(","))
            for _ in range(filas):
                fila = archivo.readline().strip().split(",")
                tablero.append(fila)
    # Validación de errores de carga de los datos
    except FileNotFoundError:
        print("Error: No se encontró el archivo tablero.txt.")
        print("^----------------------------------------------------^")
    if filas > 0 and columnas > 0:
        print(f"¡Excelente {usuario} , tablero cargado exitosamente!")
        print("^----------------------------------------------------^")
    else:
        print("Error: No se pudieron cargar los datos del tablero.")
        print("^----------------------------------------------------^")

    return filas, columnas, tablero

# Llama a la función y se imprime mensaje para el usuario
filas, columnas, tablero = cargar_tablero()
print(f"Filas: {filas} y columnas: {columnas}")

"""# Juego:"""

print(f"Juego de busca minas \n")
print("^----------------------------------------------------^")
print("Para iniciar ingrese su nombre de usuario:")
usuario = input("")
print("^----------------------------------------------------^")

def mostrar_tablero_actualizado(tablero, destapadas, marcadas):
    for i, fila in enumerate(tablero):
        for j, valor in enumerate(fila):
            if (i, j) in destapadas:
                print(valor, end=" ")
            elif (i, j) in marcadas:
                print("?", end=" ")
            else:
                print("-", end=" ")
        print()

def destapar_casilla(tablero, destapadas, marcadas, fila, columna, simbolo=None):
    if (fila, columna) in destapadas:
        print(f"Alerta {usuario} : Esta casilla ya ha sido destapada.")
        print("^----------------------------------------------------^")
        return 'repetida'

    if simbolo == "?":
        marcadas.add((fila, columna))
        return 'marcada'

    destapadas.add((fila, columna))

    if tablero[fila][columna] == "*":
        print(f"¡BOM!{usuario} has destapado una mina, fin del juego.")
        print("^----------------------------------------------------^")
        mostrar_tablero_actualizado(tablero, destapadas, marcadas)
        return 'mina'
    else:
        print(f"Casilla destapada: {tablero[fila][columna]}")  # Muestra el número de minas adyacentes

    return 'seguro'

def validar_coordenadas(filas, columnas, fila, columna):
    return 0 <= fila < filas and 0 <= columna < columnas

def jugar():
    filas, columnas, tablero = cargar_tablero()

    if not tablero:
        return

    destapadas = set()
    marcadas = set()

    while True:
        mostrar_tablero_actualizado(tablero, destapadas, marcadas)
        print("^----------------------------------------------------^")

        coordenadas = input(f"{usuario} por favor ingrese coordenadas (fila,columna,?[En caso de mina]): ")
        partes = coordenadas.split(",")

        try:
            fila, columna = map(int, partes[:2])
            simbolo = partes[2] if len(partes) > 2 else None
        except (ValueError, IndexError):
            print(f"Alerta {usuario} : Ingresa las coordenadas en el formato correcto (x,y).")
            continue

        print("^----------------------------------------------------^")

        if validar_coordenadas(filas, columnas, fila, columna):
            resultado = destapar_casilla(tablero, destapadas, marcadas, fila, columna, simbolo)

            if resultado == 'mina':
                break
            elif resultado == 'seguro':
                minas_restantes = sum(fila.count('*') for fila in tablero) - len(destapadas)
                if minas_restantes == 0:
                    print(f"¡WOW, felicidades {usario} ganaste!")
                    print("^----------------------------------------------------^")
                    mostrar_tablero_actualizado(tablero, destapadas)
                    break
            elif resultado == 'marcada':
                continue
        else:
            print(f"Error {usuario} : Coordenadas fuera de rango, por favor ingrese las coordenadas dentro del rango ({filas} , {columnas})")
            print("^----------------------------------------------------^")

def main():
    while True:
        print("Menú: \n")
        print("a. Diseñar Tablero")
        print("b. Jugar")
        print("c. Salir \n")

        opcion = input(f"{usuario} , seleccione una opción para continuar: ")
        print("^----------------------------------------------------^")

        if opcion == "a":
            print(f"¡Excelente {usuario} , tablero creado exitosamente!")
            print(f"De {filas} filas y {columnas} Columnas")
            print("^----------------------------------------------------^")
            pass
        elif opcion == "b":
            jugar()
            print("^----------------------------------------------------^")
            # Después de jugar, preguntar al usuario si quiere jugar nuevamente
            jugar_nuevamente = input(f"{usuario} ¿desea jugar nuevamente? (s/n): ")
            if jugar_nuevamente.lower() != 's':
                print(f"¡Gracias {usuario} , fin del juego!")
                print("^----------------------------------------------------^")

        elif opcion == "c":
             print(f"¡Gracias {usuario} , fin del programa!")
             print("^----------------------------------------------------^")
             break
        else:
            print(f"Alerta {usuario} : Opción no válida. Por favor, elija una de las opciones anteriores.")
            print("^----------------------------------------------------^")

if __name__ == "__main__":
    main()

"""# Pruebas"""

