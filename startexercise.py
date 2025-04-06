from tkinter import *
from PIL import Image, ImageTk
from customtkinter import CTkButton, CTkFont, CTkFrame, CTkLabel, CTkSwitch
from tkinter import messagebox
import os

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

        self.current_time = 20.0  # Duration in seconds
        self.exercise_num = 0
        self.total_exercises = 15
        self.calories_list = [22, 25, 20, 18, 30, 26, 24, 28, 32, 21, 27, 23, 29, 19, 31]

        self.exercise_names = ['Exercise A', 'Exercise B', 'Exercise C', 'Exercise D', 'Exercise E', 
                               'Exercise F', 'Exercise G', 'Exercise H', 'Exercise I', 'Exercise J',
                               'Exercise K', 'Exercise L', 'Exercise M', 'Exercise N', 'Exercise O']

        self.exercise_durations = [20.0, 25.0, 30.0, 22.0, 27.0, 28.0, 21.0, 24.0, 26.0, 23.0,
                                   18.0, 29.0, 31.0, 32.0, 19.0]

        self.img_path1 = "D:\\pythonProject1\\pict\\wheelchair.png"
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
        self.back_button = CTkButton(main_frame, height=40, width=200, corner_radius=30,text="Back", command=self.back, fg_color="#92A4D7", text_color="black")
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
                self.current_time = 0
                self.time_label.configure(text="00.00")

        self.timer.after(10, self.update_timer)

    def pause(self):
        self.paused = not self.paused
        self.pause_button.configure(text="Pause" if not self.paused else "Resume")

    def back(self):
        # Functionality to go back to the previous exercise
        if self.exercise_num > 0:
            self.exercise_num -= 1
            self.exercise_label.configure(text=f"{self.exercise_names[self.exercise_num]} {self.exercise_num + 1}/{self.total_exercises}")
            self.calories_label.configure(text=f"Kal\n{self.calories_list[self.exercise_num]}")

    def next(self):
        # Functionality to go to the next exercise
        if self.exercise_num < self.total_exercises - 1:
            self.exercise_num += 1
            self.exercise_label.configure(text=f"{self.exercise_names[self.exercise_num]} {self.exercise_num + 1}/{self.total_exercises}")
            self.current_time = self.exercise_durations[self.exercise_num]  # Duration for the next exercise
            self.time_label.configure(text=f"{self.current_time:05.2f}")
            self.calories_label.configure(text=f"Kal\n{self.calories_list[self.exercise_num]}")
            self.pause()




if __name__ == "__main__":
    root = Tk()
    Timer(root)
    root.mainloop()
