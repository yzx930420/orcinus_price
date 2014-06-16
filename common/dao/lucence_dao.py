# -*- coding: utf-8 -*-
__author__ = 'nothi'

import sys
import json
import socket
import settings
from StringIO import StringIO

class LucenceDAO:
    def send(self, data):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect( (settings.LUCENCE_URL, settings.LUCENCE_PORT) )
        sock.sendall(data + '\n' + "end\n")
        recv_data = ""
        while True:
            try:
                buf = sock.recv(2048) #接收数据
                recv_data += buf
            except socket.error, e:
                print 'Error receiving data:%s' % e
                sys.exit(1)
            if not len(buf):
                break
            print buf

        sock.close()
        return recv_data


    def query(self, action, keyword, index, size):
        data = self.send(self.__to_json(self.__to_dict(action, keyword, index, size)))
        io = StringIO(data)
        list = json.load(io)
        list.pop()
        return list

    def get_page_size(self, action, keyword):
        data = self.send(self.__to_json(self.__to_dict(action, keyword, 1, 1)))
        io = StringIO(data)
        list = json.load(io)
        return int(list.pop())

    def __to_json(self,obj):
        return json.dumps(obj,ensure_ascii=False)

    def __to_dict(self, action, keyword, index, size):
        result = {
           'action' :action,
           'keyword':keyword,
           'index':index,
           'size':size
        }
        return result

lucence_dao = LucenceDAO()
if __name__ == "__main__":
    print lucence_dao.query("title", "l", 0, 5)
    print lucence_dao.get_page_size("title", "l")
