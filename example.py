from pydal import DAL

# noinspection PyUnresolvedReferences
# import is required, even though pacakge is not used, to set up limbo:// for pyDAL
import pydal_limbo

db = DAL("limbo://localhost", folder="database")

db.define_table(
    "person",
    db.Field("name", "string"),
    db.Field("age", "integer"),
    db.Field("last_name", "string"),
    # fake_migrate=True,
)

db.commit()

# db.person.truncate()

rowid = db.person.insert(name="Henk", age=33)
assert rowid == 1

print(rowid, db(db.person.name == "Henk").select().as_list())

db.commit()

input("hi")
