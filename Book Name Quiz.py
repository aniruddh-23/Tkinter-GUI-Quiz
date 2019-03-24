import random
from tkinter import *

##################################
authorList = ["George R. R. Martin","Stephen King","Brandon Sanderson","John Green","Amish Tripathi","J.K. Rowling"]
bookDict={"J.K. Rowling" : ["the Sorcerer's Stone","the Prisoner of Azkaban","the Chamber of Secrets","the Goblet of Fire","the Order of the Phoenix","the Half-Blood Prince","The Tales of Beedle the Bard"],"George R. R. Martin":["A Game of Thrones","A Clash of Kings","A Storm of Swords","A Feast for Crows","A Dance with Dragons","Fevre Dream","The Ice Dragon"],"Stephen King":["The Shining","It","The Gunslinger","Pet Sematary","The Dark Tower","The Stand","The Outsider"],"Brandon Sanderson":["The Final Empire","The Way of Kings","The Well of Ascension","The Hero of Ages","Elantris","Words of Radiance","The Alloy of Law","Steelheart","Oathbringer","The Bands of Mourning","Shadows of Self"],"John Green" : ["The Fault in Our Stars","Looking for Alaska","Paper Towns","Turtles All the Way Down"],"Amish Tripathi":["The Immortals of Meluha","The Secret of the Nagas","The Oath of the Vayuputras","Scion of Ikshvaku","Sita: Warrior of Mithila"]}

class quiz :
    def __init__(self,master):
        master.title("Book Name Quiz")
        master.minsize("300","80")
        self.frame = Frame(master)
        self.score = 0
        self.question_number = 10
        self.ans = True
        self.author_name = " "
        self.book_name = " "
        self.hintToggle = False
        self.end_label = Label(master)
        self.selectBook()
        self.name_label = Label(master, text= self.jumble(self.book_name), bg="black", fg="white")
        self.blank_label = Label(master, text="")
        self.name_field = Entry(self.frame)
        self.revalButton = Button(self.frame,text = "Reveal", command = lambda : self.name_label.configure(text = self.book_name))
        self.checkButton = Button(self.frame, text="Check", command=lambda: self.buttonCheck(self.blank_label, self.book_name, self.name_field.get()))
        self.hintButton = Button(self.frame, text = "Hint", command = lambda : self. hintToggleFunc())
        self.set()

    def hintToggleFunc(self):
        self.blank_label.configure(text=self.author_name)
        self.hintToggle = True

    def set(self):
        self.name_label.pack(side = "top")
        self.blank_label.pack(side = "top")
        self.frame.pack(side = "top")
        self.name_field.pack(side = "left")
        self.checkButton.pack(side = "left")
        self.hintButton.pack(side = "left")


    def selectBook(self):
        # select the Book to be used
        select = random.randint(0, len(authorList) - 1)
        self.author_name = authorList[select]
        self.book_name = bookDict[self.author_name][random.randint(0,len(bookDict[self.author_name]) - 1)]
        bookDict[self.author_name].remove(self.book_name)
        if( len(bookDict[self.author_name]) == 0 ):
            authorList.remove(self.author_name)
        return self.book_name

    def jumble(self, name):
        # jumble the letters of the name of Book to be shown
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
                self.score += (1 if not self.hintToggle else 0.5)
                self.blank_label.configure(text="Correct Guess! ", fg="Green")
                self.hintToggle = False
            else:
                self.hintButton.pack_forget()
                self.revalButton.pack(side="left")
                Label.configure(text="Wrong!", fg="Red")
                self.hintToggle = False
        else:
            self.blank_label.configure(text = "")
            self.name_field.delete(0,END)
            self.ans = True
            self.revalButton.pack_forget()
            self.checkButton.configure(text = "Check")
            if self.question_number == 0:
                self.destroy()
            else :
                self.next_question()
                self.hintButton.pack(side = "left")

    def next_question(self):
        self.selectBook()
        self.name_label.configure(text = self.jumble(self.book_name))

    def destroy(self):
        self.name_label.pack_forget()
        self.name_field.pack_forget()
        self.checkButton.pack_forget()
        self.hintButton.pack_forget()
        self.frame.pack_forget()
        self.blank_label.pack_forget()

        self.end_label.pack(side = "top")
        if(self.score == 10):
            text = "Perfecto!"
            self.blank_label.configure(fg = 'green')
        elif( self.score >= 8):
            text = "Good"
            self.blank_label.configure(fg='gold')
        elif(self.score >= 5):
            text = "Decent"
            self.blank_label.configure(fg='tomato')
        else:
            text = "You Need to READ more BOOKS!!!"
            self.blank_label.configure(fg='red')

        self.end_label.configure(text = text,font=("Helvetica", 16))
        self.blank_label.pack(side = "top")
        self.blank_label.configure(text = "Your Score is : " + str(self.score) ,font=("Helvetica", 16))
###################################
#########intro#####################

class intro:
    def __init__(self,master):
        master.title("Instruction")
        self.welcome = Label(master,text = " Instructions ")
        self.oneLabel = Label(master,text = "1. Name of Popular Books have been jumbled")
        self.twoLabel = Label(master, text = "2. You have to Guess the correct name of the Book in text box")
        self.threeLabel = Label(master, text = "3. 10 questions will be asked ")
        self.fourLabel = Label(master, text = "4. Hint button can be selected to see Name of author of the book")
        self.fiveLabel = Label(master, text = "5. 1 point for correct answer with no Hint 0.5 points if Hint is used and no -ve marks!")
        self.startButton = Button(master, text = "START", command = lambda : self.StartGame(master))
        self.set()

    def set(self):
        self.welcome.grid(row = 0, column = 0,)
        self.oneLabel.grid(row = 1, column = 0,sticky = 'w')
        self.twoLabel.grid(row = 2, column = 0,sticky = 'w')
        self.threeLabel.grid(row=3, column=0,sticky = 'w')
        self.fourLabel.grid(row=4, column=0,sticky = 'w')
        self.fiveLabel.grid(row = 5, column = 0,sticky = 'w')
        self.startButton.grid(row=6,column = 0)

    def StartGame(self,master):
        self.welcome.grid_remove()
        self.oneLabel.grid_remove()
        self.twoLabel.grid_remove()
        self.threeLabel.grid_remove()
        self.fourLabel.grid_remove()
        self.fiveLabel.grid_remove()
        self.startButton.grid_remove()
        q = quiz(master)


###################################

root = Tk()
start = intro(root)


root.mainloop()
