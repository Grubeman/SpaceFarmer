from models.BaseItems import Segment, Line

class RiverSegment(Segment):
    def __init__(self, start, end):
        Segment.__init__(self, start, end)

class River(Line):
    def __init__(self):
        Line.__init__(self)