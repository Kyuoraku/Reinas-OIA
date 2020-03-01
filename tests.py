import unittest
from files.Reinas import *

class TestStringMethods(unittest.TestCase):

    def test0(self):
        archivo = open("files/salida/test0.out")
        salida = archivo.read()
        archivo.close()



        archivo = open("files/esperado/test0.out")
        esperado = archivo.read()
        archivo.close()



        self.assertEqual(salida, esperado)

    
    def test1(self):
        archivo = open("files/salida/test1.out")
        salida = archivo.read()
        archivo.close()



        archivo = open("files/esperado/test1.out")
        esperado = archivo.read()
        archivo.close()



        self.assertEqual(salida, esperado)
        
    def test2(self):
        archivo = open("files/salida/test2.out")
        salida = archivo.read()
        archivo.close()



        archivo = open("files/esperado/test2.out")
        esperado = archivo.read()
        archivo.close()



        self.assertEqual(salida, esperado)

    def test3(self):
        archivo = open("files/salida/test3.out")
        salida = archivo.read()
        archivo.close()



        archivo = open("files/esperado/test3.out")
        esperado = archivo.read()
        archivo.close()



        self.assertEqual(salida, esperado)

    def test4(self):
        archivo = open("files/salida/test4.out")
        salida = archivo.read()
        archivo.close()



        archivo = open("files/esperado/test4.out")
        esperado = archivo.read()
        archivo.close()



        self.assertEqual(salida, esperado)

    def test5(self):
        archivo = open("files/salida/test5.out")
        salida = archivo.read()
        archivo.close()



        archivo = open("files/esperado/test5.out")
        esperado = archivo.read()
        archivo.close()



        self.assertEqual(salida, esperado)

    def test6(self):
        archivo = open("files/salida/test6.out")
        salida = archivo.read()
        archivo.close()



        archivo = open("files/esperado/test6.out")
        esperado = archivo.read()
        archivo.close()



        self.assertEqual(salida, esperado)

if __name__ == '__main__':
    unittest.main()