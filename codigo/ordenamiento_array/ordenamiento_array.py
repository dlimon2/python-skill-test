import operator
from typing import Callable, Any

# Definición del tipado para operadores
Operador = Callable[[Any, Any], bool]

class OrdenamientoArray:

    def __init__(self, quicksort_key: str) -> None:

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
