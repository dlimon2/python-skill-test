import os, unittest
from codigo.contador_palabras import ContadorPalabras

class TestContadorPalabras(unittest.TestCase):

    def test_contar_palabras(self):
        texto = """
        El perro del vecino es un perro muy simpático. Cada vez que salgo de casa,
        el perro corre hacia mí y mueve la cola con mucha energía. Me encanta ver
        al perro jugar con otros perros en el parque. Es un perro que siempre está
        feliz y transmite su alegría a todos los que lo rodean. Sin duda, es el
        perro más amistoso que he conocido.
        """
        palabra_objetivo = "perro"
        contador_palabras = ContadorPalabras()
        conteo = contador_palabras.contar_palabras(texto, palabra_objetivo)
        self.assertEqual(conteo, 6)


    def test_texto_vacio(self):
        texto = ""
        palabra_objetivo = "perro"
        contador_palabras = ContadorPalabras()
        conteo = contador_palabras.contar_palabras(texto, palabra_objetivo)
        self.assertEqual(conteo, 0)


    def test_palabra_objetivo_vacia(self):
        texto = """
        El perro del vecino es un perro muy simpático. Cada vez que salgo de casa,
        el perro corre hacia mí y mueve la cola con mucha energía. Me encanta ver
        al perro jugar con otros perros en el parque. Es un perro que siempre está
        feliz y transmite su alegría a todos los que lo rodean. Sin duda, es el
        perro más amistoso que he conocido.
        """
        palabra_objetivo = ""
        contador_palabras = ContadorPalabras()
        conteo = contador_palabras.contar_palabras(texto, palabra_objetivo)
        self.assertEqual(conteo, 0)