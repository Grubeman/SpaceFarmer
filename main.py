from models.BaseItems import Point
from models.crop import Crop
from models.field import Field
from models.Seed import Seed
from models.weather import Weather
from flask import Flask, render_template

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
    myField = Field()
    myField._vertices.append(point1)
    myField._vertices.append(point2)
    myField._vertices.append(point3)
    myField._vertices.append(point4)

    map_data = [myField.to_json()]



    return render_template("map.jinja", map_data = map_data)

if __name__ == "__main__":
    app.run()