import os
from pathlib import Path
from utilities.WorldDB import WorldDB

home = str(Path.home())
DATA_DIR = os.path.join(home,"AppData","Local","SpaceFarmer")
if not os.path.exists(DATA_DIR):
    os.mkdir(DATA_DIR)



def init_DB_from_csv():
    __MODULEDIR__ = os.path.dirname(os.path.realpath(__file__))
    db_path = os.path.join(os.path.join(DATA_DIR,"world.data"))
    if os.path.exists(db_path):
        os.remove(db_path)
    WORLD_DB = WorldDB(os.path.join(DATA_DIR,"world.data"))
    WORLD_DB.populate_world_from_csv(os.path.join(__MODULEDIR__,"dev_data"))
    WORLD_DB.close()

init_DB_from_csv()

WORLD_DB_PATH = os.path.join(DATA_DIR,"world.data")
