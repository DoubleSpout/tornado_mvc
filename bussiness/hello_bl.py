# -*- coding: utf-8 -*-
import tornado
import sys
from functools import wraps
from model import app_model,db_conn



class Hello(tornado.web.RequestHandler):

    def __init__(self,appname=''):
        self.appname=appname
        self.App_model = app_model.App
        self.db_session = db_conn.db_session

    def get_me(self):
       self.app_ins = self.db_session.query(self.App_model).filter_by(Name=self.appname).first()
       if hasattr(self.app_ins,'Id'):
           return self.app_ins
       else:
           return None

    def save_me(self):

        if not hasattr(self.app_ins,'Id'):
            self.app_ins = app_model.App(Name=self.appname)
            self.db_session.add(self.app_ins)
            self.db_session.commit()



class Middleware(object):
    def __init__(self):
        pass

    def __call__(self, method):
        @wraps(method)
        def wrapper(handler, *args, **kwargs):
            count = 1
            if handler.get_secure_cookie('count'):
                count = int(handler.get_secure_cookie('count'))
            count += 1
            handler.set_secure_cookie('count',str(count),expires_days=365)
            handler.count = count
            return method(handler, *args, **kwargs)
        return wrapper

middle_ware = Middleware()