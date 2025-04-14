from tkinter import *
import pyttsx3
from pyttsx3 import *
import time
import main
from main import Window
from assetColl import *
import assetColl as asset

v = 0
r = 0
e = pyttsx3.init()
class Options:
    def __init__(self):
        themes = asset.themes()
        fonts = asset.fonts()
        self.win = Tk()
        self.win.geometry('400x400+100+100')
        self.win.title('Options')
        self.win.config(bg=themes[0][1])
        self.win.attributes('-alpha', 0.95)
        self.win.resizable(False, False)

        self.vol = IntVar()
        self.rate = IntVar()
        def get_current_value1():
            return self.vol.get()
        def slider_changed1(event):
            global v
            v = get_current_value1() 
        def get_current_value2():
            return self.rate.get()
        def slider_changed2(e):
            global r
            r = get_current_value2()
        self.hd = Label(self.win, text='Options', font=(fonts[0], 40), fg=themes[0][0], bg=themes[0][1]) 
        self.hd.pack()
        self.logobtn = Button(self.win, width=95, height=70, relief='flat', bd=0, command=self.logoclicked)
        self.logobtn.place(x=150, y=70)
        self.ph1 = PhotoImage(file=logo1)
        self.logobtn.config(image=self.ph1)
        self.o1 = Label(self.win, text="Volume:", font=(fonts[0], 20), fg=themes[0][0], bg=themes[0][1])
        self.o1.place(x=30, y=225)
        self.volsl = Scale(self.win, variable=self.vol, sliderlength=20, length=150, width=10, from_=1, to=100, orient=HORIZONTAL, bg=themes[0][1], bd=0, relief=FLAT, fg=themes[0][0], font=(fonts[0], 0), command=slider_changed1)
        self.volsl.place(x=170, y=230)
        self.btntest1 = Button(self.win, text='Test', height=2, width=5, font=(fonts[0], 8), fg=themes[0][0], bg=themes[0][1], command=self.test1)
        self.btntest1.place(x=340, y=230)
        self.o2 = Label(self.win, text="Rate:", font=(fonts[0], 20), fg=themes[0][0], bg=themes[0][1])
        self.o2.place(x=30, y=145)
        self.ratesl = Scale(self.win, variable=self.rate, sliderlength=20, length=150, width=10, from_=1, to=100, orient=HORIZONTAL, bg=themes[0][1], bd=0, relief=FLAT, fg=themes[0][0], font=(fonts[0], 0), command=slider_changed2)
        self.ratesl.place(x=170, y=150)
        self.btntest2 = Button(self.win, text='Test', height=2, width=5, font=(fonts[0], 8), fg=themes[0][0], bg=themes[0][1], command=self.test2)
        self.btntest2.place(x=340, y=150)
        self.dnbtn = Button(self.win, text='Done!', font=(fonts[0], 20), fg=themes[0][0], bg=themes[0][1], command=self.WinGenr)
        self.dnbtn.place(x=150, y=300)
        
        self.win.mainloop()
    def logoclicked(self):

        e.say("Options")
        e.say("Rate of words")
        e.say("Volume")

        e.runAndWait()
    def test1(self):
        e.setProperty('volume', v/100)
        e.say("Volume Testing")
        e.runAndWait()
    def test2(self):
        e.setProperty('rate', r+150)
        e.say("Rate Testing")
        e.runAndWait()

    def WinGenr(self):
        self.win.destroy()
        App = Window()
