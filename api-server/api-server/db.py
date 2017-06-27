from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

import config

Session = sessionmaker(autocommit=False,
                       autoflush=False,
                       bind=create_engine(config.DB_PATH))
session = scoped_session(Session)
