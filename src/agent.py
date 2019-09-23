import itchat
from itchat.content import *

from src.dispatcher import Dispatcher


class Agent(object):
    dispatcher = Dispatcher()

    @staticmethod
    @itchat.msg_register(TEXT, isGroupChat=True)
    def group_chat(msg):
        handler = Agent.dispatcher.get_handler('GROUP_TEXT')
        handler(msg)

    @staticmethod
    @itchat.msg_register(TEXT)
    def friend_chat(msg):
        handler = Agent.dispatcher.get_handler('FRIEND_TEXT')
        handler(msg)

    @staticmethod
    def run():
        itchat.auto_login()
        itchat.run()


def run_main(args):
    Agent.dispatcher = Dispatcher(verbose=args.verbose)
    Agent.run()
