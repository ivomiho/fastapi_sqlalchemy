from sqlalchemy import Table, Column
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import Integer, String



products = Table("products", meta, Column(
    "id", Integer, primary_key=True), Column("name", String(255)), Column("quantity", Integer), Column("price", Integer))

#Nuestro esquem que va para la base de datos
meta.create_all(engine)

