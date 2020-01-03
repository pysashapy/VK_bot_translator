import random
def write_msg(vk,user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message,"random_id":random.randrange(0,99999999)})
