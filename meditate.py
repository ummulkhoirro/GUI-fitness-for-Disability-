import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import customtkinter as ctk
import pygame
import video1
import video2
import video3
import video4
import video5
import video6
import video7
import video8
import video9

class Meditation:
    def __init__(self, meditasi):
        self.meditasi = meditasi
        self.meditasi.rowconfigure(0, weight=1)
        self.meditasi.columnconfigure(0, weight=1)
        height = 720
        width = 1280
        x = (meditasi.winfo_screenwidth() // 2) - (width // 2)
        y = (meditasi.winfo_screenheight() // 4) - (height // 4)
        self.meditasi.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.meditasi.config(bg="white")
        self.meditasi.attributes("-fullscreen", True)
        self.meditasi.bind("<Escape>", self.toggle_fullscreen)
        self.meditasi.bind("<Double-Button-1>", self.toggle_fullscreen)



        self.home = tk.Frame(self.meditasi)
        self.meditate = tk.Frame(self.meditasi)
        self.music = tk.Frame(self.meditasi)
        self.motiv = tk.Frame(self.meditasi)
        self.queueframe = tk.Frame(self.meditasi)

        for frame in (self.meditate, self.music, self.motiv, ):
            frame.grid(row=0, column=0, sticky='nsew')

        self.create_meditate_buttons()
        self.showmed()

        self.img2 = Image.open("images/homemed.png")
        self.img2 = self.img2.resize((meditasi.winfo_screenwidth(), meditasi.winfo_screenheight()))
        self.foto1 = ImageTk.PhotoImage(self.img2)
        self.canva1 = tk.Canvas(self.home, width=meditasi.winfo_screenwidth(), height=meditasi.winfo_screenheight(),
                                bg="black", highlightthickness=0, borderwidth=0)
        self.canva1.place(x=0, y=0)
        self.canva1.create_image(0, 0, anchor='nw', image=self.foto1)

        # home_image = ctk.CTkImage(Image.open("images/home.png"), size=(100, 70))
        # home_button = ctk.CTkButton(self.home, image=home_image, width=100, height=60, text="", bg_color="black",
        #                             fg_color="black", border_color="black", border_width=0, hover=False,
        #                             command=self.showhome)
        # home_button.place(x=200, y=675)
        #
        # med_image = ctk.CTkImage(Image.open("images/med1.png"), size=(120, 80))
        # med_button = ctk.CTkButton(self.home, image=med_image, width=100, height=60, text="", bg_color="black",
        #                            fg_color="black", border_color="black", border_width=0, hover=False,
        #                            command=self.showmed)
        # med_button.place(x=450, y=675)
        #
        # music_image = ctk.CTkImage(Image.open("images/headphonemed.png"), size=(120, 80))
        # music_button = ctk.CTkButton(self.home, image=music_image, width=100, height=60, text="", bg_color="black",
        #                              fg_color="black", border_color="black", border_width=0, hover=False,
        #                              command=self.showmusic)
        # music_button.place(x=700, y=675)
        #
        # motiv_image = ctk.CTkImage(Image.open("images/motiv.png"), size=(120, 80))
        # motiv_button = ctk.CTkButton(self.home, image=motiv_image, width=100, height=60, text="", bg_color="black",
        #                              fg_color="black", border_color="black", border_width=0, hover=False,
        #                              command=self.showmotiv)
        # motiv_button.place(x=950, y=675)
        #
        # qiu_image = ctk.CTkImage(Image.open("images/queue.png"), size=(120, 80))
        # qiu_button = ctk.CTkButton(self.home, image=qiu_image, width=100, height=60, text="", bg_color="black",
        #                            fg_color="black", border_color="black", border_width=0, hover=False,
        #                            command=self.showqueue)
        # qiu_button.place(x=1200, y=680)


        #======================================================================

        self.img3 = Image.open("images/framebg.png")
        self.img3 = self.img3.resize((meditasi.winfo_screenwidth(), meditasi.winfo_screenheight()))
        self.foto2 = ImageTk.PhotoImage(self.img3)
        self.canva2 = tk.Canvas(self.meditate, width=meditasi.winfo_screenwidth(), height=meditasi.winfo_screenheight(),
                                bg="black", highlightthickness=0, borderwidth=0)
        self.canva2.place(x=0, y=0)
        self.canva2.create_image(0, 0, anchor='nw', image=self.foto2)

        home_image = ctk.CTkImage(Image.open("images/home.png"), size=(100, 70))
        home_button = ctk.CTkButton(self.meditate, image=home_image, width=100, height=60, text="", bg_color="black",
                                    fg_color="black", border_color="black", border_width=0, hover=False,
                                    command=self.showhome)
        home_button.place(x=200, y=675)

        med_image = ctk.CTkImage(Image.open("images/med1.png"), size=(120, 80))
        med_button = ctk.CTkButton(self.meditate, image=med_image, width=100, height=60, text="", bg_color="black",
                                   fg_color="black", border_color="black", border_width=0, hover=False,
                                   command=self.showmed)
        med_button.place(x=450, y=675)

        music_image = ctk.CTkImage(Image.open("images/headphonemed.png"), size=(120, 80))
        music_button = ctk.CTkButton(self.meditate, image=music_image, width=100, height=60, text="", bg_color="black",
                                     fg_color="black", border_color="black", border_width=0, hover=False,
                                     command=self.showmusic)
        music_button.place(x=700, y=675)

        motiv_image = ctk.CTkImage(Image.open("images/motiv.png"), size=(120, 80))
        motiv_button = ctk.CTkButton(self.meditate, image=motiv_image, width=100, height=60, text="", bg_color="black",
                                     fg_color="black", border_color="black", border_width=0, hover=False,
                                     command=self.showmotiv)
        motiv_button.place(x=950, y=675)

        qiu_image = ctk.CTkImage(Image.open("images/queue.png"), size=(120, 80))
        qiu_button = ctk.CTkButton(self.meditate, image=qiu_image, width=100, height=60, text="", bg_color="black",
                                   fg_color="black", border_color="black", border_width=0, hover=False,
                                   command=self.showqueue)
        qiu_button.place(x=1200, y=680)

        self.img4 = Image.open("images/framebg.png")
        self.img4 = self.img4.resize((meditasi.winfo_screenwidth(), meditasi.winfo_screenheight()))
        self.foto3 = ImageTk.PhotoImage(self.img4)
        self.canva3 = tk.Canvas(self.music, width=meditasi.winfo_screenwidth(), height=meditasi.winfo_screenheight(),
                                bg="black", highlightthickness=0, borderwidth=0)
        self.canva3.place(x=0, y=0)
        self.canva3.create_image(0, 0, anchor='nw', image=self.foto3)

        home_image = ctk.CTkImage(Image.open("images/home.png"), size=(100, 70))
        home_button = ctk.CTkButton(self.music, image=home_image, width=100, height=60, text="", bg_color="black",
                                    fg_color="black", border_color="black", border_width=0, hover=False,
                                    command=self.showhome)
        home_button.place(x=200, y=675)

        med_image = ctk.CTkImage(Image.open("images/med1.png"), size=(120, 80))
        med_button = ctk.CTkButton(self.music, image=med_image, width=100, height=60, text="", bg_color="black",
                                   fg_color="black", border_color="black", border_width=0, hover=False,
                                   command=self.showmed)
        med_button.place(x=450, y=675)

        music_image = ctk.CTkImage(Image.open("images/headphonemed.png"), size=(120, 80))
        music_button = ctk.CTkButton(self.music, image=music_image, width=100, height=60, text="", bg_color="black",
                                     fg_color="black", border_color="black", border_width=0, hover=False,
                                     command=self.showmusic)
        music_button.place(x=700, y=675)

        motiv_image = ctk.CTkImage(Image.open("images/motiv.png"), size=(120, 80))
        motiv_button = ctk.CTkButton(self.music, image=motiv_image, width=100, height=60, text="", bg_color="black",
                                     fg_color="black", border_color="black", border_width=0, hover=False,
                                     command=self.showmotiv)
        motiv_button.place(x=950, y=675)

        qiu_image = ctk.CTkImage(Image.open("images/queue.png"), size=(120, 80))
        qiu_button = ctk.CTkButton(self.music, image=qiu_image, width=100, height=60, text="", bg_color="black",
                                   fg_color="black", border_color="black", border_width=0, hover=False,
                                   command=self.showqueue)
        qiu_button.place(x=1200, y=680)

        self.img5 = Image.open("images/framebg.png")
        self.img5 = self.img5.resize((meditasi.winfo_screenwidth(), meditasi.winfo_screenheight()))
        self.foto4 = ImageTk.PhotoImage(self.img5)
        self.canva4 = tk.Canvas(self.motiv, width=meditasi.winfo_screenwidth(), height=meditasi.winfo_screenheight(),
                                bg="black", highlightthickness=0, borderwidth=0)
        self.canva4.place(x=0, y=0)
        self.canva4.create_image(0, 0, anchor='nw', image=self.foto4)

        home_image = ctk.CTkImage(Image.open("images/home.png"), size=(100, 70))
        home_button = ctk.CTkButton(self.motiv, image=home_image, width=100, height=60, text="", bg_color="black",
                                    fg_color="black", border_color="black", border_width=0, hover=False,
                                    command=self.showhome)
        home_button.place(x=200, y=675)

        med_image = ctk.CTkImage(Image.open("images/med1.png"), size=(120, 80))
        med_button = ctk.CTkButton(self.motiv, image=med_image, width=100, height=60, text="", bg_color="black",
                                   fg_color="black", border_color="black", border_width=0, hover=False,
                                   command=self.showmed)
        med_button.place(x=450, y=675)

        music_image = ctk.CTkImage(Image.open("images/headphonemed.png"), size=(120, 80))
        music_button = ctk.CTkButton(self.motiv, image=music_image, width=100, height=60, text="", bg_color="black",
                                     fg_color="black", border_color="black", border_width=0, hover=False,
                                     command=self.showmusic)
        music_button.place(x=700, y=675)

        motiv_image = ctk.CTkImage(Image.open("images/motiv.png"), size=(120, 80))
        motiv_button = ctk.CTkButton(self.motiv, image=motiv_image, width=100, height=60, text="", bg_color="black",
                                     fg_color="black", border_color="black", border_width=0, hover=False,
                                     command=self.showmotiv)
        motiv_button.place(x=950, y=675)

        qiu_image = ctk.CTkImage(Image.open("images/queue.png"), size=(120, 80))
        qiu_button = ctk.CTkButton(self.motiv, image=qiu_image, width=100, height=60, text="", bg_color="black",
                                   fg_color="black", border_color="black", border_width=0, hover=False,
                                   command=self.showqueue)
        qiu_button.place(x=1200, y=680)

        self.img6 = Image.open("images/framebg.png")
        self.img6 = self.img6.resize((meditasi.winfo_screenwidth(), meditasi.winfo_screenheight()))
        self.foto5 = ImageTk.PhotoImage(self.img6)
        self.canva5 = tk.Canvas(self.queueframe, width=meditasi.winfo_screenwidth(), height=meditasi.winfo_screenheight(),
                                bg="black", highlightthickness=0, borderwidth=0)
        self.canva5.place(x=0, y=0)
        self.canva5.create_image(0, 0, anchor='nw', image=self.foto5)

        home_image = ctk.CTkImage(Image.open("images/home.png"), size=(100, 70))
        home_button = ctk.CTkButton(self.queueframe, image=home_image, width=100, height=60, text="", bg_color="black",
                                    fg_color="black", border_color="black", border_width=0, hover=False,
                                    command=self.showhome)
        home_button.place(x=200, y=675)

        med_image = ctk.CTkImage(Image.open("images/med1.png"), size=(120, 80))
        med_button = ctk.CTkButton(self.queueframe, image=med_image, width=100, height=60, text="", bg_color="black",
                                   fg_color="black", border_color="black", border_width=0, hover=False,
                                   command=self.showmed)
        med_button.place(x=450, y=675)

        music_image = ctk.CTkImage(Image.open("images/headphonemed.png"), size=(120, 80))
        music_button = ctk.CTkButton(self.queueframe, image=music_image, width=100, height=60, text="", bg_color="black",
                                     fg_color="black", border_color="black", border_width=0, hover=False,
                                     command=self.showmusic)
        music_button.place(x=700, y=675)

        motiv_image = ctk.CTkImage(Image.open("images/motiv.png"), size=(120, 80))
        motiv_button = ctk.CTkButton(self.queueframe, image=motiv_image, width=100, height=60, text="", bg_color="black",
                                     fg_color="black", border_color="black", border_width=0, hover=False,
                                     command=self.showmotiv)
        motiv_button.place(x=950, y=675)

        qiu_image = ctk.CTkImage(Image.open("images/queue.png"), size=(120, 80))
        qiu_button = ctk.CTkButton(self.queueframe, image=qiu_image, width=100, height=60, text="", bg_color="black",
                                   fg_color="black", border_color="black", border_width=0, hover=False,
                                   command=self.showqueue)
        qiu_button.place(x=1200, y=680)

    def create_meditate_buttons(self):
        self.medvideos = {
            "vid (1)": video1.AudioPlayerApp,
            "vid (2)": video2.AudioPlayerApp,
            "vid (3)": video3.AudioPlayerApp,
        }
        self.meditate.rowconfigure(0, weight=1)
        for index, (key, video_class) in enumerate(self.medvideos.items()):
            self.meditate.columnconfigure(index, weight=3, uniform="videos")  # Adjust column configuration
            video_image = ImageTk.PhotoImage(Image.open(f"images/{key}.png").resize((450, 350)))
            button = tk.Button(self.meditate, image=video_image, text="", bg="black",
                                   fg="black",
                                   command=lambda v_class=video_class: v_class(self.meditasi),)
            button.grid(row=0, column=index, padx=(5, 5), pady=10)
            button.image = video_image

    def create_music_buttons(self):
        self.musicvideos = {
            "vid (7)": video7.AudioPlayerApp,
            "vid (8)": video8.AudioPlayerApp,
            "vid (9)": video9.AudioPlayerApp,
        }
        self.music.rowconfigure(0, weight=1)
        for index, (key, video_class) in enumerate(self.musicvideos.items()):
            self.music.columnconfigure(index, weight=3, uniform="videos")  # Adjust column configuration
            video_image = ImageTk.PhotoImage(Image.open(f"images/{key}.png").resize((450, 350)))
            button = tk.Button(self.music, image=video_image, text="", bg="black",
                                   fg="black",
                                   command=lambda v_class=video_class: v_class(self.meditasi),)
            button.grid(row=0, column=index, padx=(5, 5), pady=10)
            button.image = video_image

    def create_motiv_buttons(self):
        self.motivvideos = {
            "vid (4)": video4.AudioPlayerApp,
            "vid (5)": video5.AudioPlayerApp,
            "vid (6)": video6.AudioPlayerApp,
        }
        self.motiv.rowconfigure(0, weight=1)
        for index, (key, video_class) in enumerate(self.motivvideos.items()):
            self.motiv.columnconfigure(index, weight=3, uniform="videos")  # Adjust column configuration
            video_image = ImageTk.PhotoImage(Image.open(f"images/{key}.png").resize((450, 350)))
            button = tk.Button(self.motiv, image=video_image, text="", bg="black",
                                   fg="black",
                                   command=lambda v_class=video_class: v_class(self.meditasi),)
            button.grid(row=0, column=index, padx=(5, 5), pady=10)
            button.image = video_image

    def toggle_fullscreen(self, event=None):
        is_fullscreen = self.meditasi.attributes("-fullscreen")
        self.meditasi.attributes("-fullscreen", not is_fullscreen)

    def showhome(self):
        self.home.tkraise()

    def showmed(self):
        self.meditate.tkraise()
        self.create_meditate_buttons()

    def showmusic(self):
        self.music.tkraise()
        self.create_music_buttons()

    def showmotiv(self):
        self.motiv.tkraise()
        self.create_motiv_buttons()

    def showqueue(self):
        self.queueframe.tkraise()


if __name__ == "__main__":
    root = ctk.CTk()
    Meditation(root)
    root.mainloop()
