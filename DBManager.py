import os
import csv
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

    @property
    def version(self):
        return self.query("SELECT version FROM DBVersion ORDER BY version")[0][0]

    def query(self, query, parameters=None, pb_commit=False):
        """
        Executes query and returns cursor value
        :param query: operation to be executed
        :param parameters: parameters may be provided as sequence or mapping and will be bound to variables in the operation.
        :param pb_commit: if True, commit changes
        :return: cursor fetch
        """
        if parameters:
            self.cur.execute(query, parameters)
        else:
            self.cur.execute(query)

        if pb_commit:
            self.commit()

        return self.cur.fetchall()

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

    def get_tables(self):
        """
        Returns a list of tables name
        :return: List of table names in database
        """
        tables = []
        for data in self.query("SELECT name FROM sqlite_master WHERE type='table';"):
            tables.append(data[0])
        return tables

    def clear_table(self, table_name=None):
        """
        Clears all entries of a specific table name
        :param table_name: Name of the table to be cleared. If None, all tables will be cleared.
        :return:
        """
        if table_name is None:
            for table_name in self.get_tables():
                self.query("DELETE FROM " + table_name + ";")
                print("Table",table_name,"cleared")
        else:
            self.query("DELETE FROM "+table_name+";")
            print("Table", table_name, "cleared")

    def __del__(self):
        """
        Ensures that connection close on python object delete
        :return:
        """
        self.close()
        del self

    def close(self, pb_with_commit=False):
        """
        Close connection with database
        :return:
        """
        if self.con:
            print("Closing", self.path)
            if pb_with_commit:
                self.con.commit()

            self.con.close()
            self.con = None

    @staticmethod
    def isSQLite3(filename):
        if not os.path.isfile(filename):
            return False
        if os.path.getsize(filename) < 100: # SQLite database file header is 100 bytes
            return False

        with open(filename, 'rb') as fd:
            header = fd.read(100)

        return header[:16] == 'SQLite format 3\x00'

            
    def populate_from_csv(self, table_name, filename):
        res = self.query('PRAGMA TABLE_INFO('+table_name+')')

        column_data = {}

        for table_column in res:
            column_data[table_column[1]] = table_column[2]
        with open(filename, newline='') as csvfile:
           reader = csv.DictReader(csvfile, delimiter=";")
           for row in reader:
                columns = []
                values = []
                for k,v in row.items():
                    if v == "":
                        continue
                    columns.append(k)
                    if not k in column_data:
                        raise NotImplementedError("Column "+k+" not in table "+table_name)

                    column_type = column_data[k]
                    if column_type == 'TEXT':
                        v = "'" + v + "'"
                    else:
                        raise NotImplementedError("Unknowned column type "+column_type) 
                    values.append(v)
                self.query("INSERT INTO "+table_name+" ("+",".join(columns)+") VALUES("+",".join(values)+");")

        self.commit()