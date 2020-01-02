import vk_api #pip3 install vk_api for python3 or pip install vk_api for python2
from vk_api.longpoll import VkLongPoll, VkEventType
from .errors import er
from sating import *

class Vk(object):
    """docstring for Vk.
        Vk bot translator(Yandex api)
        """
    def __init__(self, token_vk=vk_token,token_ya=ya_token):
        self.token_vk = token_vk
        self.token_ya = token_ya

        if self.token_vk == "": print("[INFO]  Error 1: "+er["1"])
        if self.token_ya == "": print("[INFO]  Error 2: "+er["2"])
