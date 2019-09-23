
import time

import itchat
from itchat.content import *
from .saver import TextSaver


class Dispatcher(object):
    def __init__(self, verbose=False):
        self._registered_handlers = dict()
        self._text_saver = TextSaver(verbose=verbose)

        # Message Type definition:
        # 1 : Plain Text
        # 3 : Picture
        #
        self._register_handler('COMMON', self.common_handler)
        self._register_handler('GROUP_TEXT', self.save_group_msg)
        self._register_handler(1, self.save_group_msg)

    def get_handler(self, type):
        try:
            return self._registered_handlers[type]
        except KeyError:
            return self._registered_handlers['COMMON']

    def _register_handler(self, type, handler):
        self._registered_handlers[type] = handler

    def save_group_msg(self, msg):
        group_name = msg.User.NickName
        sender = msg.ActualNickName
        create_time = time.gmtime(int(msg.CreateTime))
        content = msg.Text
        formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', create_time)
        self._text_saver.write(content, sender, group_name, formatted_time)

    def save_friend_msg(self, msg, handle=False):
        if not handle:
            return
        pass

    def common_handler(self):
        print('Can not get proper handler to handle this type of msg.')


