from tkinter import *
from assetColl import *
import assetColl as asset
import pygame
import pyttsx3

pygame.mixer.init()
eng = pyttsx3.init()
class QuarkRead:
    def __init__(self, key):
        import writingAQuark as wq
        self.r = Tk()
        themes = asset.themes()
        fonts = asset.fonts()
        stories = asset.story() 
        self.r.geometry("600x500+200+200")
        self.r.config(bg=themes[0][1])
        self.r.attributes('-alpha', 0.95)
        self.r.title("Neutron- Read a Quark")
        im = PhotoImage(file='C:/Users/Sohamdeep/OneDrive/Desktop/Term Python Project 2022/Assets/icon.png')
        self.r.iconphoto(False, im)
        self.r.resizable(False, False)

        self.h = Label(self.r, text="", font=(fonts[0], 20), bg=themes[0][1], fg=themes[0][0])
        self.h.place(x=30, y=10)
        self.stry = Text(self.r, font=(fonts[0], 12), width=52, height=12, bg=themes[0][0], fg=themes[0][1], wrap=WORD)
        self.stry.place(x=35, y=70)
        self.btnrd = Button(self.r, text="Start Reading", font=(fonts[0], 18), bg=themes[0][0], fg=themes[0][1], command=self.read)
        self.btnrd.place(x=50, y=400)
        self.btnpse = Button(self.r, text="Pause", font=(fonts[0], 18), bg=themes[0][0], fg=themes[0][1], command=self.pause)
        self.btnpse.place(x=300, y=400)
        self.btnrsme = Button(self.r, text="Resume", font=(fonts[0], 18), bg=themes[0][0], fg=themes[0][1], command=self.resume)
        self.btnrsme.place(x=430, y=400)
        global hTxt, storyTxt
        if key == 0:
            hTxt = wq.headng
            storyTxt = wq.story
        elif key > 0:
            hTxt = stories[key-1][0]
            storyTxt = stories[key-1][1]
        self.h.configure(text=hTxt)
        self.stry.insert(1.0, storyTxt)
        self.stry.configure(state=DISABLED)

        self.r.mainloop()
    def read(self):
        global hTxt, storyTxt
        rdr = "temp.wav"
        txt = hTxt + " " + storyTxt
        eng.save_to_file(txt, rdr)
        eng.runAndWait()
        pygame.mixer.music.load(rdr)
        pygame.mixer.music.play()
    def pause(self):
        pygame.mixer.music.pause()
    def resume(self):
        pygame.mixer.music.unpause()

