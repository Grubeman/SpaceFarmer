import unittest
import os
from DBManager import DBManager

__MODULEDIR__ = os.path.dirname(os.path.realpath(__file__))

class DBManagerTest(unittest.TestCase):
    def test_init(self):
        db = DBManager(os.path.join(__MODULEDIR__,"DATA","output","test.db"))

    def test_version(self):
        db = DBManager(os.path.join(__MODULEDIR__,"DATA","output","test.db"))
        self.assertEqual("0.0.0",db.version)

    def test_populate_from_csv(self):
        db = DBManager(os.path.join(__MODULEDIR__,"DATA","output","test.db"))
        db.populate_from_csv("DBVersion", os.path.join(__MODULEDIR__,"DATA","input","test_populate_from_csv.csv"))

if __name__ == "__main__":
    unittest.main()