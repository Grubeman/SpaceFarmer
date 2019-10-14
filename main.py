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
    for i in range(365):
        crop_1.grow(weather)
        crop_data.append({"height":crop_1.height, "diameter":crop_1.diameter})
    data["crop"] = crop_data    
    return render_template("test.jinja", dataset = data)

if __name__ == "__main__":
    app.run()