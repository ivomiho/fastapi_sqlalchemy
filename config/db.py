from sqlite3 import connect
from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:@localhost:3306/products")

conn = engine.connect()
meta = MetaData()



