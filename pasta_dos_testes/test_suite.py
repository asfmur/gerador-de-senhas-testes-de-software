import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pasta_dos_testes.test_app_tamanho import TestTamanho
from pasta_dos_testes.test_app_combinacao import TestCombinacao
from pasta_dos_testes.test_app_especiais import TestEspeciais 
from pasta_dos_testes.test_app_numeros import TestNumeros
from pasta_dos_testes.test_app_unica import TestSenhaUnica 
from pasta_dos_testes.test_app_maiusculas import TestMaiusculas

def suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    
    suite.addTests(loader.loadTestsFromTestCase(TestMaiusculas))
    suite.addTests(loader.loadTestsFromTestCase(TestEspeciais))
    suite.addTests(loader.loadTestsFromTestCase(TestNumeros))
    suite.addTests(loader.loadTestsFromTestCase(TestCombinacao))
    suite.addTests(loader.loadTestsFromTestCase(TestTamanho))
    suite.addTests(loader.loadTestsFromTestCase(TestSenhaUnica))
    
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
