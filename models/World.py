class World:
    def __init__(self):
        self.vertices = {}
        self.parcels = {}

    def build_from_db(self, world_db):
        res = world_db.query("select id from vertex")
        for v in res:
            self.vertices[v[0]] = v[0]

        res = world_db.query("select id from parcel")
        for p in res:
            self.parcels[p[0]] = p[0]        

        for id, vertex in self.vertices.items():
            if isinstance(vertex, str):
                self.vertices[id] = world_db.get_vertex(id)

        for id, parcel in self.parcels.items():
            if isinstance(parcel, str):
                self.parcels[id] = world_db.get_parcel(self, id)