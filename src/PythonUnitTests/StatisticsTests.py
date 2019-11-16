import unittest
from Python.Statistics import Statistics

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_statistics(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_PopMean(self):
        list = [5, 78, 3]
        result = 28.666666666666668
        self.assertEqual(self.statistics.pop_mean(list), result)

    def test_Median(self):
        list = [3, 5, 11, 13, 19, 21]
        result = 12
        self.assertEqual(self.statistics.median(list), result)

    def test_Mode(self):
        list = [21, 13, 19, 13,19,13]
        result = 13
        self.assertEqual(self.statistics.mode(list), result)

    def test_PopVariance(self):
        list = [21, 13, 19, 13,19,13]
        result = 11.5555555556
        self.assertEqual(self.statistics.pop_variance(list), result)

    def test_PopStandardDeviation(self):
        list = [21, 13, 19, 13,19,13]
        result = 4.8989794855664
        self.assertEqual(self.statistics.pop_standard_deviation(list), result)

    def test_Standardized_Score(self):
        list = [21, 13, 19, 13, 19, 13]
        result = 4.8989794855664
        self.assertEqual(self.statistics.standardized_score(list), result)

    def test_SampleMean(self):
        list = [21, 13, 19, 13, 19, 13]
        result = 16.3333333333
        self.assertEqual(self.statistics.sample_mean(list), result)

    def test_SampleStandardDeviation(self):
        list = [21, 13, 19, 13, 19, 13]
        result = 3.7237973450051
        self.assertEqual(self.statistics.sample_standard_deviation(list), result)

    def test_SampleVariance(self):
        list = [21, 13, 19, 13,19,13]
        result = 13.8666666667
        self.assertEqual(self.statistics.sample_variance(list), result)

    def test_ZScore(self):
        list = [21, 13, 19, 13,19,13]
        result = 13.8666666667
        self.assertEqual(self.statistics.z_score(list), result)