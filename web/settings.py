# -*- coding: utf-8 -*-
__author__ = 'nothi'


import os
import sys

workdir = os.path.split( os.path.realpath( sys.argv[0] ))[0]
workdir = os.path.join(workdir, "web")
template_dir = os.path.join(workdir,"template")

settings = {
    "static_path": os.path.join(workdir, "static"),
    "template_path": os.path.join(workdir, "template"),
    "listen_port":8080,
    "xsrf_cookies": False,

}

#分页
ITEM_PER_PAGE = 15
