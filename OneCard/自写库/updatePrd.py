#-*-coding:utf-8-*-

import json

def update_Prd(data,productId):
    #a=json.loads(data)
    data['body']['productId']=productId
    return data
pass
    
if __name__ == "__main__":
    pass