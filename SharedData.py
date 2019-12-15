import os
from pathlib import Path
from DBManager import DBManager
home = str(Path.home())
DATA_DIR = os.path.join(home,"AppData","Local","SpaceFarmer")
if not os.path.exists(DATA_DIR):
    os.mkdir(DATA_DIR)
WORLD_DB = DBManager(os.path.join(DATA_DIR,"world.data"))