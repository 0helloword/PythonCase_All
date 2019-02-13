#-*-coding:utf-8-*-

import json

def update_PlanId(data,planid):
    #a=json.loads(data)
    data['body']['planId']=planid
    return data
pass
    
if __name__ == "__main__":
    pass