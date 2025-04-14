from tkinter import *
import pyttsx3
import options
from options import *
from assetColl import *
import assetColl as asset
from writingAQuark import *
from interWin import *

en = pyttsx3.init()
en.setProperty('volume', 100)
icon = 'C:/Users/Sohamdeep/OneDrive/Desktop/Term Python Project 2022/Assets//icon.png'


class Window:
    def __init__(self):
        themes = asset.themes()
        fonts = asset.fonts()
        self.w = Tk()
        self.w.geometry("600x500+100+100")
        self.w.config(bg=themes[0][1])
        self.w.attributes('-alpha', 0.95)
        self.w.title("Neutron")
        im = PhotoImage(file=icon)
        self.w.iconphoto(False, im)
        self.w.resizable(False, False)

        self.hdng = Label(self.w, text="Neutron", bg=themes[0][1], font=(
            fonts[0], 30), fg=themes[0][0], activebackground="#33B5E5", relief=FLAT)
        self.hdng.pack()
        self.logoBtn1 = Button(self.w, width=100, height=75,
                               bg=themes[0][1], relief='flat', bd=0, command=self.spk)
        self.logoBtn1.place(x=-5, y=-5)
        self.img1 = PhotoImage(file=logo1)
        self.logoBtn1.config(image=self.img1)
        self.logoBtn2 = Button(self.w, width=100, height=75,
                               bg=themes[0][1], relief='flat', bd=0, command=self.spk)
        self.logoBtn2.place(x=500, y=-5)
        self.logoBtn2.config(image=self.img1)
        self.i1 = Label(self.w, text=">>> Welcome to Neutron!", bg=themes[0][1], font=(
            fonts[0], 11), fg=themes[0][0], anchor='center')
        self.i1.place(x=10, y=100)
        self.i2 = Label(self.w, text=">>> This is your very own personalised audio book.",
                        bg=themes[0][1], font=(fonts[0], 11), fg=themes[0][0], anchor='center')
        self.i2.place(x=10, y=130)
        self.i3 = Label(self.w, text=">>> All audiobooks here are referred to as Quarks.",
                        bg=themes[0][1], font=(fonts[0], 11), fg=themes[0][0], anchor='center')
        self.i3.place(x=10, y=160)
        self.btn1 = Button(self.w, text=">>> [Reading a Quark]", bg=themes[0][0], font=(
            fonts[0], 11), fg=themes[0][1], command=self.readQuark)
        self.btn1.place(x=10, y=190)
        self.i4 = Label(self.w, text=">>> Wanna try writing a story maybe? Next option just for you!",
                        bg=themes[0][1], font=(fonts[0], 11), fg=themes[0][0], anchor='center')
        self.i4.place(x=10, y=230)
        self.btn2 = Button(self.w, text=">>> [Writing your own Quark]", bg=themes[0][0], font=(
            fonts[0], 11), fg=themes[0][1], command=self.quarkwrite)
        self.btn2.place(x=10, y=260)
        self.optns = Button(self.w, width=105, height=128,
                            bg=themes[0][1], relief='flat', bd=0, command=self.optns)
        self.optns.place(x=250, y=320)
        self.img = PhotoImage(
            file='C:/Users/Sohamdeep/OneDrive/Desktop/Term Python Project 2022/Assets/optns.png')
        self.optns.config(image=self.img)
        self.cprt = Label(self.w, text="©2022 Neutron Inc. All rights *not* reserved.\n( YOU ACTUALLY READ THE COPYRIGHT ?! )",
                          bg=themes[0][1], font=(fonts[0], 8), fg='#525252')
        self.cprt.place(x=0, y=460)

        self.w.mainloop()

    def spk(self):
        en.say("Welcome to Neutron!")
        en.say("This is your very own personalised audio book.")
        en.say("All audiobooks here are referred to as Quarks.")
        en.say("Start reading a Quark? Or maybe, write a story yourself?")
        en.runAndWait()

    def optns(self):
        self.w.destroy()
        opt = Options()

    def quarkwrite(self):
        self.w.destroy()
        quWrite = QuarkWrite()

    def readQuark(self):
        self.w.destroy()
        quRead = InterWin()


def main():
    App = Window()


if __name__ == '__main__':
    main()
