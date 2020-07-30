import vk_api
import random
import time

x = 1
y = 2

f = open("settings.txt", 'r')
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
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() != lin[x].rstrip("\n"):
                x = x + 2
                y = y + 2
                continue
            elif body.lower() == lin[x].rstrip("\n"):
                vk.method("messages.send", {"peer_id": id, "message": lin[y].rstrip("\n"), "random_id": random.randint(1, 2147483647)})
                x = 1
                y = 2
                continue
    except Exception as E:
        time.sleep(1)

#made by alde-the-coder
#version 1.1
