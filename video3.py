import tkinter as tk
from PIL import Image, ImageTk
import pygame
from tkinter import ttk
import customtkinter

class AudioPlayerApp:
    def __init__(self, root):
        self.root = root
        self.playing = False
        self.root.title(" ")
        self.root.config(bg="black")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        height = 720
        width = 1280
        x = (root.winfo_screenwidth() // 2) - (width // 2)
        y = (root.winfo_screenheight() // 4) - (height // 4)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.root.config(bg="white")
        self.root.attributes("-fullscreen", True)
        self.root.bind("<Escape>", self.toggle_fullscreen)
        self.root.bind("<Double-Button-1>", self.toggle_fullscreen)

        self.vid1bg = ImageTk.PhotoImage(Image.open("images/vid3bg.png").resize((root.winfo_screenwidth(),root.winfo_screenheight())))
        self.canva1 = tk.Canvas(self.root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(),
                             bg="black", highlightthickness=0, borderwidth=0)
        self.canva1.place(x=0, y=0)
        self.canva1.create_image(0, 0, anchor='nw', image=self.vid1bg)

        play_pause_img = Image.open("images/play.png")
        play_pause_img_hover = Image.open("images/pause1.png")
        play_pause_img = play_pause_img.resize((150, 100))
        play_pause_img_hover = play_pause_img_hover.resize((150, 100))
        self.play_pause_img_bg = ImageTk.PhotoImage(play_pause_img)
        self.play_pause_img_hover = ImageTk.PhotoImage(play_pause_img_hover)

        self.play_pause_button = tk.Button(root, command=self.play_pause, image=self.play_pause_img_bg,
                                           background='black', border=False,fg='black' ,activebackground="black")
        self.play_pause_button.place(x=625, y=573)

        self.progress_label = tk.Label(root, text="00:00 / 00:00", background="black", border=False,fg="white")
        self.progress_label.place(x=1068, y= 645)

        style = ttk.Style()
        style.theme_use('default')
        style.configure("custom.Horizontal.TProgressbar", foreground="white", background="green", thickness=1.5, )

        self.progress_bar = ttk.Progressbar(root, orient="horizontal", length=900, mode="determinate",
                                            style="custom.Horizontal.TProgressbar")
        self.progress_bar.place(x=230, y=677)

        self.paused = False
        self.playing = False
        self.paused_time = 0
        self.song_length = 0

    def toggle_fullscreen(self, event=None):
        is_fullscreen = self.root.attributes("-fullscreen")
        self.root.attributes("-fullscreen", not is_fullscreen)


    def play_pause(self):
        if not self.playing:
            self.play()
        elif self.paused:
            self.resume()
        else:
            self.pause()

    def play(self):
        if not self.playing:
            pygame.mixer.init()
            pygame.mixer.music.load("sounds/vid3.mp3")
            pygame.mixer.music.play()

            song_info = pygame.mixer.Sound("sounds/vid3.mp3")
            self.song_length = song_info.get_length()

            # Update progress bar and labels
            self.update_progress_bar()

            self.playing = True
            self.paused = False
            self.play_pause_button.config(image=self.play_pause_img_hover)

    def pause(self):
        if self.playing and not self.paused:
            pygame.mixer.music.pause()
            self.paused = True
            self.paused_time = pygame.mixer.music.get_pos() / 1000

            self.play_pause_button.config(image=self.play_pause_img_bg)

    def resume(self):
        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False

            self.update_progress_bar()

            self.play_pause_button.config(image=self.play_pause_img_hover)

    def update_progress_bar(self):
        if pygame.mixer.music.get_busy() and not self.paused:
            current_time = pygame.mixer.music.get_pos() / 1000
            progress = (current_time / self.song_length) * 100
            self.progress_bar["value"] = progress

            current_time_str = self.format_time(current_time)
            song_length_str = self.format_time(self.song_length)
            self.progress_label.config(text=f"{current_time_str} / {song_length_str}")

            self.root.after(100, self.update_progress_bar)  # Update every 100ms
        elif self.paused:
            self.progress_bar["value"] = (self.paused_time / self.song_length) * 100

            current_time_str = self.format_time(self.paused_time)
            song_length_str = self.format_time(self.song_length)
            self.progress_label.config(text=f"{current_time_str} / {song_length_str}")

    def format_time(self, seconds):
        minutes = int(seconds // 60)
        seconds = int(seconds % 60)
        return f"{minutes:02}:{seconds:02}"

    # def toggle_play_pause(self):
    #     if self.playing:  # Jika sedang diputar, maka jeda
    #         pygame.mixer.music.pause()
    #         self.play_pause_btn.config(image=self.play_img_bg)  # Mengganti gambar tombol ke play
    #     else:  # Jika sedang dijeda, maka mainkan
    #         pygame.mixer.music.unpause()
    #         self.play_pause_btn.config(image=self.pause_bg)  # Mengganti gambar tombol ke pause
    #     self.playing = not self.playing
    #
    # def loadaudio(self):
    #     audio_path = "sounds\\vid1.m4a"
    #     pygame.mixer.init()
    #     pygame.mixer.music.load(audio_path)

if __name__ == "__main__":
    root = customtkinter.CTk()
    app = AudioPlayerApp(root)
    root.mainloop()
