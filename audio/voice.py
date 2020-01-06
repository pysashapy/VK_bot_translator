from gtts import gTTS
import time
import requests
import os
import json



class Say(object):
    """docstring for Say."""

    def __init__(self,vk=None,id=None,text=None):
        self.text = text
        self.vk = vk
        self.id = id

    def __str__(self):
        url =self.vk.method('docs.getMessagesUploadServer', {'type': 'audio_message', "peer_id": self.id})['upload_url']  # получаем ссылку для загрузки файла
        tts = gTTS(text=self.text)
        name = str(int(time.time())) + ".mp3"
        tts.save(name)
        file = open(name, 'rb')
        files = [('file', (name, file))]
        url_2 = requests.post(url , files=files).text
        file.close()
        os.remove(name)
        RESPONSE = json.loads(url_2)['file']
        RESPONSE2 =self.vk.method('docs.save',{'file': RESPONSE })
        id = RESPONSE2["audio_message"]["id"]
        owner_id = RESPONSE2["audio_message"]["owner_id"]
        document = 'doc%s_%s' % (str(owner_id), str(id))
        print(document)
        return document

    def save(self,gs):
        gs.save('hello.mp3',)
