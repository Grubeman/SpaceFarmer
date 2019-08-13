import unittest
from models.crop import Crop
class CropsTest(unittest.TestCase):
    def test_growth(self):
        crop_1 = Crop("Crop1")
        self.assertEqual(crop_1._height,0.0)
        crop_1.next()
        self.assertEqual(crop_1._height,1.0)

    def test_growth_2(self):
        self.assertTrue(True)