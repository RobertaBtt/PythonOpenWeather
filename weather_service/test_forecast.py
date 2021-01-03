__author__ = 'RobertaBtt'

import unittest

from . import forecast

class TestForecast(unittest.TestCase):

    def test_forecast(self):
        # Test:
        self.assertIsNotNone(forecast.Forecast.getForecastByCityAndDays( ['-n10', '-cBarcelona']))