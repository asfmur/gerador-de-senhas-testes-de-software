import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from pasta_do_app.app import gerar_senha

class TestLengthZero(unittest.TestCase):
    
    def setUp(self):
        self.tamanho = 0

    def test_erro_tamanho_zero(self):
        with self.assertRaises(ValueError):
            gerar_senha(self.tamanho)

