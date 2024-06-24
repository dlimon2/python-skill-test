import re

class ContadorPalabras:

    def __init__(self: object) -> None:
        self.__contador = int()
    

    def contar_palabras(self: object,
                        texto: str,
                        palabra_objetivo: str) -> int:
        
        # Limpiar texto con expresiones regulares
        texto = re.sub(r'[^\w\s]', '', texto)
     
        # Texto a tupla de palabras
        split_texto: tuple = tuple(texto.split())

        # Resetear contador
        self.contador = 0

        # Búsqueda de coincidencias
        for palabra in split_texto:
            if palabra.lower() == palabra_objetivo.lower():
                # Incremento de contador
                self.__contador += 1

        return self.__contador