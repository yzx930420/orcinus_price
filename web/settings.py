__author__ = 'nothi'


import os
import sys

workdir = os.path.split( os.path.realpath( sys.argv[0] ))[0]

settings = {
    "static_path": os.path.join(workdir, "static"),
    "template_path": os.path.join(workdir, "template"),
    "listen_port":8888,
    "xsrf_cookies": False,

}