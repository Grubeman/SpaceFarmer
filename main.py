from models.crop import Crop
from models.field import Field
from models.weather import Weather
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    field_1 = Field()
    crop_1 = Crop("Crop1", field_1)
    weather = Weather()
    data = []
    for i in range(365):
        crop_1.grow(weather)
        data.append({"y":crop_1.height})
        
    return render_template("test.html", dataset = data)

if __name__ == "__main__":
    app.run()