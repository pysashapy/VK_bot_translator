import requests
import vk_api #pip3 install vk_api for python3 or pip install vk_api for python2
import threading
from vk_api.longpoll import VkLongPoll, VkEventType
from sating import *
from audio.voice import Say
from .functions import *
from .errors import er



class Vk_bot(object):
    """docstring for Vk.
        Vk bot translator(Yandex api)
        """
    def __init__(self, token_vk=vk_token,token_ya=ya_token,vk=None):
        self.token_vk = token_vk
        self.token_ya = token_ya
        self.vk = vk

        if self.token_vk == "":
            print("[INFO]  Error 1: "+er["1"])
            exit()
        if self.token_ya == "":
            print("[INFO]  Error 2: "+er["2"])
            exit()
        if self.vk != None:
            self.longpoll_vk()
        else:
            self.auth_vk()
            self.longpoll_vk()

    def auth_vk(self):
        self.vk = vk_api.VkApi(token=self.token_vk)
    def longpoll_vk(self):
        longpoll = VkLongPoll(self.vk)
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    request = (event.text).split()
                    print(request[0].lower()=="audio",)
                    if request[0].lower() in lang:
                        write_msg(self.vk,event.user_id, str(self.translate(" ".join(request[1:]),request[0].lower())))
                    elif request[0].lower() == "help" and len(request) == 1:
                        write_msg(self.vk,event.user_id, lang_help)
                    elif request[0].lower() == "audio" and request[1].lower() in lang:
                        threading.Thread(target=self.logick, args=(self.vk,event, request,)).start()

                    else:
                        write_msg(self.vk,event.user_id, str(self.translate(" ".join(request[0:]),"en")))

    def logick(self,vk,event,request):
        text = self.translate(" ".join(request[2:]),request[1].lower())
        audio_dc = Say(vk,event.peer_id, text,request[1].lower())
        write_msg(vk,event.user_id, text, audio_dc.__str__())
    def translate(self, text, language="en"):

        params = {
            "key": self.token_ya,
            "text": text,
            "lang": language
                }
        response = requests.get("https://translate.yandex.net/api/v1.5/tr.json/translate" ,params=params)
        print(response.json())
        try:
            return "".join((response.json())["text"])
        except Exception as e:
            return "error %s in Yandex api" %(response.json()["code"])
