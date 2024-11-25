import unittest
from tests_12_3 import Runnertest, TournamentTest


loader = unittest.TestLoader()
suite = unittest.TestSuite()
suite.addTests(loader.loadTestsFromTestCase(Runnertest))
suite.addTests(loader.loadTestsFromTestCase(TournamentTest))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)