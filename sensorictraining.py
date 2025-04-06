from tkinter import *
from PIL import Image, ImageTk
from customtkinter import CTkButton, CTkFont, CTkFrame, CTkLabel, CTkSwitch
from tkinter import messagebox
from gtts import gTTS
import os
import playsound
from tkinter import font
import datetime
import tkinter as tk
import random

from cardiosensory import CardioSensory
from fitsensory import FitSensory

class SensoricTraining():
    
    def __init__(self, sensoric):
        self.sensoric = sensoric
        self.click_count = 0
        self.click_count1 = 0
        self.click_count2 = 0
        self.sensoric.after(1000, self.open_sensortrain)
        self.sensoric.title("FitInclusive")
        self.sensoric.rowconfigure(0, weight=1)
        self.sensoric.columnconfigure(0, weight=1)
        height = 720
        width = 1280
        x = (self.sensoric.winfo_screenwidth() // 2) - (width // 2)
        y = (self.sensoric.winfo_screenheight() // 4) - (height // 4)
        self.sensoric.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.sensoric.resizable(0, 0)
        self.sensoric.config(bg="#291C4F")
        self.myfont = CTkFont(family='Poppins', size=14, weight='bold', slant='italic')

        def exit():
            sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=self.sensoric)
            if sure:
                self.sensoric.destroy()
        self.sensoric.protocol("WM_DELETE_WINDOW", exit)
        # IMAGE

        self.img_path = ("D:\\pythonProject1\\pict\\sensorycardio.png")
        self.img2_path = ("D:\\pythonProject1\\pict\\sensoryfitness.png")
        self.img3_path = ("D:\\pythonProject1\\pict\\backbgremove.png")
        self.load_image()

        # LABEL
        canvas = Canvas(self.sensoric, width=self.img_back.width(), height=self.img_back.height(), bg="#291C4F", bd=0, highlightthickness=0)
        canvas.place(x=20, y=20)
        
        Label_atas = Label(canvas, text="SENSORIC", bg="#291C4F", fg="white", font=("Italic, 35"))
        Label_atas.pack(side=RIGHT, padx=10)

        Label_text = Label(self.sensoric, text="RECOMMENDED FOR YOU !!", font=self.myfont, bg="#291C4F", fg="white")
        Label_text.place(x=90, y=200)

        # BUTTON

        def go_back():
            self.sensoric.destroy()

        def tts_back():
            self.click_count2 += 1
            if self.click_count2 == 1:
                speech = gTTS(text="back to previous page, tap again to go back", lang="en")
                filepath = "audio\\phyexercise.mp3"
                speech.save(filepath)
                try:
                    playsound.playsound(filepath)
                except playsound.PlaysoundException:
                    print("Error playing audio")
                finally:
                    os.remove(filepath)
            elif self.click_count2 == 2:
                go_back()
                self.click_count2 = 0

        def open_fitnessensory():
            self.sensoric.destroy()
            new_window = Tk()
            FitSensory(new_window)
            new_window.mainloop()        

        def tts_cardiosensory():
            self.click_count += 1
            if self.click_count == 1:
                speech = gTTS(text="Cardio for sensory, tap again here to open", lang="en")
                filepath = "audio\\phyexercise.mp3"
                speech.save(filepath)
                try:
                    playsound.playsound(filepath)
                except playsound.PlaysoundException:
                    print("Error playing audio")
                finally:
                    print("playing audio success")
                    os.remove(filepath)
            elif self.click_count == 2:
                open_cardiosensory()
                self.click_count = 0
        
        def open_cardiosensory():
            self.sensoric.destroy()
            new_window = Tk()
            CardioSensory(new_window)
            new_window.mainloop()

        def tts_fitsensory():
            self.click_count1 += 1
            if self.click_count1 == 1:
                speech = gTTS(text="Fitness for sensory, tap again here to open", lang="en")
                filepath = "audio\\phyexercise.mp3"
                speech.save(filepath)
                try:
                    playsound.playsound(filepath)
                except playsound.PlaysoundException:
                    print("Error playing audio")
                finally:
                    print("playing audio success")
                    os.remove(filepath)
            elif self.click_count1 == 2:
                open_fitnessensory()
                self.click_count1 = 0


        btn_back = Button(canvas, image=self.img_back, bg="#291C4F", activebackground="#291C4F", borderwidth=0, highlightthickness=0, command=tts_back)
        btn_back.pack()
        btn1 = Button(self.sensoric, image=self.img, borderwidth=0, width=1100, height=200, command=tts_cardiosensory)
        btn1.place(x=90, y=237)
        btn2 = Button(self.sensoric, image=self.img2, borderwidth=0, width=1100, height=200, command=tts_fitsensory)
        btn2.place(x=90, y=440)


    def load_image(self):
        img = Image.open(self.img_path)
        img2 = Image.open(self.img2_path)
        img_back = Image.open(self.img3_path)
        self.img_back = ImageTk.PhotoImage(img_back)
        self.img = ImageTk.PhotoImage(img)
        self.img2 = ImageTk.PhotoImage(img2)   

    def tts_sensorictrain(self):
        speech = gTTS(text="training for sensoric disabillity", lang="en")
        filepath = "audio\\phyexercise.mp3"
        speech.save(filepath)
        try:
            playsound.playsound(filepath)
        except playsound.PlaysoundException:
            print("Error playing audio file")
        finally:
            os.remove(filepath)


    def open_sensortrain(self):
        self.tts_sensorictrain()


if __name__ == "__main__":
    root = Tk()
    app = SensoricTraining(root)
    root.mainloop()
    app.go_back()
