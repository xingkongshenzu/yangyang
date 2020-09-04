# !/usr/bin/env python
# -*-coding:utf8-*-
# Project_name:framework
# File_name:dingding.py
# Author: jick gao
# Time:2020年09月04日

import json
import requests

def message(link=1):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=5cdbae0a5f556109b68935e81c869da2bef810bd56295525db5ec9e916ce38a5'
    pagrem = {
        "msgtype": "text",
        "text": {
            "content": "：%s " % ('冲冲冲')
        },
        "at":{
            "atMobiles":[
                "18695970629"       #需要填写自己的手机号，钉钉通过手机号@对应人
            ],
            "isAtAll": True     #是否@所有人，默认否
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    requests.post(url, data=json.dumps(pagrem), headers=headers)

if __name__ == "__main__":
    message()