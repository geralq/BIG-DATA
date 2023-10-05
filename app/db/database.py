import configparser

from sqlalchemy import URL
from sqlalchemy import create_engine

config = configparser.ConfigParser()
config.read("app/db/database.ini")

url_object = URL.create(
    "postgresql",
    username=config["postgresql"]["user"],
    password=config["postgresql"]["password"],
    host=config["postgresql"]["host"],
    port=int(config["postgresql"]["port"]),
    database=config["postgresql"]["dbname"])

engine = create_engine(url_object)
