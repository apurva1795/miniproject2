import unittest
from Statistics import Statistics

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()

    def tearDown(self):
        if self.statistics is not None:
            self.statistics = None

    def test_instantiate_statistics(self):
        self.assertIsInstance(self.statistics, Statistics)
