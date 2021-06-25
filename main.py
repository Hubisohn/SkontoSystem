# sconto system with coupon codes

from tkinter import *
import string
import random
import os
import re

VERSION = 2.1

global count
count = 0
global path
path = r"codes"
for root, dirs, files in os.walk(path):
    print(root)
    for i in files:
        count = count + 1


#create codes Folder if not existing
os.makedirs(path, exist_ok=True)
#create codes Folder if not existing

def renamefile():
    os.chdir(path)
    count = 1
    for file in os.listdir():
        os.rename(file, "Code" + str(count))
        count = count + 1

    count = 1
    for file in os.listdir():
        os.rename(file, "Code" + str(count) + ".txt")
        count = count + 1

    os.chdir("..")

def countrefresh():
    global count
    count = 0
    for root, dirs, files in os.walk(path):
        print(root)
        for i in files:
            count = count + 1

    noc.config(text=f"{count}/10")

    if count > 7:
        noc.config(foreground="gold")
        if count == 10:
            noc.config(foreground="red")

#global varia

def einloesen():

        einlowin = Tk()
        einlowin.title("Einloesen")

        helptxt = Label(einlowin, text="Bitte geben Sie ihren Code ein:")
        helptxt2 = Label(einlowin, text="(Code wird dann gelöscht!)")
        helptxt2.config(font=("Bold", 7))

        codeenterframe = LabelFrame(einlowin, text="Eingabe")
        global codeenter
        codeenter = Entry(codeenterframe, width=20)

        submit = Button(einlowin, text="Submit", height=1, width=20, command=submited)

        global einlcode
        einlcode = Label(einlowin)
        einlcode.config(font=("Bold", 12))

        #place and mainloop
        helptxt.place(x=0, y=10)
        helptxt2.place(x=0, y=25)
        codeenterframe.place(x=37, y=100)
        codeenter.pack()
        submit.place(x=25, y=150)
        einlcode.place(x=60, y=50)
        einlowin.mainloop()

def submited():
    codeofuser = codeenter.get()

    codeofuser = codeofuser + '\n'

    for i in range(count):
        i = i + 1
        spfile = open(f"codes\\Code{i}.txt", 'r')
        codeoffile = spfile.readline()
        if codeoffile == codeofuser:
            prozent = spfile.readline()
            print(f"Dieser Code hat einen Rabbat von {prozent}%")
            einlcode.config(text=f"Rabatt: {prozent}%")
            spfile.close()
            os.remove(f"codes\\Code{i}.txt")

            renamefile()
            countrefresh()
            break
        else:
            print("Ungültiger Code")
            einlcode.config(text=f"Ungültig!")

def helpwin():
    helpwindow = Tk()
    helpwindow.title("?")

    # label

    helptxt = Label(helpwindow, text="Geben Sie zuerst den % Satz an!")
    helptxt2 = Label(helpwindow, text="Klicken Sie dann auf ""Generate""")
    helptxt3 = Label(helpwindow, text="um einen neuen Code zu generieren!")
    helptxt4 = Label(helpwindow, text="Nach einlösen des Codes ist er")
    helptxt5 = Label(helpwindow, text="nicht mehr gültig!")

    # mainloop & place

    helptxt.place(x=0, y=0)
    helptxt2.place(x=0, y=15)
    helptxt3.place(x=0, y=30)
    helptxt4.place(x=0, y=60)
    helptxt5.place(x=0, y=75)
    helpwindow.mainloop()


def gencode():
    global randlet
    randlet = ''
    global proz
    global count

    CodeLabel = Label(window, text="                                          ")
    CodeLabel.config(text="                                                   ")
    CodeLabel.place(x=150, y=150)

    copybut = Button(window, text="Copy", height=1, width=4, command=copytxt)
    copybut.place(x=700, y=225)

    proz = prozentsatz.get()

    if proz != "":
        global myerrlabel
        myerrlabel = Label(window)
        if int(proz) < 1:
            myerrlabel.config(text="Sie müssen einen gültigen Wert angeben [1 - 100]!")
            myerrlabel.config(foreground="red")
            myerrlabel.place(y=435, x=265)


        elif int(proz) > 100:
            myerrlabel.config(text="Sie müssen einen gültigen Wert angeben [1 - 100]!")
            myerrlabel.config(foreground="red")
            myerrlabel.place(y=435, x=265)

        else:
            if count < 10:

                count = count + 1
                #print(count)
                noc.config(text=f"{count}/10")

                if count > 7:
                    noc.config(foreground="gold")
                    if count == 10:
                        noc.config(foreground="red")

                #print(proz)
                prozentsatz.delete(0, END)
                myerrlabel.destroy()

                randlet = randlet + random.choice(string.ascii_letters)
                randlet = randlet + str(random.randint(0, 9))
                randlet = randlet + random.choice(string.ascii_letters)
                randlet = randlet + str(random.randint(0, 9))
                randlet = randlet + random.choice(string.ascii_letters)
                randlet = randlet + str(random.randint(0, 9))
                randlet = randlet + random.choice(string.ascii_letters)
                randlet = randlet + str(random.randint(0, 9))

                file = open(f"codes\\Code{count}.txt", 'w')
                file.write(randlet)
                file.write("\n")
                file.write(proz)

                file.close()

                CodeLabel.config(text="Code:" + " " + randlet + "                    ")
                CodeLabel.config(font=("Bold", 50))

            else:
                CodeLabel.config(text="Error! 10/10                                      ")
                CodeLabel.config(font=("Bold", 50))
                copybut.config(state='disable')
    else:
        CodeLabel.config(text="Error!                                        ")
        CodeLabel.config(font=("Bold", 50))
        copybut.config(state='disable')

def copytxt():
    copywin = Tk()
    copywin.title("Copy")

    copylab = Text(copywin, height=10, width=40)
    copylab.insert('end', randlet)

    copylab.pack()

    copywin.mainloop()


# window with geo
window = Tk()
window.title(f"Scontosystem v{VERSION}")
window.geometry("800x500")

# Button/labels/Frames
help = Button(window, text="Help", height=1, width=4, command=helpwin)

gen = Button(window, text="Generate", height=3, width=20, command=gencode)

welc = Label(window, text=f"Scontosystem v{VERSION}")
welc.config(font=("Courier", 30))

einlo = Button(window, text="Einloesen!", height=1, width=7, command=einloesen)


global noc
noc = Label(window, text=f"{count}/10")

prozentframe = LabelFrame(window, text="Prozentsatz angeben")
prozentsatz = Entry(prozentframe, width=20)


#colorise the number
countrefresh()
#colorise the number


# place and mainloop
help.place(x=757, y=5)
noc.place(x=700, y=8)
einlo.place(x=4, y=5)
welc.place(x=170, y=50)
gen.place(x=500, y=350)
prozentframe.place(x=150, y=350)
prozentsatz.pack()
window.mainloop()