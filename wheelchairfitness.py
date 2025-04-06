from tkinter import *
from PIL import Image, ImageTk
from customtkinter import CTkButton, CTkFont
from tkinter import messagebox

import os
import playsound 

from cardopole import CardioPole
from Strechingworkout import Streching
from upperbody import Upbody

class Wheelchairfitness():

    def __init__(self, fitness):
        self.fitness = fitness
        self.fitness.title("FitInclusive")
        self.fitness.rowconfigure(0, weight=1)
        self.fitness.columnconfigure(0, weight=1)
        height = 720
        width = 1280
        x = (self.fitness.winfo_screenwidth() // 2) - (width // 2)
        y = (self.fitness.winfo_screenheight() // 2) - (height // 2)
        self.fitness.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.fitness.resizable(0, 0)
        self.fitness.config(bg="#291C4F")
        self.myfont = CTkFont(family='Poppins', size=14, weight='bold', slant='italic')

        # IMAGE

        self.img_path1 = "D:\\pythonProject1\\pict\\Cardio pole.png"
        self.img_path2 = "D:\\pythonProject1\\pict\\backbutton2.png"
        self.img_path3 = "D:\\pythonProject1\\pict\\wcnexticon.png"
        self.img_path4 = "D:\\pythonProject1\\pict\\Stretchingpict.png"
        self.img_path5 = "D:\\pythonProject1\\pict\\Upper body.png"
        self.load_image()

        # CANVAS

        canvas = Canvas(self.fitness, width=self.img_back.width(), height=self.img_back.height(), bg="#291C4F", bd=0, highlightthickness=0)
        canvas.place(x=20, y=20)

        canvas2 = Canvas(self.fitness, width=1080, height=150, bg="#291C4F", borderwidth=0, highlightthickness=0)
        canvas2.place(x=100, y=155)
        inner_canvas2 = Canvas(self.fitness, width=200, height=150, bg="#7f7b7b", borderwidth=0, highlightthickness=0)
        inner_canvas2.place(x=100, y=155)

        canvas3 = Canvas(self.fitness, width=1080, height=150, bg="#291C4F", borderwidth=0, highlightthickness=0)
        canvas3.place(x=100, y=345)
        inner_canvas3 = Canvas(self.fitness, width=200, height=150, bg="#7f7b7b", borderwidth=0, highlightthickness=0)
        inner_canvas3.place(x=100, y=345)

        canvas4 = Canvas(self.fitness, width=1080, height=150, bg="#291c4f", borderwidth=0, highlightthickness=0)
        canvas4.place(x=100, y=535)
        inner_canvas4 = Canvas(self.fitness, width=200, height=150, bg="#7F7B7B", borderwidth=0, highlightthickness=0)
        inner_canvas4.place(x=100, y=535)

        # LABEL

        Label_text = Label(self.fitness, text="15 EXERCISE", font=self.myfont, bg="#291C4F", fg="white")
        Label_text.place(x=100, y=120)

        Label_pojok = Label(canvas, text="wheelchair fitness", bg="#291C4F", fg="white", font=("Italic, 25"))
        Label_pojok.pack(side=RIGHT, padx=10)

        # BUTTON

        def open_cardiopole():
            self.fitness.destroy()
            new_window = Tk()
            CardioPole(new_window)
            new_window.mainloop()

        def open_streching():
            self.fitness.destroy()
            new_window = Tk()
            Streching(new_window)
            new_window.mainloop()

        def open_upperbody():
            self.fitness.destroy()
            new_window = Tk()
            Upbody(new_window)
            new_window.mainloop()

        def back():
            self.cardio.destroy()

        btn1 = Button(canvas2, image=self.img_next, bg="#291C4F", activebackground="#291C4F", width=200, height=145, borderwidth=0, highlightthickness=0, command=open_cardiopole)
        btn1.pack()

        btn2 = Button(canvas3, image=self.img_next, bg="#291C4F", activebackground="#291C4F", width=200, height=145, borderwidth=0, highlightthickness=0, command=open_streching)
        btn2.pack()

        btn3 = Button(canvas4, image=self.img_next, bg="#291C4F", activebackground="#291C4F", width=200, height=145, borderwidth=0, highlightthickness=0, command=open_upperbody)
        btn3.pack()

        btn_back = CTkButton(master=canvas,
                             image=self.img_back,
                             fg_color="#291C4F",
                             hover_color="291C4F",
                             width=50,
                             text='',
                             command=back)
        btn_back.pack()

        def exit():
            sure = messagebox.askyesno("Exit", "Are you sure you want to exit", parent=self.fitness)
            if sure:
                self.fitness.destroy()

        self.fitness.protocol("WM_DELETE_WINDOW", exit)
        self.insert_image(inner_canvas2, self.img, x_coord=100, y_coord=60)
        self.insert_image(inner_canvas3, self.img2, x_coord=80, y_coord=80)
        self.insert_image(inner_canvas4, self.img3, x_coord=50, y_coord=80)

        canvas2.create_text(560, 25, text="Cardio Pole Workout", font=("Italic, 25"), fill="white")
        canvas2.create_text(560, 50, text="10 minutes", font=self.myfont, fill="white")
        canvas3.create_text(560, 25, text="Streching Workout", font=("Italic 25"), fill="white")
        canvas3.create_text(560, 50, text="10 minutes", font=self.myfont, fill="white")
        canvas4.create_text(560, 25, text="Upperbody Strength Workout", font=("Italic 25"), fill="white")
        canvas4.create_text(560, 50, text="10 minutes", font=self.myfont, fill="white")

        x_right = 1080
        y_center = 75
        canvas2.create_window(x_right, y_center, window=btn1, anchor=E)
        canvas3.create_window(x_right, y_center, window=btn2, anchor=E)
        canvas4.create_window(x_right, y_center, window=btn3, anchor=E)


    def load_image(self):
        img = Image.open(self.img_path1)
        img2 = Image.open(self.img_path4)
        img3 = Image.open(self.img_path5)
        width = 200
        height = 150

        def resize_image(image, width, height):
            width_ratio = width / image.width
            height_ratio = height / image.height
            resize_ratio = min(width_ratio, height_ratio)
            new_width = int(image.width * resize_ratio)
            new_height = int(image.height * resize_ratio)
            return image.resize((new_width, new_height), Image.LANCZOS)

        img = resize_image(img, width, height)
        img2 = resize_image(img2, width, height)
        img3 = resize_image(img3, width, height)

        img_back = Image.open(self.img_path2)
        img_next = Image.open(self.img_path3)
        img_next = resize_image(img_next, 50, 80)

        self.img = ImageTk.PhotoImage(img)
        self.img2 = ImageTk.PhotoImage(img2)
        self.img3 = ImageTk.PhotoImage(img3)

        
        self.img_back = ImageTk.PhotoImage(img_back)
        self.img_next = ImageTk.PhotoImage(img_next)

        return self.img, self.img2, self.img3
    
    def insert_image(self, canvas, img, x_coord, y_coord):
        canvas.create_image(x_coord, y_coord, image=img)

if __name__ == "__main__":
    root = Tk()
    Wheelchairfitness(root)
    root.mainloop()
