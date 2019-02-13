#-*-coding:utf-8-*-

import json

def update_Appid(data,appid):
    #a=json.loads(data)
    data['body']['appId']=appid
    return data
pass
    
if __name__ == "__main__":
    pass