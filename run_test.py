from src import app
from src.entitys import beer_entity
from src.factories import beer_factory
import unittest

tests = unittest.defaultTestLoader.discover('tests', pattern='test_*.py')
if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(tests)
