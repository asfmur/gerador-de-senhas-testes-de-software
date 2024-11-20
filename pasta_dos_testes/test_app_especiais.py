import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from pasta_do_app.app import gerar_senha

class TestEspeciais(unittest.TestCase):

    def setUp(self):
        self.tamanho = 10
        self.incluir_maiusculas=0 
        self.incluir_numeros=0
        self.incluir_especiais=True


    def test_senha_com_especiais(self):
        senha = gerar_senha(self.tamanho, self.incluir_maiusculas, self.incluir_numeros, self.incluir_especiais)
        especiais = "!@#"
        self.assertTrue(any(char in especiais for char in senha))
