# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:50:32 2019

@author: TheKa
"""
import random
from tkinter import *

##################################
class quiz :
    def __init__(self,master):
        master.title("TV Show Name Quiz")
        master.minsize("300", "80")
        self.score = 0
        self.showList = ['the umbrella academy', 'the walking dead',' beverly hills, 90210','the order','riverdale','true detective','the widow','northern rescue','doom patrol','shameless','grey Anatomy','the orville',' workin moms','brooklyn nine-nine','dirty john','arrow','supernatural', 'star trek: discovery','sex education','whiskey cavalier','gotham','vikings',' the office','the big bang theory','peaky blinders','the flash','suits','the good doctor','good girls',"American Gods", "Brooklyn Nine Nine", "The Other Two", "CBS This Morning","Stranger Things","Black Mirror","The Crown","GLOW","House of Cards","Orange Is the New Black","13 Reasons Why","Jessica Jones"]
        self.question_number = 10
        self.ans = True
        self.show_name = self.selectShow()
        self.name_label = Label(master, text= self.jumble(self.show_name), bg="black", fg="white")
        self.blank_label = Label(master, text="")
        self.name_field = Entry(master)
        self.revalButton = Button(master,text = "reveal", command = lambda : self.name_label.configure(text = self.show_name))
        self.checkButton = Button(master, text="check", command=lambda: self.buttonCheck(self.blank_label, self.show_name, self.name_field.get()))
        self.set()

    def set(self):
        self.name_label.grid(row=0, column=0)
        self.blank_label.grid(row=1, column=0)
        self.name_field.grid(row=2, column=0)
        self.checkButton.grid(row=2, column=1)

    def selectShow(self):
        # select the tv show to be used
        select = random.randint(0, len(self.showList) - 1)
        show = self.showList[select]
        self.showList.remove(show)
        return show

    def jumble(self, name):
        # jumble the letters of the name of showw to be shown
        name = name.lower()
        nameList = name.split(" ")
        jumbleName = ""
        for i in nameList:
            temp = list(i)
            while (len(temp) > 0):
                select = random.randint(0, len(temp) - 1)
                jumbleName += temp[select]
                temp.pop(select)
            jumbleName += " "
        return jumbleName

    def check(self, guessName, correctName):
        # check if the guess is same
        guessName = guessName.lower()
        correctName = correctName.lower()
        if guessName == correctName:
            return True
        else:
            return False

    def buttonCheck(self, Label, guessName, correctName):
        ##calls check and ants upon the answer
        if self.ans:
            self.ans = False
            self.checkButton.configure(text = "Next")
            checkVal = self.check(guessName, correctName)
            self.question_number -= 1
            if checkVal:
                self.score += 1
                Label.configure(text="Correct Guess! ", fg="Green")
            else:
                self.revalButton.grid(padx=2, pady=1, row=2, column=2)
                Label.configure(text="Wrong!", fg="Red")
        else:
            self.blank_label.configure(text = "")
            self.name_field.delete(0,END)
            self.ans = True
            self.revalButton.grid_remove()
            self.checkButton.configure(text = "Check")
            if self.question_number == 0:
                self.destroy()
            else :
                self.next_question()

    def next_question(self):
        self.show_name = self.selectShow()
        self.name_label.configure(text = self.jumble(self.show_name))

    def destroy(self):
        self.name_label.grid_remove()
        self.name_field.grid_remove()
        self.checkButton.grid_remove()
        self.blank_label.configure(text = "Your Score is : " + str(self.score))

###################################
class intro:
    def __init__(self,master):
        master.title("Instruction")
        self.welcome = Label(master,text = " Instructions ")
        self.oneLabel = Label(master,text = "1. Name of Popular TV shows have been jumbled")
        self.twoLabel = Label(master, text = "2. You have to Guess the correct name of the show in text box")
        self.threeLabel = Label(master, text = "3. 10 questions will be asked ")
        self.fourLabel = Label(master, text = "4. 1 point for correct answer no -ve marks!")
        self.startButton = Button(master, text = "START", command = lambda : self.StartGame(master))
        self.set()

    def set(self):
        self.welcome.grid(row = 0, column = 0,)
        self.oneLabel.grid(row = 1, column = 0,sticky = 'w')
        self.twoLabel.grid(row = 2, column = 0,sticky = 'w')
        self.threeLabel.grid(row=3, column=0,sticky = 'w')
        self.fourLabel.grid(row=4, column=0,sticky = 'w')
        self.startButton.grid(row=5,column = 0)

    def StartGame(self,master):
        self.welcome.grid_remove()
        self.oneLabel.grid_remove()
        self.twoLabel.grid_remove()
        self.threeLabel.grid_remove()
        self.fourLabel.grid_remove()
        self.startButton.grid_remove()
        q = quiz(master)



###################################

root = Tk()
game = intro(root)
root.mainloop()
