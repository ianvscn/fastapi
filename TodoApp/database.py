from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://username:password@hostname:port/database_name"
# SQLALCHEMY_DATABASE_URL = "postgresql://username:password@hostname:port/database_name"

SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'

#caso altere para banco local
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
