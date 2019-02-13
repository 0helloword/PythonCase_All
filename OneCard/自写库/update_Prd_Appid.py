#-*-coding:utf-8-*-

import json

def update_Prd_Appid(data,productId,appId):
    #a=json.loads(data)
    data['body']['productId']=productId
    data['body']['appId']=appId
    return data
pass
    
if __name__ == "__main__":
    pass