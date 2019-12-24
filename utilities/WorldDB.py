import os
import csv
import sqlite3 as lite
from utilities.DBManager import DBManager
from models.BaseItems import Point
from models.field import Field

__MODULEDIR__ = os.path.dirname(os.path.realpath(__file__))

class WorldDB(DBManager):
    def __init__(self, db_path):
        DBManager.__init__(self, db_path)

    def populate_world_from_csv(self, inputs_folder):
        self.populate_from_csv("Vertex", os.path.join(inputs_folder,"vertex.csv"))
        self.populate_from_csv("Parcel", os.path.join(inputs_folder,"parcel.csv"))
        self.populate_from_csv("Parcel_vertices", os.path.join(inputs_folder,"parcel_vertices.csv"))
        self.populate_from_csv("Road_segment", os.path.join(inputs_folder,"road_segment.csv"))
        self.populate_from_csv("Road", os.path.join(inputs_folder,"road.csv"))
        self.populate_from_csv("road_segments", os.path.join(inputs_folder,"road_segments.csv"))

    def get_vertex(self, id):
        res = self.query("Select x, y, z from vertex where id='"+id+"';")
        if len(res) > 1:
            raise NotImplementedError
        if len(res) == 0:
            raise NotImplementedError
        
        data = dict(zip(["x_coord", "y_coord", "z_coord"],res[0]))
        return Point(**data)

    def get_parcel(self, world, id):
        current = Field()
        res = self.query("Select vertex from parcel_vertices where parcel='"+id+"' ORDER BY idx;")
        if len(res) == 0:
            raise NotImplementedError("Parcel not found in db")
        for v in res:
            current._vertices.append(world.vertices[v[0]])
        return current