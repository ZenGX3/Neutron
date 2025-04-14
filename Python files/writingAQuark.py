from tkinter import *
import time
from assetColl import *
import assetColl as asset


headng = ""
story = ""
ls = ["\t>>> Give a good start to your story.Describe the \n\t  environment around the characters. For eg, \n  A boy lived in a castle/(any place)", "\t\t\t\t\t>>> Add a middle plot and maybe include \n\t\t\tsome twists too!", "\t\t>>> You have reached the last stretch! \n\tNow, end your story...\n\t\t\t\t[BONUS- You could end it like there is a deeper \n\t\t\t   story awaiting your debut!]"]
class QuarkWrite:
    def __init__(self):
        self.root = Tk()
        themes = asset.themes()
        fonts = asset.fonts()
        self.root.geometry("700x600+200+200")
        self.root.config(bg=themes[0][1])
        self.root.attributes('-alpha', 0.95)
        self.root.title("Neutron- Write a Quark")
        im = PhotoImage(file='C:/Users/Sohamdeep/OneDrive/Desktop/Term Python Project 2022/Assets/icon.png')
        self.root.iconphoto(False, im)
        self.root.resizable(False, False)
        
        self.head = Label(self.root, text="~ Write A Quark ~", font=(fonts[0], 25), fg=themes[0][0], bg=themes[0][1])
        self.head.place(x=190, y=10)
        self.storyspace = Text(self.root, height=15, width=60, font=(fonts[0], 12), bg=themes[0][1], fg=themes[0][0], cursor='circle')
        self.storyspace.place(x=45, y=100)
        self.txt = Label(self.root, text=">>> First, type a heading for you story.", font=(fonts[0], 18), bg=themes[0][1], fg=themes[0][0], anchor=W)
        self.txt.place(x=45, y=400)
        self.btndone = Button(self.root, text="Next...", font=(fonts[0], 18), bg=themes[0][1], fg=themes[0][0], command=self.next)
        self.btndone.place(x=45, y=500)

        self.root.mainloop()
    def next(self):
        global headng
        headng = self.storyspace.get('1.0', END)
        self.storyspace.delete(1.0, END)
        time.sleep(1)
        self.txt.configure(text=ls[0], anchor=W)
        self.txt.place(x=-40, y=400)
        self.txt.configure(font=('Space Mono', 15))
        self.btndone.configure(command=self.next2)
    def next2(self):
        time.sleep(1)
        global story
        story += self.storyspace.get(1.0, END)
        self.storyspace.delete(1.0, END)
        self.txt.configure(text=ls[1], anchor=W, font=("Space Mono", 18))
        self.txt.place(x=-550, y=400)
        self.btndone.configure(command=self.next3)
    def next3(self):
        time.sleep(1)
        self.btndone.configure(text="Done!")
        self.btndone.place(x=300)
        global story
        story += self.storyspace.get(1.0, END)
        self.storyspace.delete(1.0, END)
        self.txt.configure(text=ls[2], font=("Space Mono", 15))
        self.txt.place(x=-300, y=360)
        self.btndone.configure(command=self.donewin)
    def donewin(self):
        time.sleep(1)
        global story
        story += self.storyspace.get(1.0, END)
        self.storyspace.delete(1.0, END)
        self.root.destroy()
        import quarkRead
        App = quarkRead.QuarkRead(0)




        
    
