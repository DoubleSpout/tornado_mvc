# -*- coding: utf-8 -*-
import os
import logging


import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado.options import define, options
# Sqlalchemy imports

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


import config.config
import model
import route


class Application(tornado.web.Application):
    def __init__(self):
        #定义控制器
        handlers = route.routes
        #定义配置参数
        settings = dict(
            cookie_secret=options.cookie_secret,
            login_url=options.login_url,
            template_path=options.template_path,
            static_path=options.static_path,
            xsrf_cookies=options.xsrf_cookies,
            debug=options.debug,
        )
        #执行基类构造函数
        tornado.web.Application.__init__(self, handlers, **settings)
        #定义数据库引擎


if __name__ == '__main__':
    app = Application()

    consoleStr = 'server is running, listen port:{0},env:{1}'.format(options.port,options.env)
    logging.info(consoleStr)
    print consoleStr

    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
