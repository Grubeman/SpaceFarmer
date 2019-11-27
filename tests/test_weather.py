import unittest

from models.weather import Weather
class WeatherTest(unittest.TestCase):
    def test_daily(self):
        wea = Weather()
        for i in range(10):
            print(wea.get_daily(i))


if __name__ == "__main__":
    unittest.main()
