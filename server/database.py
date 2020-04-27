
import os
from dotenv import load_dotenv
import sqlalchemy as db


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
DB_USER = os.getenv('DB_USER')
DB_PW = os.getenv('DB_PW')


class Database():
    db_string = f'postgres://{DB_USER}:{DB_PW}@localhost:5432/hhdb'
    engine = db.create_engine(db_string)

    def __init__(self):
        self.connection = self.engine.connect()
        print('DB Instance created')

