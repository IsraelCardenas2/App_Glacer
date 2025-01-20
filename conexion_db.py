from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import declarative_base
import os



engine = create_engine('mysql://root:App_Glacer@34.51.27.97:3306/glacer_vias')
pool_size=50, 
max_overflow=80,
db_session = scoped_session(sessionmaker(bind=engine))

Database = declarative_base()