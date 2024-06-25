import unittest
from codigo.ordenamiento_array import OrdenamientoArray

class TestOrdenamientoArray(unittest.TestCase):

    def test_ordenamiento_array(self):
        ordenamiento = OrdenamientoArray("priority")
        data = [
            {"weight": 3, "width": 2, "length": 3, "priority": 1},
            {"weight": 3, "width": 3, "length": 2, "priority": 3},
            {"weight": 3, "width": 1, "length": 1, "priority": 2},
            {"weight": 2, "width": 3, "length": 2, "priority": 3},
            {"weight": 1, "width": 1, "length": 1, "priority": 2}]
        
        criterio = [
            ("weight", "=", 1) ]
        
        resultado = ordenamiento.ordenamiento_array(data, criterio)

        self.assertEqual(resultado, [
            {"weight": 1, "width": 1, "length": 1, "priority": 2},
            {"weight": 3, "width": 2, "length": 3, "priority": 1},
            {"weight": 3, "width": 3, "length": 2, "priority": 3},
            {"weight": 3, "width": 1, "length": 1, "priority": 2},
            {"weight": 2, "width": 3, "length": 2, "priority": 3}])
        

    def test_ordenamiento_array_2(self):
        ordenamiento = OrdenamientoArray("priority")
        data = [
            {"weight": 3, "width": 2, "length": 3, "priority": 1},
            {"weight": 3, "width": 3, "length": 2, "priority": 3},
            {"weight": 3, "width": 1, "length": 1, "priority": 2},
            {"weight": 2, "width": 3, "length": 2, "priority": 3},
            {"weight": 1, "width": 1, "length": 1, "priority": 2}]
        
        criterio = [
            ("weight", "=", 3) ]
        
        resultado = ordenamiento.ordenamiento_array(data, criterio)

        self.assertEqual(resultado, [
            {"weight": 3, "width": 3, "length": 2, "priority": 3},
            {"weight": 3, "width": 1, "length": 1, "priority": 2},
            {"weight": 3, "width": 2, "length": 3, "priority": 1},
            {"weight": 2, "width": 3, "length": 2, "priority": 3},
            {"weight": 1, "width": 1, "length": 1, "priority": 2}])
        

    def test_multiple_criteria(self):
        ordenamiento = OrdenamientoArray("priority")
        data = [
            {"weight": 3, "width": 2, "length": 3, "priority": 1},
            {"weight": 3, "width": 3, "length": 2, "priority": 3},
            {"weight": 3, "width": 1, "length": 1, "priority": 2},
            {"weight": 2, "width": 3, "length": 2, "priority": 3},
            {"weight": 1, "width": 1, "length": 1, "priority": 2}]
        
        criterio = [
            ("weight", "=", 3),
            ("width", ">=", 2) ]
        
        resultado = ordenamiento.ordenamiento_array(data, criterio)

        self.assertEqual(resultado, [
            {"weight": 3, "width": 3, "length": 2, "priority": 3},
            {"weight": 3, "width": 2, "length": 3, "priority": 1},   
            {"weight": 3, "width": 1, "length": 1, "priority": 2},
            {"weight": 2, "width": 3, "length": 2, "priority": 3},
            {"weight": 1, "width": 1, "length": 1, "priority": 2}])

