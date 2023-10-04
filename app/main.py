from app.db import database
from app.db.model import Base

if __name__ == "__main__":
    Base.metadata.create_all(database.engine)