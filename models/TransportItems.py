from models.BaseItems import Segment, Line

class RoadSegment(Segment):
    def __init__(self, start, end):
        Segment.__init__(self, start, end)

class Road(Line):
    def __init__(self):
        Line.__init__(self)