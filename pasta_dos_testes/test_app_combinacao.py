import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from pasta_do_app.app import gerar_senha

class TestCombinacao(unittest.TestCase):

    def setUp(self):
        self.tamanho = 10
        self.incluir_maiusculas=True 
        self.incluir_numeros=True 
        self.incluir_especiais=True

    def test_combinacao(self):
        senha = gerar_senha(self.tamanho, self.incluir_maiusculas, self.incluir_numeros, self.incluir_especiais)
        self.assertTrue(any(char.isupper()for char in senha))
        self.assertTrue(any(char.isdigit() for char in senha))
        especiais = "!@#"
        self.assertTrue(any(char in especiais for char in senha))

