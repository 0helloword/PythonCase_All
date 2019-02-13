#-*-coding:utf-8-*-

import json

def update_Header_notoken(data,appId,partnerId,channelCode):
    a=json.loads(data)
    a['header']['appId']=appId
    a['header']['partnerId']=partnerId
    a['header']['channelCode']=channelCode
    return a
pass
    
if __name__ == "__main__":
    pass