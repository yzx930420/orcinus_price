# -*- coding: utf-8 -*-
__author__ = 'nothi'

import sys
import json
import socket
import settings

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
        print "data", data
        return ['9787509611876','9780821228692','9787806886182']

    def get_page_size(self, action, keyword):
        return 100;

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
