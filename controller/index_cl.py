# -*- coding: utf-8 -*-
import tornado.web
import sys

from bussiness import hello_bl


class MainHandler(tornado.web.RequestHandler):
    def initialize(self):
        pass

    @hello_bl.middle_ware
    def get(self):
        hello = hello_bl.Hello('hello world')
        if not hello.get_me():
            data = 'not found hello world'
            hello.save_me()
        else:
            data = hello.get_me().Name

        count = self.count

        self.render('index.html', entity=data,count=str(count))

class SecondHandler(tornado.web.RequestHandler):
    def initialize(self):
        pass

    def get(self):

        self.write(self.reverse_url('index'))
