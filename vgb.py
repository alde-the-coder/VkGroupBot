import vk_api
import random
import time
a=3
b=3
c=3
botison=2
while c>2:
    check = input("Do you wanna to turn on the bot OR to rewrite/write the settings.txt? 1/2 \n")
    if check=="1":
        break
    if check=="2":
        f = open("settings.txt", "w")
        f.close()
        botison=botison-2
        while a>2:
            token = input("Enter your token \n")
            choice = input("Enter 1 if you want to continue, 2 if you want to change your token\n")
            if choice == "1":
                f = open("settings.txt", "a")
                f.write(token + "\n")
                f.write("\n")
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
            f.write(msgb + "\n")
            f.write(msgu + "\n")
            f.write("\n")
            f.close()
            mchoice = input("Press 1 if you want to save, 2 if you want to make more messages\n")
            if mchoice == "1":
                b=b-2
                c=c-2
            if mchoice == "2":
                continue

if botison>1:
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
