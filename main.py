"""
<Python Skill Test>
Este repositorio implementa dos ejercicios:
- Contador de palabras
- Ordenamiento de array

Autor: Daniel Limón
Email: dani@dlimon.net

Ejercicio 1: Contador de palabras
----------------------------------
Cuenta la ocurrencia de una palabra específica para un texto dado.

Ejercicio 2: Ordenamiento de array
----------------------------------
Ordena un array de tuplas según dos criterios:
1. Criterio 1: Filtrar y ordenar elementos según criterio de búsqueda
2. Criterio 2: Ordenar elementos filtrados según key objetivo (priority)

Uso:
----
1. Ejecutar main.py
2. Seleccionar ejercicio a ejecutar
3. Seguir instrucciones en consola

Dependencias:
-------------
- Python >= 3.8
- welcome.py: Módulo con mensaje de bienvenida
- data: Módulo con datos usados en ambos ejercicios
- contador_palabras: Módulo con clase ContadorPalabras
- ordenamiento_array: Módulo con clase OrdenamientoArray
"""

from welcome import welcome

# Datos usados en ambos módulos de la prueba.
from codigo.data import data_contador_palabras as texto
from codigo.data import data_ordenamiento_array as data

# Clases de los módulos de la prueba.
from codigo.contador_palabras import ContadorPalabras
from codigo.ordenamiento_array import OrdenamientoArray


# Parámetro ejercicio 1
palabra_objetivo = "logística"

# Parámetros ejercicio 2
key_objetivo = "priority"

criterio_1 = [
    ("weight", "=", 3) ]

criterio_2 = [
    ("width", ">=", 2),
    ("length", "<=", 20) ]


def main():

    print(welcome)
    seleccion: int = int(input("Seleccione ejercicio a ejecutar: "))

    if seleccion == 0:

        print("\nEjercicio 1: Contador de palabras\n")
        print(f"\nTexto a evaluar:{texto}")
        print(f"Palabra objetivo: {palabra_objetivo}\n")

        contador_palabras: ContadorPalabras = ContadorPalabras()

        conteo = contador_palabras.contar_palabras(\
                                    texto,
                                    palabra_objetivo)
        
        print(f"{palabra_objetivo} se repite {conteo} veces en el texto.")

        input("\nPresione cualquier tecla para continuar...")
        main()

        
    elif seleccion == 1:
        
        print("\nEjercicio 2: Ordenamiento de array\n")
        print("\nDatos a evaluar:\n")
        for i in data:
            print(i)
        print(f"\nKey objetivo (sort descendente): {key_objetivo}")
        print(f"\nCriterio 1: {criterio_1}")
        print(f"Criterio 2: {criterio_2}\n")

        ordenamiento_array: OrdenamientoArray = OrdenamientoArray(key_objetivo)

        criterio: int = int(input("Seleccione criterio a evaluar[1/2]: "))

        if criterio == 1:
            print("\nSelección: Criterio 1\n")
            resultado = ordenamiento_array.ordenamiento_array(data, criterio_1)
            print("Resultado:\n")
            for i in resultado:
                print(i)

        elif criterio == 2:
            print("\nSelección: Criterio 2\n")
            resultado = ordenamiento_array.ordenamiento_array(data, criterio_2)
            print("Resultado:\n")
            for i in resultado:
                print(i)

        else:
            print("Selección no válida")

    else:
        print("Selección no válida")


if __name__ == '__main__':
    main()
