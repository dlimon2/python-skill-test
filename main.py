from welcome import welcome

from codigo.data import data_contador_palabras as texto
from codigo.contador_palabras import ContadorPalabras

def main():

    print(welcome)
    seleccion: int = int(input("Seleccione ejercicio a ejecutar: "))

    if seleccion == 0:
        palabra_objetivo = "logística"

        print(f"\nTexto a evaluar:{texto}")
        print(f"Palabra objetivo: {palabra_objetivo}\n")

        contador_palabras: ContadorPalabras = ContadorPalabras()

        conteo = contador_palabras.contar_palabras(\
                                    texto,
                                    palabra_objetivo)
        
        print(f"{palabra_objetivo} se repite {conteo} veces en el texto.")


    elif seleccion == 1:
        pass

    else:
        print("Selección no válida")


if __name__ == '__main__':
    main()
