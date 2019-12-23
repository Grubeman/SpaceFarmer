CREATE TABLE point (
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
    point TEXT,
    index INTEGER
);

CREATE TABLE road_segment (
    id TEXT PRIMARY KEY,
    start TEXT,
    end TEXT
);

CREATE TABLE road (
    id TEXT PRIMARY KEY
);

CREATE TABLE road_segments (
    road TEXT,
    segment TEXT,
    index INTEGER
);

CREATE TABLE DBVersion (
    version TEXT PRIMARY KEY,
    comments TEXT NOT NULL
);

INSERT INTO DBVersion (version,comments) VALUES( "0.0.0","First version");