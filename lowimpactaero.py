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


class LowImpactAero():

    def __init__(self, lia):
        self.lia = lia
        self.click_count = 0
        self.lia.after(1000, self.open_lowimpact)
        self.lia.title("FitInclusive")
        self.lia.rowconfigure(0, weight=1)
        self.lia.columnconfigure(0, weight=1)
        height = 720
        width = 1280
        x = (self.lia.winfo_screenwidth() // 2) - (width // 2)
        y = (self.lia.winfo_screenheight() // 2) - (height // 2)
        self.lia.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.lia.resizable(0, 0)
        self.lia.config(bg="#291C4F")
        self.myfont = CTkFont(family='Poppins', size=14, weight='bold', slant='italic')

        self.img_path1 = "D:\\pythonProject1\\pict\\Low impact.png"
        self.img_path2 = "D:\\pythonProject1\\pict\\lowimpact.png"#if not self.is_go else "C:\\Users\\Hanseok\\Documents\\project sda\\bgrounded4.png"
        self.img_path3 = "D:\\pythonProject1\\pict\\backbutton2.png"
        self.load_image()
        self.main_frame()

        def exit():
            sure = messagebox.askyesno("Exit", "Are you sure you want to exit", parent=self.lia)
            if sure:
                self.lia.destroy()
        
        self.lia.protocol("WM_DELETE_WINDOW", exit)


    def load_image(self):
        image1 = Image.open(self.img_path1)
        width = 200
        height = 150
        width_ratio = width / image1.width
        height_ratio = height / image1.height
        resize_ratio = min(width_ratio, height_ratio)
        new_width = int(image1.width * resize_ratio)
        new_height = int(image1.height * resize_ratio)
        image1 = image1.resize((new_width, new_height), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(image1)

        img_back = Image.open(self.img_path3)
        self.img_back = ImageTk.PhotoImage(img_back)

        image2 = Image.open(self.img_path2)
        image2 = image2.resize((1280, 560), Image.LANCZOS)
        self.photo_bg = ImageTk.PhotoImage(image2)


    def main_frame(self):

        def tts_back():
            speech = gTTS("back to previous page, tap again to go back", lang="en")
            filepath = ("ewc_back.mp3")
            speech.save(filepath)
            try:
                playsound.playsound(filepath)
            except playsound.PlaysoundException:
                print("Error playing audio")
            finally:
                os.remove(filepath)

        def open_next_window():
            self.lia.destroy()
            new_window = Tk()
            Timer(new_window)
            new_window.mainloop()

        def tts_action():
            self.click_count += 1
            if self.click_count == 1:
                speech = gTTS("Start button. Tap again here to start", lang="en")
                filepath = ("sbtn.mp3")
                speech.save(filepath)
                try:
                    playsound.playsound(filepath)
                except playsound.PlaysoundException:
                    print("Error playing audio")
                finally:
                    os.remove(filepath)
            elif self.click_count == 2:
                open_next_window()
                self.click_count = 0

        frame_utama = CTkFrame(self.lia, fg_color="#291C4F", bg_color="#291C4F")
        frame_utama.pack(fill='both', expand=True)

        label_title = Label(frame_utama, height=150, image=self.photo, bg="#291C4F", fg="#291C4F")
        label_title.pack(anchor="center")

        btn_back = CTkButton(master=frame_utama, image=self.img_back, bg_color="#291C4F", fg_color="#291C4F",
                             hover_color="#291C4F", width=50, text='', anchor='', command=tts_back)
        btn_back.place(x=10, y=10)  

        frame_tengah = CTkFrame(frame_utama, height=700, width=1280, fg_color="#291C4F")
        frame_tengah.pack(fill='both', side='bottom', expand=True)

        bg_label = CTkLabel(frame_tengah, image=self.photo_bg, text="")
        bg_label.pack(fill='both', expand=True)

        button_action = CTkButton(master=frame_tengah, width=120, height=40, text="START", bg_color="white", fg_color="#179551", hover_color="#179551", corner_radius=30,command=tts_action)
        button_action.place(relx=0.5, rely=0.3, anchor='center')

    def tts_lowimpact(self):
        speech = gTTS("Low impact aerobic", lang="en")
        filepath = ("lia.mp3")
        speech.save(filepath)
        try:
            playsound.playsound(filepath)
        except playsound.PlaysoundException:
            print("Error playing audio")
        finally:
            os.remove(filepath)

    def open_lowimpact(self):
        self.tts_lowimpact()

class ResultsPage:
    def __init__(self, result_window, total_time, total_calories):
        self.total_time = total_time
        self.total_calories = total_calories
        self.image_path = "D:\\pythonProject1\\gambar\\img.png"  # Path file gambar
        self.load_image(result_window)

        myfont = font.Font(family='Poppins', size=10, weight='bold', slant='italic')

        height = 720
        width = 1280
        result_window.geometry('{}x{}+{}+{}'.format(width, height, (result_window.winfo_screenwidth() // 2) - (width // 2), (result_window.winfo_screenheight() // 2) - (height // 2)))
        result_window.resizable(0, 0)
        result_window.config(bg="#291C4F")

        self.create_widgets(result_window, myfont)

    def load_image(self, result_window):
        self.image_tk = tk.PhotoImage(file=self.image_path)
        self.canvas = tk.Canvas(result_window, width=1280, height=720)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image_tk)

    def create_widgets(self, result_window, myfont):
        # Date Label
        date_label = Label(result_window, text=f"{datetime.datetime.now().strftime('%d %B %Y')}", font=myfont, bg="#FFFFFF", fg="#291C4F")
        date_label.place(x=230, y=450)

        # Time Label
        time_label = Label(result_window, text=f"{datetime.datetime.now().strftime('%H:%M')}", font=myfont, bg="#FFFFFF", fg="#291C4F")
        time_label.place(x=258, y=560)

        # Duration Labels
        duration_label = Label(result_window, text="Time", font=myfont, bg="#FFFFFF", fg="#291C4F")
        duration_label.place(x=257, y=590)
        duration_result_label = Label(result_window, text=f"{self.total_time / 60:.2f} minutes", font=myfont, bg="#FFFFFF", fg="#000000")
        duration_result_label.place(x=450, y=590)

        # Calories Labels
        calories_label = Label(result_window, text="Calories", font=myfont, bg="#FFFFFF", fg="#291C4F")
        calories_label.place(x=652, y=590)
        calories_result_label = Label(result_window, text=f"{self.total_calories:.2f} kcal", font=myfont, bg="#FFFFFF", fg="#291C4F")
        calories_result_label.place(x=650, y=560)

class Timer:
    def __init__(self, timer):
        self.timer = timer
        self.click_count = 0
        self.click_count1 = 0
        self.timer.after(1000)
        self.timer.title("FitInclusive")
        self.timer.rowconfigure(0, weight=1)
        self.timer.columnconfigure(0, weight=1)
        height = 720
        width = 1280
        x = (self.timer.winfo_screenwidth() // 2) - (width // 2)
        y = (self.timer.winfo_screenheight() // 2) - (height // 2)
        self.timer.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.timer.resizable(0, 0)
        self.timer.config(bg="#291C4F")
        self.myfont = CTkFont(family='Poppins', size=14, weight='bold', slant='italic')

        self.current_time = 60.0  # Duration in seconds
        self.exercise_num = 0
        self.total_exercises = 10
        self.calories_list = [6, 4, 6, 4, 6, 4, 6, 4, 6, 4]
        self.total_time = 0
        self.total_calories = 0

        self.exercise_names = ['Marching in Place', 'Seated Arm Circles', 'Step Touch', 'Seated Toe Taps', 'Seated High Knees',
                               'Low Impact Jumping Jacks', 'Shoulder Press', 'Side Bends', 'Leg Lifts', 'Marches']

        self.exercise_durations = [60, 60, 60, 60, 60, 60, 60, 60, 60, 60]

        self.img_path1 = "D:\\pythonProject1\\pict\\Low impact.png"
        self.load_image()
        self.create_widgets()
        self.update_timer()

    def load_image(self):
        image1 = Image.open(self.img_path1)
        width = 600
        height = 600
        width_ratio = width / image1.width
        height_ratio = height / image1.height
        resize_ratio = min(width_ratio, height_ratio)
        new_width = int(image1.width * resize_ratio)
        new_height = int(image1.height * resize_ratio)
        image1 = image1.resize((new_width, new_height), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(image1)

    def create_widgets(self):
        # Frame for the main content
        main_frame = CTkFrame(self.timer, fg_color="#CFCFCF")
        main_frame.pack(fill='both', expand=True )

        # Placeholder for Image
        self.image_frame = CTkLabel(main_frame, text="", width=300, height=300, bg_color="#CFCFCF", image=self.photo)
        self.image_frame.place(relx=0.5, rely=0.2, anchor=CENTER)

        info_frame = CTkFrame(main_frame, width=1280, height=150, fg_color="#ECECEC")
        info_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Timer display
        self.time_label = CTkLabel(info_frame, text=f"{self.current_time:05.2f}", font=("Arial", 40), text_color="black")
        self.time_label.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Duration
        self.duration_label = CTkLabel(info_frame, text=f"Duration\n{self.current_time:05.2f}", font=("Arial", 20), text_color="black")
        self.duration_label.place(relx=0.2, rely=0.5, anchor=CENTER)

        # Calories
        self.calories_label = CTkLabel(info_frame, text=f"Kal\n{self.calories_list[self.exercise_num]}", font=("Arial", 20), text_color="black")
        self.calories_label.place(relx=0.8, rely=0.5, anchor=CENTER)

        # Exercise Count
        self.exercise_label = CTkLabel(main_frame, text=f"{self.exercise_names[self.exercise_num]} {self.exercise_num + 1}/{self.total_exercises}", font=("Arial", 20), text_color="black")
        self.exercise_label.place(relx=0.9, rely=0.1, anchor=CENTER)

        # Buttons
        self.back_button = CTkButton(main_frame, height=40, width=200, corner_radius=30, text="Back", command=self.back, fg_color="#92A4D7", text_color="black")
        self.back_button.place(relx=0.3, rely=0.7, anchor=CENTER)

        self.next_button = CTkButton(main_frame, height=40, width=200, corner_radius=30, text="Next", command=self.next, fg_color="#92A4D7", text_color="black")
        self.next_button.place(relx=0.7, rely=0.7, anchor=CENTER)

        self.pause_button = CTkButton(main_frame, height=40, width=200, corner_radius=30, text="Start", command=self.pause, fg_color="red", text_color="white")
        self.pause_button.place(relx=0.5, rely=0.8, anchor=CENTER)

        # Initialize Timer state
        self.paused = True

    def update_timer(self):
        if not self.paused:
            if self.current_time > 0:
                self.current_time -= 0.01
                self.time_label.configure(text=f"{self.current_time:05.2f}")
            else:
                self.next_exercise()

        self.timer.after(10, self.update_timer)

    def pause(self):
        self.paused = not self.paused
        self.pause_button.configure(text="Pause" if not self.paused else "Resume")

    def back(self):
        if self.exercise_num > 0:
            self.exercise_num -= 1
            self.exercise_label.configure(text=f"{self.exercise_names[self.exercise_num]} {self.exercise_num + 1}/{self.total_exercises}")
            self.current_time = self.exercise_durations[self.exercise_num]  # Update duration for previous exercise
            self.time_label.configure(text=f"{self.current_time:05.2f}")
            self.calories_label.configure(text=f"Kal\n{self.calories_list[self.exercise_num]}")
            self.pause()

    def next(self):
        elapsed_time = self.exercise_durations[self.exercise_num] - self.current_time
        self.total_time += elapsed_time
        calories_burned = (self.calories_list[self.exercise_num] / self.exercise_durations[self.exercise_num]) * elapsed_time
        self.total_calories += calories_burned

        if self.exercise_num < self.total_exercises - 1:
            self.exercise_num += 1
            self.current_time = self.exercise_durations[self.exercise_num]
            self.exercise_label.configure(text=f"{self.exercise_names[self.exercise_num]} {self.exercise_num + 1}/{self.total_exercises}")
            self.time_label.configure(text=f"{self.current_time / 60:05.2f}")
            self.calories_label.configure(text=f"Kal\n{self.calories_list[self.exercise_num]}")
            self.pause()
        else:
            self.show_result()

    def show_result(self):
        self.timer.withdraw()
        result_window = Toplevel(self.timer)
        ResultsPage(result_window, self.total_time, self.total_calories)


if __name__ == "__main__":
    lia = Tk()
    app = LowImpactAero(lia)
    lia.mainloop()
