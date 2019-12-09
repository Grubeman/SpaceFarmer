import os
import sqlite3 as lite

__MODULEDIR__ = os.path.dirname(os.path.realpath(__file__))

class DBManager:
    def __init__(self, db_path):
        self.con = None
        self.cur = None
        self.path = db_path
        
        if DBManager.isSQLite3(db_path):
            self.connect()
        else:
            self.create_db(os.path.join(__MODULEDIR__, "static", "schema", "v0_0_0.sql"))
        
    def create_db(self, schema_path=None):

        b_create_from_schema = not os.path.isfile(self.path) and schema_path and os.path.isfile(schema_path)

        # Create connection
        self.connect()

        # Create from schema
        if b_create_from_schema:
            # DB file does not exist and a schema is provided
            # => create a new database from the schema
            with open(schema_path) as fp:
                self.cur.executescript(fp.read())
            self.commit()

    def commit(self):
        """
        Commit changes of the database
        :return:
        """
        if self.con:
            self.con.commit()

    def connect(self):
        """
        Establishes connection with database
        :return:
        """
        self.con = lite.connect(self.path)
        self.cur = self.con.cursor()

    @staticmethod
    def isSQLite3(filename):
        if not os.path.isfile(filename):
            return False
        if os.path.getsize(filename) < 100: # SQLite database file header is 100 bytes
            return False

        with open(filename, 'rb') as fd:
            header = fd.read(100)

        return header[:16] == 'SQLite format 3\x00'