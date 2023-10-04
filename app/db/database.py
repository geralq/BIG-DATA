from sqlalchemy import create_engine

import config

from sqlalchemy import URL

from app.db.model import Base

config = config.Config("app/db/database.ini")

url_object = URL.create(
    "postgresql",
    username=config.get("user"),
    password=config.get("password"),
    host=config.get("host"),
    port=config.get("port"),
    database=config.get("dbname")
)

engine = create_engine(url_object)
