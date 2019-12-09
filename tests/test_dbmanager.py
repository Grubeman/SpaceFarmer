import unittest
import os
from DBManager import DBManager

__MODULEDIR__ = os.path.dirname(os.path.realpath(__file__))

class DBManagerTest(unittest.TestCase):
    def test_init(self):
        db = DBManager(os.path.join(__MODULEDIR__,"DATA","output","test.db"))

if __name__ == "__main__":
    unittest.main()