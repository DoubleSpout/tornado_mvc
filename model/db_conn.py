# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from tornado.options import define, options
from abstract_base import Base
import app_model



def __init_db(engine):
    Base.metadata.create_all(bind=engine)

#定义数据库引擎
__engine = create_engine(options.db_path, convert_unicode=True, echo=options.debug)
__init_db(__engine)
#self.db = scoped_session(sessionmaker(bind=engine))
__Session = sessionmaker(bind=__engine)
db_session = __Session()

