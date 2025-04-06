import tkinter as tk
from tkinter import font
from tkVideoPlayer import TkinterVideo
import time
from datetime import datetime
from tkcalendar import Calendar
import random

class EasyCWorkout3:

    def __init__(self, cworkout3):
        self.cworkout = cworkout3
        self.click_count = 0
        self.click_count1 = 0
        self.start_time = time.time()
        self.elapsed_time = 0
        self.calories_burned = 0
        self.is_paused = False
        self.video_path = "gambar\\easy workout.mp4"  # Set the path to your video file
        self.after_id = None  # Track the after ID for cancelling
        
        self.cworkout.title("FitInclusive")
        self.cworkout.rowconfigure(0, weight=1)
        self.cworkout.columnconfigure(0, weight=1)
        height = 720
        width = 1280
        x = (self.cworkout.winfo_screenwidth() // 2) - (width // 2)
        y = (self.cworkout.winfo_screenheight() // 2) - (height // 2)
        self.cworkout.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.cworkout.resizable(0, 0)
        self.cworkout.config(bg="#291C4F")
        self.myfont = font.Font(family='Poppins', size=14, weight='bold', slant='italic')
        
        self.video_player = TkinterVideo(master=self.cworkout, scaled=True)
        try:
            self.video_player.load(self.video_path)
        except Exception as e:
            print(f"Error loading video: {e}")
            # Handle error here, e.g., show an error message to the user
            return
        
        self.video_player.place(relx=0.5, rely=0.4, anchor="center", width=width, height=int(height * 0.6))
        
        self.pause_button = tk.Button(self.cworkout, text="PAUSE", command=self.pause_video, font=self.myfont, bg="#FFDDC1")
        self.pause_button.place(relx=0.5, rely=0.8, anchor="center")
        
        self.skip_button = tk.Label(self.cworkout, text="Skip", font=self.myfont, bg="#FFDDC1", cursor="hand2")
        self.skip_button.place(relx=0.9, rely=0.1, anchor="center")
        self.skip_button.bind("<Button-1>", self.skip_video)
        
        self.time_label = tk.Label(self.cworkout, text="Time: 0s", font=self.myfont, bg="#291C4F", fg="#FFFFFF")
        self.time_label.place(relx=0.1, rely=0.9, anchor="w")
        
        self.calories_label = tk.Label(self.cworkout, text="Calories: 0", font=self.myfont, bg="#291C4F", fg="#FFFFFF")
        self.calories_label.place(relx=0.9, rely=0.9, anchor="e")
        
        self.update_time_and_calories()

        # List to store workout dates
        self.workout_dates = []
        
        if self.video_player:
            self.video_player.play()
            self.start_time = time.time()

    def pause_video(self):
        if self.video_player and self.video_player.is_paused():
            self.video_player.play()
            self.pause_button.config(text="PAUSE")
            self.start_time = time.time() - self.elapsed_time  # Continue counting from where it stopped
            self.is_paused = False
        else:
            self.video_player.pause()
            self.pause_button.config(text="PLAY")
            self.elapsed_time = time.time() - self.start_time  # Capture the time elapsed so far
            self.is_paused = True

    def update_time_and_calories(self):
        if self.video_player and not self.is_paused:
            self.elapsed_time = time.time() - self.start_time
            self.time_label.config(text=f"Time: {int(self.elapsed_time)}s")
            
            # Assuming a fixed burn rate of 100 calories for 15 minutes exercise
            total_duration_minutes = 15
            total_calories = 100
            calories_per_second = total_calories / (total_duration_minutes * 60)
            self.calories_burned = self.elapsed_time * calories_per_second
            self.calories_label.config(text=f"Calories: {self.calories_burned:.2f}")
        
        # Schedule the next update
        self.after_id = self.cworkout.after(1000, self.update_time_and_calories)

    def skip_video(self, event):
        if self.video_player:
            self.video_player.stop()
        self.add_current_date()
        self.show_results()

    def add_current_date(self):
        today = datetime.now()
        self.workout_dates.append(today)

    def show_results(self):
        # Cancel the after callback before destroying the window
        if self.after_id:
            self.cworkout.after_cancel(self.after_id)
        self.cworkout.destroy()
        result_window = tk.Tk()
        ResultsPage(result_window, int(self.elapsed_time), self.calories_burned, self.workout_dates)
        result_window.mainloop()

class ResultsPage:

    def __init__(self, result_window, elapsed_time, calories_burned, workout_dates):
        height = 720
        width = 1280
        self.image_path = "gambar\\Vid_bg.png"  # Path file gambar
        self.load_image(result_window)
        
        myfont = font.Font(family='Poppins', size=10, weight='bold', slant='italic')

        result_window.geometry('{}x{}+{}+{}'.format(width, height, (result_window.winfo_screenwidth() // 2) - (width // 2), (result_window.winfo_screenheight() // 2) - (height // 2)))
        result_window.resizable(0, 0)
        result_window.config(bg="#291C4F")

        # Label for Workout Summary
        result_label = tk.Label(result_window, text="Easy Cardio Workout", font=myfont, bg="#FFFFFF", fg="#291C4F")
        result_label.place(x=250, y=480)

        # Label for Date
        date_label = tk.Label(result_window, text=f"{datetime.now().strftime('%d %B %Y')}", font=myfont, bg="#FFFFFF", fg="#291C4F")
        date_label.place(x=230, y=450)

        # Label for Time
        time_label = tk.Label(result_window, text=f"{datetime.now().strftime('%H:%M')}", font=myfont, bg="#FFFFFF", fg="#291C4F")
        time_label.place(x=258, y=560)

        # Label for Duration
        duration_label = tk.Label(result_window, text="Time", font=myfont, bg="#FFFFFF", fg="#291C4F")
        duration_label.place(x=257, y=590)

        # Result for Duration (Random)
        random_hour = random.randint(0, 23)
        random_minute = random.randint(0, 59)
        duration_result_label = tk.Label(result_window, text=f"{random_hour:02d}:{random_minute:02d}", font=myfont, bg="#FFFFFF", fg="#291C4F")
        duration_result_label.place(x=450, y=590)

        # Label for Exercise Text
        exercise_text_label = tk.Label(result_window, text="Exercise", font=myfont, bg="#FFFFFF", fg="#291C4F")
        exercise_text_label.place(x=980, y=560)

        # Generating random exercise text
        exercises = ["1","2","3","4","5","6","7","8","9","10"]
        random_exercise = random.choice(exercises)

        # Result for Exercise Text
        exercise_text_result_label = tk.Label(result_window, text=random_exercise, font=myfont, bg="#FFFFFF", fg="#291C4F")
        exercise_text_result_label.place(x=1000, y=535)

        # Label for Time
        time_label = tk.Label(result_window, text="Duration", font=myfont, bg="#FFFFFF", fg="#291C4F")
        time_label.place(x=455, y=590)
        
        # Result for Time
        time_result_label = tk.Label(result_window, text=f"{elapsed_time} seconds", font=myfont, bg="#FFFFFF", fg="#291C4F")
        time_result_label.place(x=450, y=560)

        # Label for Calories
        calories_label = tk.Label(result_window, text="Calories", font=myfont, bg="#FFFFFF", fg="#291C4F")
        calories_label.place(x=652, y=590)
        
        # Result for Calories
        calories_result_label = tk.Label(result_window, text=f"{calories_burned:.2f} kcal", font=myfont, bg="#FFFFFF", fg="#291C4F")
        calories_result_label.place(x=650, y=560)

        # Calendar
        cal = Calendar(result_window, font=myfont, selectbackground="red", selectforeground="white")
        cal.place(x=750, y=100)

        for date in workout_dates:
            if date.day == 24:
                cal.calevent_create(date.year, date.month, date.day, text="Workout", background="red", disabled=True)
            else:
                cal.calevent_create(date.year, date.month, date.day, text="Workout")

        self.bind_active_calendar(cal, workout_dates)

        cal.tag_config("workout", background="red", foreground="white")

    def bind_active_calendar(self, calendar, workout_dates):
        def on_click(event):
            date = calendar.get_date()
            if datetime(date.year, date.month, date.day) in workout_dates:
                calendar.calevent_create(date.year, date.month, date.day, text="Workout", background="red", disabled=True)
            else:
                calendar.calevent_create(date.year, date.month, date.day, text="Workout")
        
        calendar.bind("<<CalendarSelected>>", on_click)

    def load_image(self, result_window):
        self.image_tk = tk.PhotoImage(file=self.image_path)
        self.canvas = tk.Canvas(result_window, width=1280, height=720)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image_tk)

if __name__ == "__main__":
    root = tk.Tk()
    app = EasyCWorkout3(root)
    root.mainloop()

