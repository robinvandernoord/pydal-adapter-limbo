from pydal.adapters import SQLite, adapters

from .limbo_dbapi2 import dbapi2


@adapters.register_for("limbo")
class Limbo(SQLite):
    drivers = ("pylimbo",)

    # def _initialize_(self):
    #     pass

    def find_driver(self):
        self.driver_name = self.drivers[0]
        self.driver = dbapi2

    def connector(self):
        return self.driver.Connection(self.dbpath, **self.driver_args)

    def lastrowid(self, table):
        # not supported
        if row := self.execute("select last_insert_rowid();").fetchone():
            return row[0]

        return None

    def after_connection(self):
        self._register_extract()
        self._register_regexp()
        # if self.adapter_args.get("foreign_keys", True):
        #     self.execute("PRAGMA foreign_keys=ON;")
        self.execute("PRAGMA journal_mode=OFF;")
