import tkinter as tk
from tkinter import ttk
import pygame
from PIL import Image,ImageTk
import customtkinter

class TextToSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio")
        self.root.config(bg="white")
        self.root.iconbitmap("audio.ico")

        def close_window(event=None):
            root.destroy()

        root.bind("<Escape>", close_window)

        play_pause_img = Image.open("images/play.png")
        play_pause_img_hover = Image.open("images/pause.png")
        play_pause_img = play_pause_img.resize((70, 50))
        play_pause_img_hover = play_pause_img_hover.resize((70, 50))
        self.play_pause_img_bg = ImageTk.PhotoImage(play_pause_img)
        self.play_pause_img_hover = ImageTk.PhotoImage(play_pause_img_hover)

        self.play_pause_button = tk.Button(root, command=self.play_pause, image=self.play_pause_img_bg,
                                           background='white', border=False,)
        self.play_pause_button.grid(row=0, column=0)

        self.progress_label = tk.Label(root, text="00:00 / 00:00", background="white",border=False)
        self.progress_label.grid(row=0, column=1,columnspan=1,pady=10)

        style = ttk.Style()
        style.theme_use('default')
        style.configure("custom.Horizontal.TProgressbar", background="red", thickness=1)

        self.progress_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate",
                                            style="custom.Horizontal.TProgressbar")
        self.progress_bar.grid(row=1, column=0, columnspan=2)

        self.paused = False
        self.playing = False
        self.paused_time = 0
        self.song_length = 0

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
            pygame.mixer.music.load("sounds/A8.mp3")
            pygame.mixer.music.play()

            song_info = pygame.mixer.Sound("sounds/A8.mp3")
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

if __name__ == "__main__":
    root = customtkinter.CTk()
    app = TextToSpeechApp(root)
    root.mainloop()
