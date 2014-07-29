from controller import index_cl
from tornado.web import RequestHandler, Application, url

routes = [
    url(r'/', index_cl.MainHandler, name='index'),
    url(r'/second', index_cl.SecondHandler, name='second'),
    ]
