abc=2
q=2

f = open("settings.txt", "w")
f.close()

while abc>1:
    token = input("Enter your token \n")
    choice = input("Enter 1 if you want to continue, 2 if you want to change your token\n")
    if choice=="1":
        abc = abc-1
        f = open("settings.txt", "a")
        f.write(token + '\n')
        f.close()
        break
    if choice=="2":
        f = open("settings.txt", "w")
        f.close()
        continue

def cicle():
    msgb = input("Enter user message to bot \n")
    msgu = input("Enter bot message to user \n")
    f = open("settings.txt", "a")
    f.write(msgb + '\n')
    f.write(msgu + '\n')
    f.close()
    mchoice = input(
        "Press 1 if you want to save and exit, 2 if you want to make more messages\n")
    if mchoice == "1":
        lines = [" "]*1000
        with open("settings.txt", "a") as file:
            file.writelines("%s\n" % line for line in lines)
            global q
            q = q-1
    if choice == "2":
        cycle()

while q>1 :
    cicle()

#made by alde-the-coder
#version 1.0