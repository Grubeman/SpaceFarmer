from flask import Flask,render_template


from models.BaseItems import Point
from models.crop import Crop
from models.field import Field
from models.TransportItems import Road, RoadSegment
from models.Seed import Seed
from models.weather import Weather
from models.World import World

from utilities.WorldDB import WorldDB
from SharedData import WORLD_DB_PATH

app = Flask(__name__)

@app.route('/')
def index():
    field_1 = Field()
    crop_1 = Crop(Seed, field_1)
    weather = Weather()
    data = {}
    crop_data = []
    weather_data = []
    for i in range(365):
        weather_data.append({"temperature":weather.get_daily(i)})
        crop_1.grow(weather_data[-1])
        crop_data.append({"height":crop_1.height, "diameter":crop_1.diameter})
    data["crop"] = crop_data    
    data["weather"] = weather_data 
    return render_template("test.jinja", dataset = data)

@app.route('/map')
def draw_map():

    world = World()

    world_db = WorldDB(WORLD_DB_PATH)
    world.build_from_db(world_db)
    world_db.close()

    print(world.vertices)

    point2 = Point(50,0,0)
    point3 = Point(50,50,0)

    road = Road()
    road._segments.append(RoadSegment(point2, point3))


    print(road.to_json())
    map_data = {"fields": [parcel.to_json() for parcel in world.parcels.values()], "roads": [road.to_json()]}



    return render_template("map.jinja", map_data = map_data)

if __name__ == "__main__":
    app.run()