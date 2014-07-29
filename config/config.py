# -*- coding: utf-8 -*-

# Python imports
import sys
import os
import getopt
import json


from tornado.options import define, options

#获取配置参数,确定环境
__opts, _ = getopt.getopt(sys.argv[1:], "e:") #获取命令行参数
__scritpEnv = ""
__runningEvn = "Debug"

__json_data = {}
for name, value in __opts:
    if name == '-e': #获取命令行参数e
        __scritpEnv = value

if __scritpEnv == 'Debug' :
    __json_data=open(os.path.join(os.path.dirname(__file__),'debug.json'))
else:
    __runningEvn = "Production"
    __json_data=open(os.path.join(os.path.dirname(__file__),'production.json'))

#解析json配置文件
baseDirname = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir))
configDict = json.load(__json_data)

define('port', default=configDict['port'], help="run on the given port", type=int)
define("debug", default=configDict['is_debug'], type=bool)
define("env", default=__runningEvn, type=str)
define("db_path", default=configDict['db_path'], type=str)
define("static_path", default=os.path.join(baseDirname,configDict['static_path']), type=str)
define("template_path", default=os.path.join(baseDirname,configDict['template_path']), type=str)
define("xsrf_cookies", default=configDict['xsrf_cookies'], type=bool)
define("cookie_secret", default=configDict['cookie_secret'], type=str)
define('base_dirname', default=baseDirname,  type=str)
define('login_url', default=configDict['login_url'], type=str)
define('logger_name', default=configDict['logger_name'], type=str)
define('sep_logger', default=configDict['sep_logger'], type=str)

sys.path.append(baseDirname)