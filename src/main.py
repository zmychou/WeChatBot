#!/usr/bin/env python

import itchat
from itchat.content import *
import urllib
from urllib import request
import time
import hashlib
import json

from src.agent import run_main

def _inflate_data(question, seeion='test'):
    param = {
        'app_id' : 2121794067,
        'time_stamp' : int(time.time()),
        'nonce_str' : str(int(time.time())),
        'question': question,
        'session': seeion
    }

    keys = param.keys()
    sorted_keys = list(keys)
    sorted_keys.sort()
    sorted_dict = dict()
    for key in sorted_keys:
        sorted_dict[key] = param[key]


    data = urllib.parse.urlencode(sorted_dict)
    data = data + '&app_key=UW9t8eqy83M5ykcH'
    md5digest = hashlib.md5(bytes(data, 'utf-8')).hexdigest().upper()
    sorted_dict['sign'] = md5digest

    return sorted_dict



def _think(hear):
    data = urllib.parse.urlencode(_inflate_data(hear))
    data = bytes(data, 'utf-8')
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    req = request.Request('https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat', headers=headers, data=data, method='POST')
    resp = request.urlopen(req)
    return resp.read()

#@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg.isAt:
        question = msg.text.replace('@周小明', '')
        rev = _think(question)
        rev_obj = json.loads(rev)
        resp = 'Robot error, try again please.'
        if rev_obj['ret'] == 0:
            data = rev_obj['data']
            resp = data['answer']
        msg.user.send(u'@%s\u2005%s' % (
            msg.actualNickName, resp))

class Dummy():
    verbose = True

if __name__ == '__main__':
    args = Dummy()
    run_main(args)
