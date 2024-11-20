import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from pasta_do_app.app import gerar_senha

class TestNumeros(unittest.TestCase):

    def setUp(self):
        self.tamanho = 10
        self.incluir_maiusculas=0
        self.incluir_numeros=True 
        self.incluir_especiais=0

    def test_senha_com_numeros(self):
        senha = gerar_senha(self.tamanho, self.incluir_maiusculas, self.incluir_numeros, self.incluir_especiais)
        self.assertTrue(any(char.isdigit() for char in senha))