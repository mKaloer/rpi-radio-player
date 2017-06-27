from sqlalchemy import Column, Integer, Unicode, Boolean, DateTime, func, create_engine
from sqlalchemy.ext.declarative import declarative_base

import config

Base = declarative_base()

class Station(Base):
    __tablename__ = 'stations'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode, unique=True, nullable=False)
    url = Column(Unicode, unique=True, nullable=False)
    is_favorite = Column(Boolean, nullable=False, default=False)


class Log(Base):
    """
    Log item for persistent logging of mayor actions.
    """

    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    action = Column(Unicode, nullable=False)
    url = Column(Unicode, nullable=True)

# Create database
engine = create_engine(config.DB_PATH)
Base.metadata.create_all(engine)
