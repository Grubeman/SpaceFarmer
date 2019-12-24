CREATE TABLE vertex (
    id TEXT PRIMARY KEY,
    x REAL NOT NULL,
    y REAL NOT NULL,
    z REAL NOT NULL
);

CREATE TABLE parcel (
    id TEXT PRIMARY KEY
);

CREATE TABLE parcel_vertices (
    parcel TEXT,
    vertex TEXT,
    idx REAL NOT NULL,
    FOREIGN KEY(vertex) REFERENCES vertex(id),
    FOREIGN KEY(parcel) REFERENCES parcel(id)   
);

CREATE TABLE road_segments (
    road TEXT,
    segment TEXT,
    idx REAL NOT NULL,
    FOREIGN KEY(road) REFERENCES road(id),
    FOREIGN KEY(segment) REFERENCES road_segment(id)
);


CREATE TABLE road_segment (
    id TEXT PRIMARY KEY,
    vstart TEXT,
    vend TEXT,
    FOREIGN KEY(vstart) REFERENCES vertex(id),
    FOREIGN KEY(vend) REFERENCES vertex(id)
);

CREATE TABLE road (
    id TEXT PRIMARY KEY
);

CREATE TABLE DBVersion (
    version TEXT PRIMARY KEY,
    comments TEXT NOT NULL
);

INSERT INTO DBVersion (version,comments) VALUES( "0.0.0","First version");