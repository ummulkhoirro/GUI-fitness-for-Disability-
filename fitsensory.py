from tkinter import *
from PIL import Image, ImageTk
from customtkinter import CTkButton, CTkFont
from tkinter import messagebox
from gtts import gTTS
import os
import playsound 

from resistanceband import ResistanceBand
from balancecoor import BalanceCoordination
from strengthweight import StrengthWeight

class FitSensory():

    def __init__(self, Fsensor):
        self.Fsensor = Fsensor
        self.click_count = 0
        self.click_count1 = 0
        self.click_count2 = 0
        self.Fsensor.after(1000, self.open_Fsensor)
        self.Fsensor.title("FitInclusive")
        self.Fsensor.rowconfigure(0, weight=1)
        self.Fsensor.columnconfigure(0, weight=1)
        height = 720
        width = 1280
        x = (self.Fsensor.winfo_screenwidth() // 2) - (width // 2)
        y = (self.Fsensor.winfo_screenheight() // 2) - (height // 2)
        self.Fsensor.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.Fsensor.resizable(0, 0)
        self.Fsensor.config(bg="#291C4F")
        self.myfont = CTkFont(family='Poppins', size=14, weight='bold', slant='italic')

        # IMAGE

        self.img_path1 = "D:\\pythonProject1\\pict\\blind.png"
        self.img_path2 = "D:\\pythonProject1\\pict\\backbutton2.png"
        self.img_path3 = "D:\\pythonProject1\\pict\\wcnexticon.png"
        self.load_image()

        # CANVAS

        canvas = Canvas(self.Fsensor, width=self.img_back.width(), height=self.img_back.height(), bg="#291C4F", bd=0, highlightthickness=0)
        canvas.place(x=20, y=20)

        canvas2 = Canvas(self.Fsensor, width=1080, height=150, bg="#291C4F", borderwidth=0, highlightthickness=0)
        canvas2.place(x=100, y=155)
        inner_canvas2 = Canvas(self.Fsensor, width=200, height=150, bg="#7f7b7b", borderwidth=0, highlightthickness=0)
        inner_canvas2.place(x=100, y=155)

        canvas3 = Canvas(self.Fsensor, width=1080, height=150, bg="#291C4F", borderwidth=0, highlightthickness=0)
        canvas3.place(x=100, y=345)
        inner_canvas3 = Canvas(self.Fsensor, width=200, height=150, bg="#7f7b7b", borderwidth=0, highlightthickness=0)
        inner_canvas3.place(x=100, y=345)

        canvas4 = Canvas(self.Fsensor, width=1080, height=150, bg="#291c4f", borderwidth=0, highlightthickness=0)
        canvas4.place(x=100, y=535)
        inner_canvas4 = Canvas(self.Fsensor, width=200, height=150, bg="#7F7B7B", borderwidth=0, highlightthickness=0)
        inner_canvas4.place(x=100, y=535)

        # LABEL

        Label_text = Label(self.Fsensor, text="3 EXERCISE", font=self.myfont, bg="#291C4F", fg="white")
        Label_text.place(x=100, y=120)

        Label_pojok = Label(canvas, text="Fitness for Sensory", bg="#291C4F", fg="white", font=("Italic, 25"))
        Label_pojok.pack(side=RIGHT, padx=10)

        # BUTTON

        def open_resband():
            self.Fsensor.destroy()
            new_window = Tk()
            ResistanceBand(new_window)
            new_window.mainloop()

        def tts_btn1():
            self.click_count += 1
            if self.click_count == 1:
                speech = gTTS("Resitance Band Exercise. Tap again here to open", lang="en")
                filepath = ("lowimp.mp3")
                speech.save(filepath)
                try:
                    playsound.playsound(filepath)
                except playsound.PlaysoundException:
                    print("Error playing audio")
                finally:
                    os.remove(filepath)
            elif self.click_count == 2:
                open_resband()
                self.click_count = 0
        
        def open_balancecoor():
            self.Fsensor.destroy()
            new_window = Tk()
            BalanceCoordination(new_window)
            new_window(mainloop)

        def tts_btn2():
            self.click_count1 += 1
            if self.click_count1 == 1:
                speech = gTTS("Balance and Coordination Exercises. Tap again here to open", lang="en")
                filepath = ("seated.mp3")
                speech.save(filepath)
                try:
                    playsound.playsound(filepath)
                except playsound.PlaysoundException:
                    print("Error playing audio")
                finally:
                    os.remove(filepath)
            elif self.click_count1 == 2:
                open_balancecoor()
                self.click_count1 = 0
        
        def open_strengthweight():
            self.Fsensor.destroy()
            new_window = Tk()
            StrengthWeight(new_window)
            new_window.mainloop()

        def tts_btn3():
            self.click_count2 += 1
            if self.click_count2 == 1:
                speech = gTTS("Strength Training with Weights. Tap again here to open", lang="en")
                filepath = ("rythmd.mp3")
                speech.save(filepath)
                try:
                    playsound.playsound(filepath)
                except playsound.PlaysoundException:
                    print("Error playing audio")
                finally:
                    os.remove(filepath)
            elif self.click_count2 == 2:
                open_strengthweight()
                self.click_count2 = 0

        def tts_back():
            speech = gTTS("back to previous page, tap again to go back", lang="en")
            filepath = ("backbutton.mp3")
            speech.save(filepath)
            try:
                playsound.playsound(filepath)
            except playsound.PlaysoundException:
                print("Error playing audio")
            finally:
                os.remove(filepath)


        btn1 = Button(canvas2, image=self.img_next, bg="#291C4F", activebackground="#291C4F", width=200, height=145, borderwidth=0, highlightthickness=0, command=tts_btn1)
        btn1.pack()

        btn2 = Button(canvas3, image=self.img_next, bg="#291C4F", activebackground="#291C4F", width=200, height=145, borderwidth=0, highlightthickness=0, command=tts_btn2)
        btn2.pack()

        btn3 = Button(canvas4, image=self.img_next, bg="#291C4F", activebackground="#291C4F", width=200, height=145, borderwidth=0, highlightthickness=0, command=tts_btn3)
        btn3.pack()

        btn_back = CTkButton(master=canvas,
                             image=self.img_back,
                             fg_color="#291C4F",
                             hover_color="291C4F",
                             width=50,
                             text='',
                             command=tts_back)
        btn_back.pack()

        def exit():
            sure = messagebox.askyesno("Exit", "Are you sure you want to exit", parent=self.Fsensor)
            if sure:
                self.Fsensor.destroy()

        self.Fsensor.protocol("WM_DELETE_WINDOW", exit)
        self.insert_image(inner_canvas2, x_coord=100, y_coord=80)
        self.insert_image(inner_canvas3, x_coord=100, y_coord=80)
        self.insert_image(inner_canvas4, x_coord=100, y_coord=80)

        canvas2.create_text(560, 25, text="Resitance Band Exercise", font=("Italic, 25"), fill="white")
        canvas2.create_text(560, 50, text="10 minutes", font=self.myfont, fill="white")
        canvas3.create_text(560, 25, text="Balance and Coordination Exercises", font=("Italic 25"), fill="white")
        canvas3.create_text(560, 50, text="10 minutes", font=self.myfont, fill="white")
        canvas4.create_text(560, 25, text="Strength Training with Weights", font=("Italic 25"), fill="white")
        canvas4.create_text(560, 50, text="10 minutes", font=self.myfont, fill="white")

        x_right = 1080
        y_center = 75
        canvas2.create_window(x_right, y_center, window=btn1, anchor=E)
        canvas3.create_window(x_right, y_center, window=btn2, anchor=E)
        canvas4.create_window(x_right, y_center, window=btn3, anchor=E)


    def load_image(self):
        img = Image.open(self.img_path1)
        width = 200
        height = 150
        width_ratio = width / img.width
        height_ratio = height / img.height
        resize_ratio = min(width_ratio, height_ratio)
        new_width = int(img.width * resize_ratio)
        new_height = int(img.height * resize_ratio)
        img = img.resize((new_width, new_height), Image.LANCZOS)
        img_back = Image.open(self.img_path2)
        img_next = Image.open(self.img_path3)
        self.img = ImageTk.PhotoImage(img)
        self.img_back = ImageTk.PhotoImage(img_back)
        img_next = img_next.resize((50, 80), Image.LANCZOS)
        self.img_next = ImageTk.PhotoImage(img_next)
        return self.img
    
    def tts_wcFsensor(self):
        speech = gTTS("Fitness for sensory", lang="en")
        filepath = ("wheelchair_Fsensor.mp3")
        speech.save(filepath)
        try:
            playsound.playsound(filepath)
        except playsound.PlaysoundException:
            print("Error playing audio")
        finally:
            os.remove(filepath)

    def open_Fsensor(self):
        self.tts_wcFsensor()

    def insert_image(self, canvas, x_coord, y_coord):
        canvas.create_image(x_coord, y_coord, image=self.img)

if __name__ == "__main__":
    root = Tk()
    FitSensory(root)
    root.mainloop()
