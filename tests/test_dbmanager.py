import unittest
import os
from utilities.DBManager import DBManager

__MODULEDIR__ = os.path.dirname(os.path.realpath(__file__))

INPUTS = os.path.join(__MODULEDIR__,"DATA","input")
OUTPUTS = os.path.join(__MODULEDIR__,"DATA","output")

class DBManagerTest(unittest.TestCase):
    def setUp(self):
        self.db_path = os.path.join(OUTPUTS,"test.db")
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_init(self):
        db = DBManager(self.db_path)

    def test_version(self):
        db = DBManager(self.db_path)
        self.assertEqual("0.0.0",db.version)

    def test_populate_from_csv(self):
        db = DBManager(self.db_path)
        db.populate_from_csv("DBVersion", os.path.join(INPUTS,"test_populate_from_csv.csv"))
        db.populate_from_csv("Vertex", os.path.join(INPUTS,"vertex.csv"))
        db.populate_from_csv("Parcel", os.path.join(INPUTS,"parcel.csv"))
        db.populate_from_csv("Parcel_vertices", os.path.join(INPUTS,"parcel_vertices.csv"))
        db.populate_from_csv("Road_segment", os.path.join(INPUTS,"road_segment.csv"))
        db.populate_from_csv("Road", os.path.join(INPUTS,"road.csv"))
        db.populate_from_csv("road_segments", os.path.join(INPUTS,"road_segments.csv"))
if __name__ == "__main__":
    unittest.main()