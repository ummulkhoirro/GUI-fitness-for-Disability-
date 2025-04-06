from tkinter import *
from PIL import Image, ImageTk
from customtkinter import *
from gtts import gTTS
from tkinter import messagebox
import playsound
import os

from aerobics import Aerobics
from physioteraphy import Physioteraphy

class IntelectualMental():
    
    def __init__(self, mental):
        self.mental = mental
        self.mental.after(1000)
        self.mental.title("FitInclusive")
        self.mental.rowconfigure(0, weight=1)
        self.mental.columnconfigure(0, weight=1)
        height = 720
        width = 1280
        x = (self.mental.winfo_screenwidth() // 2) - (width // 2)
        y = (self.mental.winfo_screenheight() // 4) - (height // 4)
        self.mental.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.mental.resizable(0, 0)
        self.mental.config(bg="#291C4F")
        self.myfont = CTkFont(family='Poppins', size=14, weight='bold', slant='italic')

        def exit():
            sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=self.mental)
            if sure:
                self.mental.destroy()
        self.mental.protocol("WM_DELETE_WINDOW", exit)
        # IMAGE

        self.img_path = ("D:\\pythonProject1\\pict\\aerobic.png")
        self.img2_path = ("D:\\pythonProject1\\pict\\physiotherapy.png")
        self.img3_path = ("D:\\pythonProject1\\pict\\backbgremove.png")
        self.load_image()

        # LABEL
        canvas = Canvas(self.mental, width=self.img_back.width(), height=self.img_back.height(), bg="#291C4F", bd=0, highlightthickness=0)
        canvas.place(x=20, y=20)
        
        Label_atas = Label(canvas, text="INTELECTUAL MENTAL", bg="#291C4F", fg="white", font=("Italic, 35"))
        Label_atas.pack(side=RIGHT, padx=10)

        Label_text = Label(self.mental, text="RECOMMENDED FOR YOU !!", font=self.myfont, bg="#291C4F", fg="white")
        Label_text.place(x=90, y=200)

        # BUTTON

        def tts_back():
            self.mental.destroy()

        
        def open_aerobics():
            self.mental.destroy()
            new_window = Tk()
            Aerobics(new_window)
            new_window.mainloop()

        def open_physioteraphy():
            self.mental.destroy()
            new_window = Tk()
            Physioteraphy(new_window)
            new_window.mainloop()


        btn_back = Button(canvas, image=self.img_back, bg="#291C4F", activebackground="#291C4F", command=tts_back, borderwidth=0, highlightthickness=0)
        btn_back.pack()
        btn1 = Button(self.mental, image=self.img, borderwidth=0, width=1100, height=200, command=open_aerobics)
        btn1.place(x=90, y=237)
        btn2 = Button(self.mental, image=self.img2, borderwidth=0, width=1100, height=200, command=open_physioteraphy)
        btn2.place(x=90, y=440)


    def load_image(self):
        img = Image.open(self.img_path)
        img2 = Image.open(self.img2_path)
        img_back = Image.open(self.img3_path)
        self.img_back = ImageTk.PhotoImage(img_back)
        self.img = ImageTk.PhotoImage(img)
        self.img2 = ImageTk.PhotoImage(img2)   

if __name__ == "__main__":
    root = Tk()
    IntelectualMental(root)
    root.mainloop()
