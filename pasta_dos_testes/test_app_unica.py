import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from pasta_do_app.app import gerar_senha

class TestSenhaUnica(unittest.TestCase):

    def setUp(self):
        self.tamanho = 10

    def test_senha_unica(self):
        senhas = [gerar_senha(self.tamanho, ) for _ in range(100)]
    
        duplicates = [senha for senha in senhas if senhas.count(senha) > 1]
    
        self.assertEqual(len(duplicates), 0, "Existem senhas repetidas")

