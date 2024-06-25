import operator
from typing import Callable, Any

# Definición del tipado para operadores
Operador = Callable[[Any, Any], bool]

class OrdenamientoArray:
    """Ordenar array de diccionarios según criterios dados:
    - Elementos que cumplen criterios.
    - Orden descendente según key objetivo de elementos que cumplen criterios.

    Atributos:
    __quicksort_key: str
        Key objetivo para ordenar array de diccionarios en quicksort
    __operadores: dict[str, Operador]
        Mapeo de operadores para validación de criterios en elementos.

    Métodos:
    __init__(self: object, quicksort_key: str) -> None
        Constructor de clase. Establece key objetivo para quicksort
        y mapeo de operadores.

    __validacion_parametros(self, elemento: list[str, int],
                            parametros: list[tuple]) -> bool
        Valida si un elemento del array de entrada cumple con los criterios

    __quicksort_descendente(self, data: list[dict],
                            sort_key: str) -> list[dict]
        Ordena array de diccionarios en quicksort descendente según key objetivo

    ordenamiento_array(self, data: list[dict],
                        parametros: list[tuple]) -> list[dict]
        Ordena array de diccionarios según criterios dados.
    
    """

    def __init__(self, quicksort_key: str) -> None:
        """Constructor de clase. Establece key objetivo para quicksort
        y mapeo de operadores.

        Parámetros:
        - quicksort_key: str
            Key objetivo para ordenar array de diccionarios en quicksort

        Retorna:
        - None
        """

        # Priority
        self.__quicksort_key = quicksort_key

        # Mapeo de operadores
        self.__operadores: dict[str, Operador] = {
            '=': operator.eq,
            '>': operator.gt,
            '<': operator.lt,
            '>=': operator.ge,
            '<=': operator.le,
            '!=': operator.ne
        }


    def __validacion_parametros(self,
                            elemento: list[str, int],
                            parametros: list[tuple]) -> bool:
        """Valida si un elemento del array de entrada cumple con los criterios.
        
        Parámetros:
        - elemento: list[str, int]
            Elemento del array de entrada
        - parametros: list[tuple]
            Lista de criterios a cumplir

        Retorna:
        - bool: True si el elemento cumple con los criterios,
            False en caso contrario.
        """

        # Filtración de elementos según parámetros
        for key, operador, valor in parametros:
            if operador not in self.__operadores:
                raise ValueError(f"Operador no válido: {operador}")

            # Elemento no cumple con parámetros     
            if not self.__operadores[operador](elemento[key], valor):
                return False

        # Elemento cumple con parámetros
        return True
    

    def __quicksort_descendente(self,
                                data: list[dict],
                                sort_key: str) -> list[dict]:
        """Ordena array de dict. en quicksort descendente según key objetivo.
        
        Parámetros:
        - data: list[dict]
            Array de diccionarios a ordenar
        
        - sort_key: str
            Key objetivo para ordenar array de diccionarios

        Retorna:
        - list[dict]: Array de diccionarios ordenado en quicksort descendente
        """
        
        if len(data) <= 1:
            return data
        
        # Elemento pivote
        pivote: dict = data[len(data) // 2][sort_key]
        fila_izquierda: list[dict] = [
            elemento for elemento in data if elemento[sort_key] < pivote]
        
        # Elementos iguales al pivote
        fila_central: list[dict] = [
            elemento for elemento in data if elemento[sort_key] == pivote]
        
        fila_derecha: list[dict] = [
            elemento for elemento in data if elemento[sort_key] > pivote]
        
        # Recursividad de __quicksort_descendente en fila izquierda y derecha
        return self.__quicksort_descendente(fila_derecha, sort_key) + \
            fila_central + self.__quicksort_descendente(fila_izquierda, sort_key) 

    

    def ordenamiento_array(self,
                            data: list[dict],
                            parametros: list[tuple]) -> list[dict]:
        """Ordena array de diccionarios según criterios dados.
        
        Parámetros:
        - data: list[dict]
            Array de diccionarios a ordenar
        - parametros: list[tuple]
            Lista de criterios a cumplir

        Retorna:
        - list[dict]: Array de diccionarios ordenado según criterios dados
        """
        
        # Elementos que cumplen parámetros
        elementos_encontrados: list[dict] = [
                    elemento for elemento in data
                    if self.__validacion_parametros(elemento, parametros)]
        
        # Quicksort a elementos encontrados
        elementos_ordenados: list[dict] = self.__quicksort_descendente(
                    elementos_encontrados, self.__quicksort_key)
        
        # Elementos que no cumplen parámetros
        elementos_invalidos: list[dict] = [
                    elemento for elemento in data
                    if elemento not in elementos_encontrados]
        
        # Retornar array final pedido por prueba técnica
        array_final = elementos_ordenados + elementos_invalidos

        return array_final
