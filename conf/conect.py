import configparser
import pathlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

file_config = pathlib.Path(__file__).parent.parent.joinpath('config.ini')
config = configparser.ConfigParser()
config.read(file_config)

user = config.get('DEV_DB', 'USER')
password = config.get('DEV_DB', 'PASSWORD')
db_name = config.get('DEV_DB', 'DB_NAME')
domain = config.get('DEV_DB', 'DOMAIN')
port = config.get('DEV_DB', 'PORT')

URI = f"postgresql://{user}:{password}@{domain}:{port}/{db_name}"

engine = create_engine(URI, echo=False, pool_size=4, max_overflow=0)
DBSession = sessionmaker(bind=engine)
session = DBSession()
