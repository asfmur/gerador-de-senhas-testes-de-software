import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from pasta_do_app.app import gerar_senha

class TestTamanho(unittest.TestCase):
    
    def setUp(self):

        self.incluir_maiusculas=0 
        self.incluir_numeros=0 
        self.incluir_especiais=0

        if self._testMethodName == "test_senha_tamanho":
            self.tamanho = 10
        elif self._testMethodName == "test_segundo_senha_tamanho":
            self.tamanho = 1
        elif self._testMethodName == "test_terceiro_senha_tamanho":
            self.tamanho = 30
        elif self._testMethodName == "test_quarto_senha_tamanho":
            self.tamanho = "gaskjyjasgjkyg==========88888888!@" 

    def tearDown(self):
        return super().tearDown()

    def test_senha_tamanho(self):
        senha = gerar_senha(self.tamanho, self.incluir_maiusculas, self.incluir_numeros, self.incluir_especiais)
        self.assertEqual(len(senha), 10)
    
    def test_segundo_senha_tamanho(self):
        senha = gerar_senha(self.tamanho, self.incluir_maiusculas, self.incluir_numeros, self.incluir_especiais)
        self.assertEqual(len(senha), 1)
    
    def test_terceiro_senha_tamanho(self):
        senha = gerar_senha(self.tamanho, self.incluir_maiusculas, self.incluir_numeros, self.incluir_especiais)
        self.assertEqual(len(senha), 30)

    def test_quarto_senha_tamanho(self):
        with self.assertRaises(ValueError):
            gerar_senha(self.tamanho)