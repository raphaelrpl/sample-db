from datetime import datetime
from sqlalchemy import create_engine, Column, DateTime, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql://postgres:postgres@localhost:5432/sqlalchemy')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()#metadata=MetaData(schema="bdc"))


class DBO():
    def save(self):
        """
        Save and persists object in database
        """
        try:
            session.add(self)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e

    def delete(self):
        """
        Delete object from database.
        """
        try:
            session.delete(self)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e


class BaseModel(Base, DBO):
    """
    Abstract class for ORM model. 
    Injects both `created_at` and `updated_at` fields in table
    """
    __abstract__ = True

    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())