from codigo.data import data_contador_palabras
from codigo.contador_palabras import ContadorPalabras

def main():
    
    contador_palabras = ContadorPalabras()

    print(contador_palabras.contar_palabras(data_contador_palabras, "logística"))


if __name__ == '__main__':
    main()
