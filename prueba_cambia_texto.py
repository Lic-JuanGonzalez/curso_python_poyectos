import unittest
import cambia_texto

class PruebaCambiarTexto(unittest.TestCase):

    def test_mayusculas(self):
        palabra = "buen dia"
        resultado = cambia_texto.todo_mayusculas(palabra)
        self.assertEquals(resultado,"Buen Dia")

if __name__ == "__main__":
    unittest.main()
