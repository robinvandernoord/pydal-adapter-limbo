# Limbo for pyDAL

**Proof of concept** pydal driver and dbapi2 implementation.

Note that the limbo python bindings are very limited, thus also limiting the pydal features!

This project is not ready yet for any real-life usage!

---

## Example usage:

```python
from pydal import DAL

# required to register limbo://
import pydal_limbo

db = DAL("limbo://storage.sqlite", folder="database")

# table = db.define_table(...)
# table.insert(id=1, ...)
# row = table(id=1)
# db.executesql(...)
# etc.

```

`db` should in the future support the same features the `sqlite3` driver
for [pyDAL](http://www.web2py.com/books/default/chapter/29/06/the-database-abstraction-layer) does.

## Limitations

Transactions are not supported in the Python driver for limbo.  
There also seems to be a problem where changes are written to a WAL-file instead of the actual database, even if 
`PRAGMA journal_mode=OFF` is used instead of `PRAGMA journal_mode=WAL`.
