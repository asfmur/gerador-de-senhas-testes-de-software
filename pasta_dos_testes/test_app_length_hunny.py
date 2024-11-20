import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from pasta_do_app.app import gerar_senha

class TestLengthHunny(unittest.TestCase):

    def setUp(self):
        self.tamanho = 100

    def test_erro_tamanho_hunny(self):
        with self.assertRaises(ValueError):
            gerar_senha(self.tamanho)



