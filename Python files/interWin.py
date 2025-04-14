from tkinter import *
from assetColl import *
import assetColl as asset
from quarkRead import *

class InterWin:
    def __init__(self):
        self.rt = Tk()
        themes = asset.themes()
        fonts = asset.fonts()
        self.rt.geometry("600x500+200+200")
        self.rt.config(bg=themes[0][1])
        self.rt.attributes('-alpha', 0.95)
        self.rt.title("Neutron- Select A Genre")
        im = PhotoImage(file='C:/Users/Sohamdeep/OneDrive/Desktop/Term Python Project 2022/Assets/icon.png')
        self.rt.iconphoto(False, im)
        self.rt.resizable(False, False)

        self.selTxt = Label(self.rt, text="Select a Genre to read- ", font=(fonts[0], 24), bg=themes[0][1], fg=themes[0][0])
        self.selTxt.place(x=70, y=20)
        self.gnrBtn1 = Button(self.rt, text="Horror", font=(fonts[0], 30), bg=themes[0][0], fg=themes[0][1], command=self.genre1)
        self.gnrBtn1.place(x=100, y=150)
        self.gnrBtn2 = Button(self.rt, text="Comedy", font=(fonts[0], 30), bg=themes[0][0], fg=themes[0][1], command=self.genre2)
        self.gnrBtn2.place(x=320, y=150)
        self.gnrBtn3 = Button(self.rt, text="Science Fiction", font=(fonts[0], 30), bg=themes[0][0], fg=themes[0][1], command=self.genre3)
        self.gnrBtn3.place(x=100, y=300)

        self.rt.mainloop()
    def genre1(self):
        self.rt.destroy()
        NextWin = QuarkRead(1)
    def genre2(self):
        self.rt.destroy()
        NextWin = QuarkRead(2)
    def genre3(self):
        self.rt.destroy()
        NextWin = QuarkRead(3)


