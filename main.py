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
    return render_template("map.jinja")

if __name__ == "__main__":
    app.run()