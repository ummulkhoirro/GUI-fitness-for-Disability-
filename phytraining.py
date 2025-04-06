from tkinter import *
from PIL import Image, ImageTk
from customtkinter import *
from tkinter import messagebox
import os

from wheelchaircardio import Wheelchaircardio
from wheelchairfitness import Wheelchairfitness


class PhyTraining():
    
    def __init__(self, training):
        self.training = training
        self.training.title("FitInclusive")
        self.training.rowconfigure(0, weight=1)
        self.training.columnconfigure(0, weight=1)
        height = 720
        width = 1280
        x = (self.training.winfo_screenwidth() // 2) - (width // 2)
        y = (self.training.winfo_screenheight() // 4) - (height // 4)
        self.training.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.training.resizable(0, 0)
        self.training.config(bg="#291C4F")
        self.myfont = CTkFont(family='Poppins', size=14, weight='bold', slant='italic')

        def exit():
            sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=self.training)
            if sure:
                self.training.destroy()
        self.training.protocol("WM_DELETE_WINDOW", exit)
        # IMAGE

        self.img_path = ("D:\\pythonProject1\\pict\\cardio_wc-transformed.png")
        self.img2_path = ("D:\\pythonProject1\\pict\\wcfitness.png")
        self.img3_path = ("D:\\pythonProject1\\pict\\backbgremove.png")
        self.load_image()

        # LABEL
        canvas = Canvas(self.training, width=self.img_back.width(), height=self.img_back.height(), bg="#291C4F", bd=0, highlightthickness=0)
        canvas.place(x=20, y=20)
        
        Label_atas = Label(canvas, text="PHYSIC", bg="#291C4F", fg="white", font=("Italic, 35"))
        Label_atas.pack(side=RIGHT, padx=10)

        Label_text = Label(self.training, text="RECOMMENDED FOR YOU !!", font=self.myfont, bg="#291C4F", fg="white")
        Label_text.place(x=90, y=200)

        # BUTTON

        def open_wheelchaircardio():
            self.training.destroy()
            new_window = Tk()
            Wheelchaircardio(new_window)
            new_window.mainloop()        

#open wccardio
        
        def open_wheelchairfitness():
            self.training.destroy()
            new_window = Tk()
            Wheelchairfitness(new_window)
            new_window.mainloop()

        def back():
            self.training.destroy()




        btn_back = Button(canvas, image=self.img_back, bg="#291C4F", activebackground="#291C4F", borderwidth=0, highlightthickness=0, command=back)
        btn_back.pack()
        btn1 = Button(self.training, image=self.img, borderwidth=0, width=1100, height=200, command=open_wheelchaircardio)
        btn1.place(x=90, y=237)
        btn2 = Button(self.training, image=self.img2, borderwidth=0, width=1100, height=200, command=open_wheelchairfitness)
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
    PhyTraining(root)
    root.mainloop()
