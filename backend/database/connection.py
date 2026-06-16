from sqlalchemy import create_engine
from backend.database.config import *
from sqlalchemy.engine import URL

url = URL.create(
    drivername="mysql+pymysql",
    username=MYSQL_USER,
    password=MYSQL_PASSWORD,
    host=MYSQL_HOST,
    database=MYSQL_DATABASE
)

engine = create_engine(
    url,
    echo=True
)