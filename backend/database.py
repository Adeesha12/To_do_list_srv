import time
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database

user = 'postgres'
password = 'mysecretpassword'
host = 'localhost'
port = '5432' 
db_name = 'todo_db'

DATABASE_URI = f'postgresql://{user}:{password}@{host}:{port}/{db_name}'


def is_databse_ready(database_url, max_reties=10, retry_interval=5):
    retries = 0
    while retries < max_reties:
        try:
            test_engine = create_engine(database_url)
            with test_engine.connect() as connection:
                connection.execute(text("SELECT 1"))
            return True
        except OperationalError:
            time.sleep(retry_interval)
            retries += 1
    return False
 
if is_databse_ready(DATABASE_URI):
    print('Database is ready')
else:
    print('Database is not yet ready. exiting..............1')      

engine = create_engine(DATABASE_URI)


try:
    if not database_exists(engine.url):
        create_database(engine.url)
        print(f'Database{db_name} creat successfully ')
except OperationalError as err:
    print("an error ocured", err)
    
sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db =  sessionlocal()
    try:
        yield db 
    finally:
        db.close()

