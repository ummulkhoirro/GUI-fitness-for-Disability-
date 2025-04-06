import tkinter as tk
import pygame
from tkinter import ttk
from tkVideoPlayer import TkinterVideo
import customtkinter

class VideoPlayerApp:
    def __init__(self, master):
        self.master = master
        self.master.iconbitmap("audio.ico")
        self.master.title(" ")
        self.master.geometry("400x500")
        self.master.config(bg="black")

        self.vid_player = TkinterVideo(master=self.master,bg="gray25")
        self.vid_player.pack(expand=True, fill="both")

        self.play_pause_btn = tk.Button(self.master, text="Play", command=self.play_pause)
        self.play_pause_btn.pack()

        style = ttk.Style()
        style.theme_use('default')
        style.configure("custom.Horizontal.TProgressbar", foreground="white", background="red", thickness=1.5,)

        self.progress_bar = ttk.Progressbar(self.master, orient="horizontal", mode="determinate", length=300,
                                            style="custom.Horizontal.TProgressbar")
        self.progress_bar.pack(fill="x", padx=10, pady=5)

        self.vid_player.bind("<<Duration>>", self.update_duration)
        self.vid_player.bind("<<SecondChanged>>", self.update_scale)
        self.vid_player.bind("<<Ended>>", self.video_ended)

        self.load_video()  # Load video automatically when the app starts

    def update_duration(self, event):
        """ updates the duration after finding the duration """
        duration = self.vid_player.video_info()["duration"]
        self.progress_bar.config(maximum=duration)

    def update_scale(self, event):
        """ updates the scale value """
        seconds = self.vid_player.current_duration()
        self.progress_bar["value"] = seconds

    def load_video(self):
        """ loads the video """
        file_path = "video\\vid_slowed.mp4"

        if file_path:
            # Clear the thumbnail image from the label
            self.vid_player.load(file_path)

            # Load the audio file
            audio_path = "video\\vid1.wav"
            pygame.mixer.init()
            pygame.mixer.music.load(audio_path)

            # Play video automatically after loading
            self.play_pause()  # Call play_pause method to start playing video automatically

    def play_pause(self):
        """ pauses and plays """
        if self.vid_player.is_paused():
            self.vid_player.play()
            self.play_pause_btn["text"] = "Pause"
            # Play audio here
            pygame.mixer.music.play()
        else:
            self.vid_player.pause()
            self.play_pause_btn["text"] = "Play"
            # Pause audio here
            pygame.mixer.music.pause()

    def video_ended(self, event):
        """ handle video ended """
        self.play_pause_btn["text"] = "Play"
        pygame.mixer.music.stop()

if __name__ == "__main__":
    root = customtkinter.CTk()
    app = VideoPlayerApp(root)
    root.mainloop()
