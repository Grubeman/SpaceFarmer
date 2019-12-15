CREATE TABLE point (
    id TEXT PRIMARY KEY,
    x REAL NOT NULL,
    y REAL NOT NULL,
    z REAL NOT NULL
);

CREATE TABLE DBVersion (
    version TEXT PRIMARY KEY,
    comments TEXT NOT NULL
);

INSERT INTO DBVersion (version,comments) VALUES( "0.0.0","First version");