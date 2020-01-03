import random
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

def keybord():
    a = VkKeyboard(one_time=False)
    a.add_button('Help', color=VkKeyboardColor.DEFAULT)
    return a.get_keyboard()
def write_msg(vk,user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message,"keyboard":keybord(),"random_id":random.randrange(0,99999999)})
