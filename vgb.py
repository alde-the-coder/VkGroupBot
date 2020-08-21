import vk_api, random, time # Imports vk_api, random and time libraries.
try: # Creates a Try-Except construction.
    import variables as var # Imports file with variables.
except Exception: # If variables.py not found, this code will run.
    input("Variables.py file not found please, redownload it from my github (alde-the-coder/vkgroupbot)") # Asks user to redownlaod variables.py from github
botison = 2 # Variable botison = 2 (2 means that bot can be turned on).
mainloop = 2 # Variable mainloop = 2 (2 means that main loop will work).
RU="RU" # Variable RU = string "RU".
language = 1 # Variable language = 1 (1 = english).
try: # Creates a Try-Except construction.
    open("autostartbot.txt", "r") # Checks is there autostartbot.txt.
except FileNotFoundError: # If autostartbot does not exist this code will run.
    startfile = open("autostartbot.txt", "w") # Creates autobotstart.txt.
    startfile.write("0") # Writes "0" (this means what bot will not launch automatically).
    startfile.close() # Closes the file.
    print("File autostartbot.txt not found, making a new one with stock settings...") # Prints that the autostartbot.txt was made.
try: # Creates a Try-Except construction.
    open("language.txt", "r") # Checks is there language.txt.
except FileNotFoundError: # If language.txt not found, this code will run.
    checkfile = open("language.txt", "w")  # Creates the language.txt file.
    checkfile.write("EN") # Writes "EN" in language.txt.
    checkfile.close() # Closes the file.
    print("File language.txt not found, making a new one with stock settings...") # Prints that the language.txt was made.
with open("autostartbot.txt") as autocheck: # Opens autobotstart.txt.
    if "1" in autocheck.read(): # Searches for "1" in it (1=bot will start automatically).
        mainloop=mainloop-2 # If "1" was found, mainloop will not run.
    else: # If "1" was not found, mainloop will run.
        pass # Just pass.
with open("language.txt") as file: # Opens language.txt.
    if RU in file.read(): # If in language.txt printed "RU" this code will run.
        language = language - 1 # Changes the variable to 0 (0 = russian).
    else: # If there is no "RU" in language.txt this code will run.
        var.question1ru=var.question1
        var.question2ru=var.question2
        var.question3ru=var.question3
        var.question4ru=var.question4
        var.question5ru=var.question5
        var.question6ru=var.question6 # Changing all russian variables to english ones.
while mainloop>1: # Main loop.
            check = input(var.question1ru) # Asks user to input 1 or 2.
            if check=="1": # Checking what did user input, if its 1 this code will run.
                break # Breaks the cycle.
            if check=="2": # If its 2, this code will run.
                botison=botison-2 # Makes impossible to turn un the bot.
                while True: # Cycle about token.
                    token = input(var.question2ru) # Asks user to input his token.
                    choice = input(var.question3ru) # Asks user to input 1 or 2.
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
                    msgb = input(var.question4ru) # Asks user to input users message to the bot.
                    msgu = input(var.question5ru) # Asks user to input bots answer to users message.
                    f = open("settings.txt", "a") # Opens settings.txt to add data.
                    f.write(msgb + "\n") # Writes users message in the file.
                    f.write(msgu + "\n") # Writes bots message in the file.
                    f.write("\n") # Writes a new line in the life.
                    f.close() # Closes the file.
                    mchoice = input(var.question6ru) # Asks user to input 1 or 2.
                    if mchoice == "1": # If 1 is entered this code will run.
                        mainloop=mainloop-2 # Breaks the mainloop.
                        break # Breaks this loop.
                    if mchoice == "2": # If 2, this one.
                        continue # Makes a loop.
if botison>1: # Checks the variable, if its bigger than 1, this code will run.
    try: # Makes a Try-Except construction.
        open("settings.txt", "r") # Checks is there settings.txt.
    except FileNotFoundError: # If settings.txt not found, this code will run.
    	with open("autostartbot.txt") as errorcheck: # Opens autostartbot.txt.
    		if "1" in errorcheck.read(): # If "1" is in autostartbot.txt, this code will run.
    			input("File settings.txt not found, please turn off the autostartbot feature, reopen application and select to create settings.txt.") # Prints that the settings.txt needs to be made.
    		else: # If "1" is not found, this code will run.
        		input("File settings.txt not found, please reopen the application and select to make one.") # Prints that the settings.txt needs to be made.
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
# Version 1.5b
