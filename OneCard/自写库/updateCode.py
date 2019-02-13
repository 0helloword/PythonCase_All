#-*-coding:utf-8-*-

import json

def update_Code(data,code):
    #a=json.loads(data)
    data['body']['code']=code
    return data
pass
    
if __name__ == "__main__":
    pass