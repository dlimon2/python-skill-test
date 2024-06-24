import re

class ContadorPalabras:
    """
    Clase para contar las veces que una paalbraa objetivo se
    repite en un texto.

    Atributos:
    contador: int
        Almacena el número de veces que se repite la palabra

    Métodos:
    
    __init__(self: object) -> None
        Constructor de clase. Inicializa contador en cero.

    contar_palabras(self: object,
                    texto: str,
                    palabra_objetivo: str) -> int
        Cuenta las veces que una palabra objetivo se repite en un
        texto usando expresiones regulares en la limpieza del texto.
    """

    def __init__(self: object) -> None:
        """ Inicializa contador en cero."""
        self.__contador = int()
    

    def contar_palabras(self: object,
                        texto: str,
                        palabra_objetivo: str) -> int:
        
        """
        Cuenta las ocurrencias de la palabra objetivo en el texto.

        Parámetros:
        - texto: str
        - palabra_objetivo: str

        Retorna:
        - int: Número de repeticiones de la palabra objetivo en el texto.
        """
        
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