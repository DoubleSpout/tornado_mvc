#!/usr/bin/env python
#coding=utf-8
from datetime import datetime
from sqlalchemy import Table,Column,Integer,String,MetaData,ForeignKey,types
from sqlalchemy.ext.declarative import declarative_base
from abstract_base import Base


class App(Base):
    __tablename__='hello_app'   #表名

    Id=Column(Integer,primary_key=True)
    Name=Column(types.String(255))
    WriteTime = Column(types.DateTime)

    def __init__(self,Id='',Name=''):
        self.Id=Id
        self.Name=Name
        self.WriteTime=datetime.today()

    def __repr__(self):
        return "<User('%s','%s','%s')>" % (self.Id,self.Name,self.WriteTime)

    @staticmethod
    def parseToList(objary):
        objLen = len(objary)
        tempArray = []
        for i in range(0,objLen):
            if not objary[i]:
                tempArray.append({})
            else:
                tempArray.append({
                    'Id':objary[i].Id,
                    'Name':objary[i].Name,
                    'WriteTime' :objary[i].WriteTime.strftime('%Y-%m-%d %H:%M:%S'),
                })
        return tempArray

users_table=App.__table__  #用来获得Table
metadata=Base.metadata  #获得MetaDATA
