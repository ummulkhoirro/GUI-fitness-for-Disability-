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
            "name": "Chair Yoga",
            "path": os.path.join(base_path, "gambar", "D:\\pythonProject1\\gambar\\yoga.png"),
            "video": os.path.join(base_path, "video", "D:\\pythonProject1\\video\\yoga.mp4"),
            "audio": os.path.join(base_path, "audio", "D:\\pythonProject1\\audio\\yoga.mp3"),
            "label": [
                "1. Sit comfortably on a chair with your feet flat on the ground.",
                "2. Follow the instructor's cues to perform gentle yoga poses adapted for seated practice.",
                "3. Focus on deep breathing and relaxation to calm the mind and body."
            ]
        },
        {
            "name": "Seated Pilates",
            "path": os.path.join(base_path, "gambar", "D:\\pythonProject1\\gambar\\seated.png"),
            "video": os.path.join(base_path, "video", "D:\\pythonProject1\\video\\seated.mp4"),
            "audio": os.path.join(base_path, "audio", "D:\\pythonProject1\\audio\\seated.mp3"),
            "label": [
                "1. Sit upright on a chair with your back supported and engage your core muscles.",
                "2. Follow the instructor's cues to perform pilates exercises modified for seated position.",
                "3. Focus on maintaining proper alignment and controlled movements throughout the session."
            ]
        },
        {
            "name": "Chair Cardio",
            "path": os.path.join(base_path, "gambar", "D:\\pythonProject1\\gambar\\cardio.png"),
            "video": os.path.join(base_path, "video", "D:\\pythonProject1\\video\\cardio.mp4"),
            "audio": os.path.join(base_path, "audio", "D:\\pythonProject1\\audio\\cardio.mp3"),
            "label": [
                "1. Get your heart pumping with this seated cardio workout.",
                "2. Follow the instructor's energetic movements to elevate your heart rate while staying seated.",
                "3. Have fun and enjoy the benefits of cardio exercise from the comfort of your chair!"
            ]
        }
    ],
    "Tuesday": [
        {
            "name": "Chair Zumba",
            "path": os.path.join(base_path, "gambar", "D:\\pythonProject1\\gambar\\zumba.png"),
            "video": os.path.join(base_path, "video", "D:\\pythonProject1\\video\\zumba.mp4"),
            "audio": os.path.join(base_path, "audio", "D:\\pythonProject1\\audio\\zumba.mp3"),
            "label": [
                "1. Get ready to dance and groove with this seated Zumba workout.",
                "2. Follow the instructor's lively choreography to the rhythm of Latin music.",
                "3. Enjoy a fun and effective cardio session while sitting in your chair!"
            ]
        },
        {
            "name": "Chair Tai Chi",
            "path": os.path.join(base_path, "gambar", "D:\\pythonProject1\\gambar\\tai chi.png"),
            "video": os.path.join(base_path, "video", "D:\\pythonProject1\\video\\tai chi.mp4"),
            "audio": os.path.join(base_path, "audio", "D:\\pythonProject1\\audio\\tai chi.mp3"),
            "label": [
                "1. Experience the flow of Tai Chi movements adapted for seated practice.",
                "2. Follow the instructor's gentle movements to promote relaxation and balance.",
                "3. Focus on the breath and the fluidity of movement to cultivate mindfulness."
            ]
        },
        {
            "name": "Chair Stretching",
            "path": os.path.join(base_path, "gambar", "D:\\pythonProject1\\gambar\\stretching.png"),
            "video": os.path.join(base_path, "video", "D:\\pythonProject1\\video\\stretching.mp4"),
            "audio": os.path.join(base_path, "audio", "D:\\pythonProject1\\audio\\stretching.mp3"),
            "label": [
                "1. Loosen up tight muscles and improve flexibility with this seated stretching routine.",
                "2. Follow the instructor's cues to gently stretch your entire body while sitting comfortably.",
                "3. Focus on deep breathing and relaxation to release tension and improve mobility."
            ]
        }
    ],
    "Wednesday": [
        {
            "name": "Chair Aerobics",
            "path": os.path.join(base_path, "gambar", "D:\\pythonProject1\\gambar\\aero.png"),
            "video": os.path.join(base_path, "video", "D:\\pythonProject1\\video\\aerobics.mp4"),
            "audio": os.path.join(base_path, "audio", "D:\\pythonProject1\\audio\\aerobics.mp3"),
            "label": [
                "1. Elevate your heart rate and burn calories with this seated aerobics workout.",
                "2. Follow the instructor's dynamic movements to strengthen your cardiovascular system.",
                "3. Have fun and stay active while seated in your chair!"
            ]
        },
        {
            "name": "Chair Strength Training",
            "path": os.path.join(base_path, "gambar", "D:\\pythonProject1\\gambar\\strength.png"),
            "video": os.path.join(base_path, "video", "D:\\pythonProject1\\video\\Strength.mp4"),
            "audio": os.path.join(base_path, "audio", "D:\\pythonProject1\\audio\\Strength.mp3"),
            "label": [
                "1. Build muscle and improve strength with this seated strength training routine.",
                "2. Follow the instructor's cues to target different muscle groups using resistance bands or weights.",
                "3. Focus on proper form and controlled movements for maximum effectiveness."
            ]
        },
        {
            "name": "Chair Dance Fitness",
            "path": os.path.join(base_path, "gambar", "D:\\pythonProject1\\gambar\\dance.png"),
            "video": os.path.join(base_path, "video", "D:\\pythonProject1\\video\\dance.mp4"),
            "audio": os.path.join(base_path, "audio", "D:\\pythonProject1\\audio\\dance.mp3"),
            "label": [
                "1. Get your groove on and burn calories with this seated dance fitness workout.",
                "2. Follow the instructor's fun choreography to the beat of energetic music.",
                "3. Enjoy a full-body workout while seated in your chair!"
            ]
        }
    ],
    "Thursday": [
        {
            "name": "Chair Dance Fitness",
            "path": os.path.join(base_path, "gambar", "D:\\pythonProject1\\gambar\\dance.png"),
            "video": os.path.join(base_path, "video", "D:\\pythonProject1\\video\\dance.mp4"),
            "audio": os.path.join(base_path, "audio", "D:\\pythonProject1\\audio\\dance.mp3"),
            "label": [
                "1. Get your groove on and burn calories with this seated dance fitness workout.",
                "2. Follow the instructor's fun choreography to the beat of energetic music.",
                "3. Enjoy a full-body workout while seated in your chair!"
            ]
        },
        {
            "name": "Chair Stretching",
            "path": os.path.join(base_path, "gambar", "D:\\pythonProject1\\gambar\\stretching.png"),
            "video": os.path.join(base_path, "video", "D:\\pythonProject1\\video\\stretching.mp4"),
            "audio": os.path.join(base_path, "audio", "D:\\pythonProject1\\audio\\stretching.mp3"),
            "label": [
                "1. Loosen up tight muscles and improve flexibility with this seated stretching routine.",
                "2. Follow the instructor's cues to gently stretch your entire body while sitting comfortably.",
                "3. Focus on deep breathing and relaxation to release tension and improve mobility."
            ]
        },
        {
            "name": "Chair Zumba",
            "path": os.path.join(base_path, "gambar", "D:\\pythonProject1\\gambar\\zumba.png"),
            "video": os.path.join(base_path, "video", "D:\\pythonProject1\\video\\zumba.mp4"),
            "audio": os.path.join(base_path, "audio", "D:\\pythonProject1\\audio\\zumba.mp3"),
            "label": [
                "1. Get ready to dance and groove with this seated Zumba workout.",
                "2. Follow the instructor's lively choreography to the rhythm of Latin music.",
                "3. Enjoy a fun and effective cardio session while sitting in your chair!"
            ]
        }
    ],

    "Friday": [
    {
        "name": "Seated Pilates",
        "path": os.path.join(base_path, "gambar", "D:\\pythonProject1\\gambar\\seated.png"),
        "video": os.path.join(base_path, "video", "D:\\pythonProject1\\video\\seated.mp4"),
        "audio": os.path.join(base_path, "audio", "D:\\pythonProject1\\audio\\seated.mp3"),
        "label": [
            "1. Sit upright on a chair with your back supported and engage your core muscles.",
            "2. Follow the instructor's cues to perform pilates exercises modified for seated position.",
            "3. Focus on maintaining proper alignment and controlled movements throughout the session."
        ]
    },
    {
        "name": "Chair Balance Exercises",
        "path": os.path.join(base_path, "gambar", "D:\\pythonProject1\\gambar\\balance.png"),
        "video": os.path.join(base_path, "video", "D:\\pythonProject1\\video\\balance.mp4"),
        "audio": os.path.join(base_path, "audio", "D:\\pythonProject1\\audio\\balance.mp3"),
        "label": [
            "1. Improve your balance and stability with this seated balance exercise routine.",
            "2. Follow the instructor's cues to engage your core muscles and focus on maintaining equilibrium.",
            "3. Enhance your overall mobility and reduce the risk of falls with regular practice."
        ]
    },
    {
        "name": "Chair Yoga",
        "path": os.path.join(base_path, "gambar", "D:\\pythonProject1\\gambar\\yoga.png"),
        "video": os.path.join(base_path, "video", "D:\\pythonProject1\\video\\yoga.mp4"),
        "audio": os.path.join(base_path, "audio", "D:\\pythonProject1\\audio\\yoga.mp3"),
        "label": [
            "1. Sit comfortably on a chair with your feet flat on the ground.",
            "2. Follow the instructor's cues to perform gentle yoga poses adapted for seated practice.",
            "3. Focus on deep breathing and relaxation to calm the mind and body."
        ]
    }
],

    "Saturday": [
        {
            "name": "Chair Balance Exercises",
            "path": os.path.join(base_path, "gambar", "D:\\pythonProject1\\gambar\\balance.png"),
            "video": os.path.join(base_path, "video", "D:\\pythonProject1\\video\\balance.mp4"),
            "audio": os.path.join(base_path, "audio", "D:\\pythonProject1\\audio\\balance.mp3"),
            "label": [
                "1. Improve your balance and stability with this seated balance exercise routine.",
                "2. Follow the instructor's cues to engage your core muscles and focus on maintaining equilibrium.",
                "3. Enhance your overall mobility and reduce the risk of falls with regular practice."
            ]
        },
        {
            "name": "Chair Tai Chi",
            "path": os.path.join(base_path, "gambar", "D:\\pythonProject1\\gambar\\tai chi.png"),
            "video": os.path.join(base_path, "video", "D:\\pythonProject1\\video\\tai chi.mp4"),
            "audio": os.path.join(base_path, "audio", "D:\\pythonProject1\\audio\\tai chi.mp3"),
            "label": [
                "1. Experience the flow of Tai Chi movements adapted for seated practice.",
                "2. Follow the instructor's gentle movements to promote relaxation and balance.",
                "3. Focus on the breath and the fluidity of movement to cultivate mindfulness."
            ]
        },
        {
            "name": "Chair Stretching",
            "path": os.path.join(base_path, "gambar", "D:\\pythonProject1\\gambar\\stretching.png"),
            "video": os.path.join(base_path, "video", "D:\\pythonProject1\\video\\stretching.mp4"),
            "audio": os.path.join(base_path, "audio", "D:\\pythonProject1\\audio\\stretching.mp3"),
            "label": [
                "1. Loosen up tight muscles and improve flexibility with this seated stretching routine.",
                "2. Follow the instructor's cues to gently stretch your entire body while sitting comfortably.",
                "3. Focus on deep breathing and relaxation to release tension and improve mobility."
            ]
        }
    ],
    "Sunday": [
        {
            "name": "Chair Tai Chi",
            "path": os.path.join(base_path, "gambar", "D:\\pythonProject1\\gambar\\tai chi.png"),
            "video": os.path.join(base_path, "video", "D:\\pythonProject1\\video\\tai chi.mp4"),
            "audio": os.path.join(base_path, "audio", "D:\\pythonProject1\\audio\\tai chi.mp3"),
            "label": [
                "1. Experience the flow of Tai Chi movements adapted for seated practice.",
                "2. Follow the instructor's gentle movements to promote relaxation and balance.",
                "3. Focus on the breath and the fluidity of movement to cultivate mindfulness."
            ]
        },
        {
            "name": "Chair Dance Fitness",
            "path": os.path.join(base_path, "gambar", "D:\\pythonProject1\\gambar\\dance.png"),
            "video": os.path.join(base_path, "video", "D:\\pythonProject1\\video\\dance.mp4"),
            "audio": os.path.join(base_path, "audio", "D:\\pythonProject1\\audio\\dance.mp3"),
            "label": [
                "1. Get your groove on and burn calories with this seated dance fitness workout.",
                "2. Follow the instructor's fun choreography to the beat of energetic music.",
                "3. Enjoy a full-body workout while seated in your chair!"
            ]
        },
        {
            "name": "Chair Balance Exercises",
            "path": os.path.join(base_path, "gambar", "D:\\pythonProject1\\gambar\\balance.png"),
            "video": os.path.join(base_path, "video", "D:\\pythonProject1\\video\\balance.mp4"),
            "audio": os.path.join(base_path, "audio", "D:\\pythonProject1\\audio\\balance.mp3"),
            "label": [
                "1. Improve your balance and stability with this seated balance exercise routine.",
                "2. Follow the instructor's cues to engage your core muscles and focus on maintaining equilibrium.",
                "3. Enhance your overall mobility and reduce the risk of falls with regular practice."
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