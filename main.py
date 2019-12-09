from flask import Flask,render_template
from models.BaseItems import Point
from models.crop import Crop
from models.field import Field
from models.TransportItems import Road, RoadSegment
from models.Seed import Seed
from models.weather import Weather

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
    point1 = Point(0,0,0)
    point2 = Point(50,0,0)
    point3 = Point(50,50,0)
    point4 = Point(0,50,0)
    point5 = Point(100,0,0)
    point6 = Point(100,50,0)
    myField = Field()
    myField._vertices.append(point1)
    myField._vertices.append(point2)
    myField._vertices.append(point3)
    myField._vertices.append(point4)

    myField2 = Field()
    myField2._vertices.append(point2)
    myField2._vertices.append(point5)
    myField2._vertices.append(point6)
    myField2._vertices.append(point3)

    road = Road()
    road._segments.append(RoadSegment(point2, point3))


    print(road.to_json())
    map_data = {"fields": [myField.to_json(), myField2.to_json()], "roads": [road.to_json()]}



    return render_template("map.jinja", map_data = map_data)

if __name__ == "__main__":
    app.run()