# Python Skill Test
Autor: <a href="https://dlimon.net" target="_blank">Daniel Limón</a><br />
Email: dani@dlimon.net

Prueba de código en Python, compuesta por dos ejercicios, donde se evalúa:
* Nivel Técnico
* Lógica de programación
* Convenciones PEP8

## Primer ejercicio (Contador de Palabras)
Dada una palabra, contar las veces que se repite en un texto dado. No usar funciones nativas de Python, p/e: __cotains, in, find, refind, index, etc..__

## Segundo ejercicio (Ordenamiento de array)
Dada una lista de entrada, ordenar por _priority_ únicamente los elementos que cumplan los criterios establecidos por los siguientes parámetros: _width, height, lenght, weight_.

El ordenamiento debe de ser como el descrito por éstos paráemtros y además, en base a la propiedad _priority_ en modo descendente. Ordenar primero los elementos que cumplan con las condiciones y después los elementos restantes, sin alterarlos.

Restricción. No utilizar funciones nativas como __sort__ o __find__

Representación de criterio de ordenamiento que puede recibir el algoritmo:

```
criteria1 = [
    ('weight', '=', 3) ]

criteria2 = [
    ('width', '>=', 2),
    ('lenght', '<=', 20) ]

```

Muestra de entrada:
```
data_ordenamiento_array = [
  {"id": 12340, "weight": 1, "width": 1, "height": 1, "length": 1, "cost": 125, "priority": 2},
  {"id": 12341, "weight": 1, "width": 1, "height": 1, "length": 1, "cost": 127, "priority": 4},
  ...
```

## Ejecución
Para ejecutar las soluciones de esta prueba, usar los siguientes comandos:
```
$ git clone https://github.com/dlimon2/python-skill-test
$ cd python-skill-test
$ python3 main.py
```
Para salir del programa, presionar Ctrl+C

![Image](https://dlimon.net/wp-content/uploads/2024/06/Screenshot-from-2024-06-24-09-47-04.png)
