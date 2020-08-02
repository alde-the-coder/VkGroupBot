import vk_api
import random
import time
a=3
b=3
while True:
    check = input("Do you wanna to turn on the bot OR to rewrite/write the settings.txt? 1/2 \n")
    if check=="1":
        break
    if check=="2":
        f = open("settings.txt", "w")
        f.close()
        while a>2:
            token = input("Enter your token \n")
            choice = input("Enter 1 if you want to continue, 2 if you want to change your token\n")
            if choice == "1":
                f = open("settings.txt", "a")
                f.write(token + '\n')
                f.close()
                a=a-2
            if choice == "2":
                f = open("settings.txt", "w")
                f.close()
                continue
        while b>2:
            msgb = input("Enter user message to bot \n")
            msgu = input("Enter bot message to user \n")
            f = open("settings.txt", "a")
            f.write(msgb + '\n')
            f.write(msgu + '\n')
            f.close()
            mchoice = input("Press 1 if you want to save and turn on the bot, 2 if you want to make more messages\n")
            if mchoice == "1":
                b=b-2
            if mchoice == "2":
                continue

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
#version 1.2
