import unittest
import os
from utilities.WorldDB import WorldDB

__MODULEDIR__ = os.path.dirname(os.path.realpath(__file__))

INPUTS = os.path.join(__MODULEDIR__,"DATA","input")
OUTPUTS = os.path.join(__MODULEDIR__,"DATA","output")

class DBManagerTest(unittest.TestCase):
    def setUp(self):
        self.db_path = os.path.join(OUTPUTS,"world_test.db")
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_populate_from_csv(self):
        db = WorldDB(self.db_path)
        db.populate_world_from_csv(INPUTS)
if __name__ == "__main__":
    unittest.main()