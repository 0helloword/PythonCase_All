# -*- coding: utf-8 -*-

import json

def update_token(data,token):
    a=json.loads(data)
    a['header']['token']=token
    return a
pass
    
if __name__ == "__main__":
    pass