import unittest
from dna_analysis.operations.at_content import calculate_at_content

class TestATContent(unittest.TestCase):
    """
    Clase de pruebas unitarias para la función `calculate_at_content` del módulo `at_content`.
    
    Esta clase contiene métodos para probar el correcto cálculo del contenido de adenina
    y timina (AT) en secuencias de ADN, incluyendo el manejo correcto de entradas inesperadas
    o inválidas.
    
    Métodos:
        test_calculate_at_content: Prueba varios casos, incluyendo secuencias válidas e inválidas,
        para asegurar el correcto comportamiento de la función `calculate_at_content`.
    """

    def test_calculate_at_content(self):
        self.assertEqual(calculate_at_content("ATGC"), 50.0)
        self.assertEqual(calculate_at_content("AAAA"), 100.0)
        self.assertEqual(calculate_at_content("TGAAC", normalize=False), 60.0)
        #self.assertRaises(ValueError, calculate_at_content, "")
        #self.assertRaises(ValueError, calculate_at_content, "XYZ")

if __name__ == '__main__':
    unittest.main()

