# -*- coding: utf-8 -*-
__author__ = 'nothi'

LOCAL_HOST = 0

if LOCAL_HOST == 1:
    MYSQL_URL = "127.0.0.1"
    MYSQL_PORT = 3306
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "12345"
    MYSQL_DATABASE = "mytest"
    LUCENCE_URL = "127.0.0.1"
    LUCENCE_PORT = 4700
else:
    MYSQL_URL = "121.199.50.11"
    MYSQL_PORT = 3306
    MYSQL_USER = "orca"
    MYSQL_PASSWORD = "orcamysql"
    MYSQL_DATABASE = "scrapy"
    LUCENCE_URL = "121.199.50.11"
    LUCENCE_PORT = 4700

