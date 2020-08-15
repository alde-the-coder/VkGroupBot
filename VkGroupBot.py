import vk_api
import random
import time
while True:
    x = 1
    y = 2
    f = open("settings.txt", "r")
    lin = f.readlines()
    token = (lin[0]).rstrip("\n")
    vk = vk_api.VkApi(token=token)  
    vk._auth_token()
    print("Bot is working!")
    while True:
        try:
            messages = vk.method("messages.getConversations", {"offset": 0, "count": 1, "filter": "unanswered"})
            if messages["count"] >= 1:
                id = messages["items"][0]["last_message"]["from_id"]
                word = body = messages["items"][0]["last_message"]["text"]
                filename = "settings.txt"
                with open(filename) as file:
                    if word in file.read():
                        with open("settings.txt", "rt") as file:
                            for index, line in enumerate(file):
                                if word in line:
                                        f = open("settings.txt", "r")
                                        lin = f.readlines()
                                        answer = (lin[index+1]).rstrip("\n")
                                        if answer != "":
                                            vk.method("messages.send", {"peer_id": id, "message": answer, "random_id": random.randint(1, 2147483647)})
                                        else:
                                            continue
        except Exception as E:
            time.sleep(1)
else:
    input("Please reopen the application")

#made by alde-the-coder
#version 1.3f
