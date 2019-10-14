import unittest

from models.crop import Crop
from models.field import Field
from models.weather import Weather
from models.Seed import Seed
class CropsTest(unittest.TestCase):
    def test_growth(self):
        field_1 = Field()
        crop_1 = Crop(Seed, field_1)
        self.assertEqual(crop_1.height,0.0)
        crop_1.grow(Weather())
        self.assertEqual(crop_1.height,0.002)
        self.assertNotEqual(field_1.water_density,1.0)


if __name__ == "__main__":
    unittest.main()

