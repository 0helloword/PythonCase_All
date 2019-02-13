#-*-coding:utf-8-*-

import json

def update_Header(data,appId,partnerId,channelCode,token):
    a=json.loads(data)
    a['header']['appId']=appId
    a['header']['partnerId']=partnerId
    a['header']['channelCode']=channelCode
    a['header']['token']=token
    return a
pass
    
if __name__ == "__main__":
    pass