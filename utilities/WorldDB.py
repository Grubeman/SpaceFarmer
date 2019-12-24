import os
import csv
import sqlite3 as lite
from utilities.DBManager import DBManager


__MODULEDIR__ = os.path.dirname(os.path.realpath(__file__))

class WorldDB(DBManager):
    def __init__(self, db_path):
        DBManager.__init__(self, db_path)

    def populate_world_from_csv(self, inputs_folder):
        self.populate_from_csv("DBVersion", os.path.join(inputs_folder,"test_populate_from_csv.csv"))
        self.populate_from_csv("Vertex", os.path.join(inputs_folder,"vertex.csv"))
        self.populate_from_csv("Parcel", os.path.join(inputs_folder,"parcel.csv"))
        self.populate_from_csv("Parcel_vertices", os.path.join(inputs_folder,"parcel_vertices.csv"))
        self.populate_from_csv("Road_segment", os.path.join(inputs_folder,"road_segment.csv"))
        self.populate_from_csv("Road", os.path.join(inputs_folder,"road.csv"))
        self.populate_from_csv("road_segments", os.path.join(inputs_folder,"road_segments.csv"))