import sqlite3, config

connection = sqlite3.connect(config.DB_FILE)

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS funding_rounds (
        id INTEGER PRIMARY KEY, 
        seriesName TEXT NOT NULL UNIQUE, 
        funding_amount TEXT NOT NULL,
        postVal DOUBLE NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS investors (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        firm TEXT,
        capital DOUBLE,
        seriesName TEXT,
        ownership DOUBLE NOT NULL,
        CONSTRAINT name_series UNIQUE (name, seriesName),
        FOREIGN KEY (seriesName) REFERENCES funding_rounds (id) ON DELETE CASCADE
    )
""")

connection.commit()