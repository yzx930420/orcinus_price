# -*- coding: utf-8 -*-
__author__ = 'nothi'

import json

class LucenceDAO:
    def query(self, action, keyword, index, size):
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

