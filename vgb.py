import vk_api # Imports Vk_api.
import random # Imports random.
import time # Imports time.
botison = 2 # Variable botison = 2 (2 means that bot can be turned on).
mainloop = 2 # Variable mainloop = 2 (2 means that main loop will work).
RU="RU" # Variable RU = string "RU".
language = 1 # Variable language = 1 (1 = english).
with open("language.txt") as file: # Opens language.txt.
    if RU in file.read(): # If in language.txt printed "RU" this code will run.
        language = language - 1 # Changes the variable to 0 (0 = russian).
        while mainloop>1: # Main loop.
            check = input("Вы хотите включить бота или переписать/написать settings.txt? 1/2 \n") # Asks user to input 1 or 2.
            if check=="1": # Checking what did user input, if its 1 this code will run.
                break # Breaks the cycle.
            if check=="2": # If its 2, this code will run.
                botison=botison-2 # Makes impossible to turn un the bot.
                while True: # Cycle about token.
                    token = input("Введите ваш токен \n") # Asks user to input his token.
                    choice = input("Введите 1 если хотите продолжить, 2 если хотите изменить токен\n") # Asks user to input 1 or 2.
                    if choice == "1": # If 1 is entered this code will run.
                        f = open("settings.txt", "w") # Opens the settings.txt and deletes all previous data.
                        f.write(token + "\n") # Writes token in the file.
                        f.write("\n") # Writes a new line in the file.
                        f.close() # Closes the file.
                        break # Breaks the cycle.
                    if choice == "2": # If 2, this one.
                        f = open("settings.txt", "w") # Deletes all from the settings.txt.
                        f.close() # Closing a file.
                        continue # Makes a loop.
                while True: # Cycle about messanges.
                    msgb = input("Введите сообщение пользователя боту \n") # Asks user to input users message to the bot.
                    msgu = input("Введите ответ бота \n") # Asks user to input bots answer to users message.
                    f = open("settings.txt", "a") # Opens settings.txt to add data.
                    f.write(msgb + "\n") # Writes users message in the file.
                    f.write(msgu + "\n") # Writes bots message in the file.
                    f.write("\n") # Writes a new line in the life.
                    f.close() # Closes the file.
                    mchoice = input("Введите 1 если хотите сохранить, 2 если хотите добавить больше сообщений\n") # Asks user to input 1 or 2.
                    if mchoice == "1": # If 1 is entered this code will run.
                        mainloop=mainloop-2 # Breaks the mainloop.
                        break # Breaks this loop.
                    if mchoice == "2": # If 2, this one.
                        continue # Makes a loop.
    else: # If there is no "RU" in language.txt this code will run. All other comments are the same like in the RU version.
        while mainloop>1: 
            check = input("Do you wanna to turn on the bot OR to rewrite/write the settings.txt? 1/2 \n")
            if check=="1":
                break
            if check=="2":
                f = open("settings.txt", "w")
                f.close()
                botison=botison-2
                while True:
                    token = input("Enter your token \n")
                    choice = input("Enter 1 if you want to continue, 2 if you want to change your token\n")
                    if choice == "1":
                        f = open("settings.txt", "a")
                        f.write(token + "\n")
                        f.write("\n")
                        f.close()
                        break
                    if choice == "2":
                        f = open("settings.txt", "w")
                        f.close()
                        continue
                while True:
                    msgb = input("Enter user message to bot \n")
                    msgu = input("Enter bot message to user \n")
                    f = open("settings.txt", "a")
                    f.write(msgb + "\n")
                    f.write(msgu + "\n")
                    f.write("\n")
                    f.close()
                    mchoice = input("Press 1 if you want to save, 2 if you want to make more messages\n")
                    if mchoice == "1":
                        mainloop=mainloop-2
                        break
                    if mchoice == "2":
                        continue

if botison>1: # Checks the variable, if its bigger than 1, this code will run.
    f = open("settings.txt", "r") # Open file to read it.
    lin = f.readlines() # Reads lines and saves it as a variable.
    token = (lin[0]).rstrip("\n") # Says what token is on line with index 0 (first line in txt) and deletes new line.
    vk = vk_api.VkApi(token=token) # Connects to vk servers. 
    vk._auth_token() # Connects to vk servers.
    if language==0: # Check the language (0=russian).
        print("Бот включен!") # Print a message of success.
    else: # If language variable!=0, this will run.
        print("Bot is working!") # Print a message of success.
    while True: # Bot cycle.
        try: # Makes a try cycle.
            messages = vk.method("messages.getConversations", {"offset": 0, "count": 1, "filter": "unanswered"}) # Gets a message.
            if messages["count"] >= 1: # If amount of messages >=1, this code will run.
                id = messages["items"][0]["last_message"]["from_id"] # Saves id of message as a variable.
                word = messages["items"][0]["last_message"]["text"] # Text of a message as a variable.
                with open("settings.txt") as file: # Opens settings.txt to read.
                    if word in file.read(): # Searches for the text of the message in the file.
                        with open("settings.txt", "rt") as file: # Open file again for reading, but in binary reading mode.
                            for index, line in enumerate(file): # Searches for index of the message.
                                if word in line: # If message text is in file, this code will run.
                                        f = open("settings.txt", "r") # Opens file again to read.
                                        lin = f.readlines() # Reads lines and saves it as a variable.
                                        answer = (lin[index+1]).rstrip("\n") # Answer is index of a message+1 with deletes new line.
                                        if answer != "": # Answer is not empty, this code will run.
                                            vk.method("messages.send", {"peer_id": id, "message": answer, "random_id": random.randint(1, 2147483647)}) # Finally sends a answer to the user.
                                        else: # If answer is empty, this code will run.
                                            continue # Makes a loop
        except Exception as E: # Makes a exception.
            time.sleep(1) # How much code can sleep (seconds).
else: # If variable is lower than 1, this code will run.
    if language==0: # Check the language. (0=russian).
        input("Пожалуйста перезайдите в приложение") # Asks user to reopen the application.
    else: # If language variable is not equal to 0, this will run.
        input("Please reopen the application") # Asks user to reopen the application.

# Made by alde-the-coder
# Version 1.4a
