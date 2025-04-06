import tkinter as tk
from tkinter import Canvas, Label, Button, Toplevel
from PIL import Image, ImageTk
from tkVideoPlayer import TkinterVideo
import threading
import queue
import os
import pygame
from moviepy.editor import VideoFileClip, AudioFileClip


pygame.mixer.init()

# Image loading function
def load_image(img_path):
    img = Image.open(img_path)
    return ImageTk.PhotoImage(img)

# Merge sort implementation
def merge_sort(arr, key):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L, key)
        merge_sort(R, key)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i][key] < R[j][key]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

root = tk.Tk()
root.title("FitInclusive")
root.geometry("1280x720")
root.config(bg="white")

options_fm = tk.Frame(root, bg="lightgrey")
options_fm.pack(pady=5)
options_fm.pack_propagate(False)
options_fm.configure(width=1280, height=100)

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
indicator_lbs = []
pages = []

def switch(indicator_lb, page):
    for child in options_fm.winfo_children():
        if isinstance(child, tk.Label):
            child.config(bg="lightgrey", fg="black")  # Set background and foreground color
    indicator_lb.config(bg="#0097e8", fg="white")  # Set background and foreground color

    for fm in main_fm.winfo_children():
        fm.destroy()
        root.update()

    page()

def on_enter(event):
    event.widget.config(fg="red")

def on_leave(event):
    event.widget.config(fg="black")

for i, day in enumerate(days):
    label = Label(options_fm, text=day, bg="lightgrey", fg="black", font=("Arial", 12, "bold"), padx=20, pady=10)
    label.pack(side=tk.LEFT, padx=50)
    indicator_lbs.append(label)
    label.bind("<Button-1>", lambda e, day=day: switch(label, create_page(day)))
    label.bind("<Enter>", on_enter)
    label.bind("<Leave>", on_leave)

main_fm = tk.Frame(root, bg="white")
main_fm.pack(fill=tk.BOTH, expand=True)

# Ubah lokasi file sesuai dengan kebutuhan
base_path = "D:\\pythonProject1" 

programs_dict = {
    "Monday": [
        {
            "name": "Adapted",
            "path": os.path.join(base_path, "gambar", "D:\\pythonProject1\\gambar\\adapted.png"),
            "video": os.path.join(base_path, "video", "D:\\pythonProject1\\video\\adapted.mp4"),
            "audio": os.path.join(base_path, "audio", "D:\\pythonProject1\\audio\\adapted.mp3"),
            "label": [
                "1. Warm-up like walking in place or arm swings for 1-2 minutes.",
                "2. Follow adapted exercises from the video.",
                "3. Finish with gentle stretches."
            ]
        }
    ],
    "Tuesday": [
        {
            "name": "Exercise",
            "path": os.path.join(base_path, "gambar", "D:\\pythonProject1\\gambar\\exercise.png"),
            "video": os.path.join(base_path, "video", "D:\\pythonProject1\\video\\exercise.mp4"),
            "audio": os.path.join(base_path, "audio", "D:\\pythonProject1\\audio\\exercise.mp3"),
            "label": [
                "1. Light warm-up like walking in place for 1-2 minutes.",
                "2. Follow the exercises shown in the video.",
                "3. End with gentle stretches."
            ]
        },
        {
            "name": "Adapted",
            "path": os.path.join(base_path, "gambar", "D:\\pythonProject1\\gambar\\adapted.png"),
            "video": os.path.join(base_path, "video", "D:\\pythonProject1\\video\\adapted.mp4"),
            "audio": os.path.join(base_path, "audio", "D:\\pythonProject1\\audio\\adapted.mp3"),
            "label": [
                "1. Warm-up like walking in place or arm swings for 1-2 minutes.",
                "2. Follow adapted exercises from the video.",
                "3. Finish with gentle stretches."
            ]
        }
    ],
    "Wednesday": [
        {
            "name": "Exercise",
            "path": os.path.join(base_path, "gambar", "D:\\pythonProject1\\gambar\\exercise.png"),
            "video": os.path.join(base_path, "video", "D:\\pythonProject1\\video\\exercise.mp4"),
            "audio": os.path.join(base_path, "audio", "D:\\pythonProject1\\audio\\exercise.mp3"),
            "label": [
                "1. Light warm-up like walking in place for 1-2 minutes.",
                "2. Follow the exercises shown in the video.",
                "3. End with gentle stretches."
            ]
        }
    ],
    "Thursday": [
        {
            "name": "Adapted",
            "path": os.path.join(base_path, "gambar", "D:\\pythonProject1\\gambar\\adapted.png"),
            "video": os.path.join(base_path, "video", "D:\\pythonProject1\\video\\adapted.mp4"),
            "audio": os.path.join(base_path, "audio", "D:\\pythonProject1\\audio\\adapted.mp3"),
            "label": [
                "1. Warm-up like walking in place or arm swings for 1-2 minutes.",
                "2. Follow adapted exercises from the video.",
                "3. Finish with gentle stretches."
            ]
        },
        {
            "name": "Exercise",
            "path": os.path.join(base_path, "gambar", "D:\\pythonProject1\\gambar\\exercise.png"),
            "video": os.path.join(base_path, "video", "D:\\pythonProject1\\video\\exercise.mp4"),
            "audio": os.path.join(base_path, "audio", "D:\\pythonProject1\\audio\\exercise.mp3"),
            "label": [
                "1. Light warm-up like walking in place for 1-2 minutes.",
                "2. Follow the exercises shown in the video.",
                "3. End with gentle stretches."
            ]
        }
    ],

    "Friday": [
    {
        "name": "Adapted",
            "path": os.path.join(base_path, "gambar", "D:\\pythonProject1\\gambar\\adapted.png"),
            "video": os.path.join(base_path, "video", "D:\\pythonProject1\\video\\adapted.mp4"),
            "audio": os.path.join(base_path, "audio", "D:\\pythonProject1\\audio\\adapted.mp3"),
            "label": [
                "1. Warm-up like walking in place or arm swings for 1-2 minutes.",
                "2. Follow adapted exercises from the video.",
                "3. Finish with gentle stretches."
        ]
    }
],

    "Saturday": [
        {
            "name": "Exercise",
            "path": os.path.join(base_path, "gambar", "D:\\pythonProject1\\gambar\\exercise.png"),
            "video": os.path.join(base_path, "video", "D:\\pythonProject1\\video\\exercise.mp4"),
            "audio": os.path.join(base_path, "audio", "D:\\pythonProject1\\audio\\exercise.mp3"),
            "label": [
                "1. Light warm-up like walking in place for 1-2 minutes.",
                "2. Follow the exercises shown in the video.",
                "3. End with gentle stretches."
            ]
        },
    ],
    "Sunday": [
        {
            "name": "Adapted",
            "path": os.path.join(base_path, "gambar", "D:\\pythonProject1\\gambar\\adapted.png"),
            "video": os.path.join(base_path, "video", "D:\\pythonProject1\\video\\adapted.mp4"),
            "audio": os.path.join(base_path, "audio", "D:\\pythonProject1\\audio\\adapted.mp3"),
            "label": [
                "1. Warm-up like walking in place or arm swings for 1-2 minutes.",
                "2. Follow adapted exercises from the video.",
                "3. Finish with gentle stretches."
            ]
        }
    ]
}


def create_page(day):
    def page():
        for fm in main_fm.winfo_children():
            fm.destroy()
            root.update()

        page_fm = tk.Frame(main_fm, bg="white")
        page_fm.pack(fill=tk.BOTH, expand=True)
        canvas = Canvas(page_fm, width=820, height=820, bg="white", highlightthickness=0)
        canvas.pack()

        if day in programs_dict:
            programs = programs_dict[day]

            def open_program(program):
                if "video" in program:
                    video_window = Toplevel(root)
                    video_window.title(program["name"])
                    video_window.geometry("1280x720")
                    video_window.config(bg="lightgrey")

                    video_player = TkinterVideo(video_window, scaled=True)
                    video_player.load(program["video"])
                    video_player.pack(expand=True, fill="both")
                    video_player.play()

                    # Load and play audio
                    pygame.mixer.music.load(program["audio"])
                    pygame.mixer.music.play()

                    for i, tts_text in enumerate(program["label"]):
                        label = Label(video_window, text=tts_text, font=("Poppins", 12, "bold", "italic"), bg="lightgrey", fg="#000000")
                        label.pack(pady=(10, 0))

                    back_button = Button(video_window, text="\u2190", font=("Arial", 14), command=video_window.destroy)
                    back_button.place(x=20, y=20)
                else:
                    program_window = Toplevel(root)
                    program_window.title(program["name"])
                    program_window.geometry("640x480")
                    program_window.config(bg="lightgrey")

                                # Load and play audio
                    pygame.mixer.music.load(program["audio"])
                    pygame.mixer.music.play()

                    while pygame.mixer.music.get_busy():
                        pygame.time.wait(100)

                    for i, tts_text in enumerate(program["label"]):
                        label = Label(program_window, text=tts_text, font=("Poppins", 12, "bold", "italic"), bg="lightgrey", fg="#000000")
                        label.pack(pady=(10, 0))

                    back_button = Button(program_window, text="\u2190", font=("Arial", 14), command=program_window.destroy)
                    back_button.place(x=20, y=20)

            for i, program in enumerate(programs):
                program_name = program["name"]
                program_image = load_image(program["path"])
                btn = Button(page_fm, image=program_image, borderwidth=0, width=710, height=150, command=lambda p=program: open_program(p))
                btn.image = program_image
                btn.place(x=250, y=60 + i * 160)

        page_fm.pack(fill=tk.BOTH, expand=True)

    return page

pages = [create_page(day) for day in days]

def switch(label, page):
    for lb in indicator_lbs:
        lb.config(bg="lightgrey", fg="black")
    label.config(bg="#0097e8", fg="white")
    for fm in main_fm.winfo_children():
        fm.destroy()
    page()

for i, page in enumerate(pages):
    indicator_lbs[i].bind("<Button-1>", lambda e, page=page, lb=indicator_lbs[i]: switch(lb, page))

pages[0]()

root.mainloop()