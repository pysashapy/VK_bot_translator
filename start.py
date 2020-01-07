from Api_vk_lib import bot

def logo(fail):
    dir = open(fail)
    for i in dir:
        print(i,end="")

if __name__ == '__main__':
    logo("logo")
    bot.Vk_bot()
