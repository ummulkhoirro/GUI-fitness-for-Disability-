from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
import subprocess
import articlemenu
from tkinter import messagebox
import time
import webbrowser
import audio8
from tkVideoPlayer import TkinterVideo
import pygame


class Article8:
    def __init__(self, article8):
        self.article8 = article8
        self.folder_path = "D:/pythonProject1"
        self.article8.rowconfigure(0, weight=1)
        self.article8.columnconfigure(0, weight=1)
        height = 720
        width = 1280
        x = (self.article8.winfo_screenwidth() // 2) - (width // 2)
        y = (self.article8.winfo_screenheight() // 4) - (height // 4)
        self.article8.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.article8.config(bg="white")
        self.article8.last_keypress_time = 0
        self.article8.double_tap_interval = 0.3
        self.article8.attributes("-fullscreen", True)
        self.article8.bind("<Escape>", self.exit_fullscreen)
        self.article8.bind("<Double-Button-1>", self.toggle_fullscreen)
        self.file_titles = {
            "A1.py": "Behavior Modification Ideas for Weight Management",
            "A2.py": "Guidelines for Losing Weight",
            "A3.py": "Disability is not an obstacle to success. ",
            "A4.py": "Living Well With Disabilty",
            "A5.py": "Improve Your Sleep Hygine",
            "A6.py": "Healthy Lifestyle is Choice",
            "A7.py": "Stress Hacks: Your Path to Peace",
            "A8.py": "Making AI delivery robots disability-friendly"
        }

        self.img2 = Image.open("images\\he1.png")
        self.img2 = self.img2.resize((self.article8.winfo_screenwidth(), self.article8.winfo_screenheight()))
        self.foto1 = ImageTk.PhotoImage(self.img2)
        self.page1 = Canvas(self.article8, width=self.article8.winfo_screenwidth(),
                            height=self.article8.winfo_screenheight(),
                            bg="black", highlightthickness=0, borderwidth=0)
        self.page1.place(x=0, y=0)
        self.page1.create_image(0, 0, anchor='nw', image=self.foto1)

        def on_hoverjoin(event):
            listen.configure(text_color="black")
            listen.configure(font=("Arial", 19, 'bold'))

        def on_leavejoin(event):
            listen.configure(text_color="black")
            listen.configure(font=("Arial", 17, 'bold'))

        def listenow():
            win = CTkToplevel()
            win.iconbitmap("audio.ico")
            screen_width = win.winfo_screenwidth()
            win.geometry(f"200x60+{screen_width // 2 - 15}+58")
            winapp = audio8.TextToSpeechApp(win)
            win.title("")
            win.lift()
            win.focus_force()
            win.attributes('-topmost', True)
            win.after(1, lambda: win.attributes('-topmost', False))

            def keep_on_top():
                win.lift()
                win.after(100, keep_on_top)

            keep_on_top()

            def close_window(event=None, app=winapp):
                app.pause()

                app.root.after(1000, win.destroy)

            win.bind("<Escape>", close_window)
            win.protocol("WM_DELETE_WINDOW", close_window)

        listen = CTkButton(self.page1,
                           text="Listen",
                           bg_color="white",
                           fg_color="white",
                           text_color="black",
                           font=("Arial", 17, 'bold'),
                           width=140,
                           height=50,
                           corner_radius=10,
                           hover_color="black",
                           command=listenow)
        listen.place(x=700, y=27)
        listen.bind("<Enter>", on_hoverjoin)
        listen.bind("<Leave>", on_leavejoin)
        self.my_entry = CTkEntry(self.page1, font=("Arial", 15),
                                 text_color="black",
                                 width=300,
                                 fg_color="white",
                                 border_color="black",
                                 border_width=1,
                                 bg_color="white",
                                 placeholder_text="Cari artikel yang ingin kamu cari",
                                 placeholder_text_color="black")
        self.my_entry.place(x=1000, y=23)

        self.my_list = Listbox(self.page1, width=40,
                               activestyle="dotbox",
                               font=("Arial", 9),
                               highlightthickness=1,
                               highlightcolor="black",
                               highlightbackground="black")

        self.toggle_listbox('hide')

        self.my_entry.bind("<Key>", self.handle_keypress)

        self.my_list.bind("<Double-Button-1>", self.execute_on_double_click)
        self.my_list.bind("<<ListboxSelect>>", self.fillout)

        def main():
            self.openmainmenu()

        def home_command():
            main()

        def on_hoverhome(event):
            self.home_button.configure(text_color="black")
            self.home_button.configure(font=("Arial", 19, 'bold'))

        def on_leavehome(event):
            self.home_button.configure(text_color="black")
            self.home_button.configure(font=("Arial", 17, 'bold'))

        self.home_button = CTkButton(self.page1,
                                     text="home",
                                     bg_color="white",
                                     fg_color="white",
                                     text_color="black",
                                     font=("Arial", 17, 'bold'),
                                     width=140,
                                     height=50,
                                     corner_radius=10,
                                     hover_color="black",
                                     command=home_command)
        self.home_button.place(x=550, y=27)

        self.home_button.bind("<Enter>", on_hoverhome)
        self.home_button.bind("<Leave>", on_leavehome)

        self.scrframe = CTkScrollableFrame(self.article8,
                                           orientation="vertical",
                                           width=self.article8.winfo_screenwidth(),
                                           height=700,
                                           fg_color='white',
                                           bg_color='white',
                                           )
        self.scrframe.place(x=0, y=89)

        self.img1 = Image.open("images\\page7 (1).png")
        self.img1 = self.img1.resize((self.article8.winfo_screenwidth(), self.article8.winfo_screenheight()))
        self.foto = ImageTk.PhotoImage(self.img1)
        self.page2 = Canvas(self.scrframe, width=self.article8.winfo_screenwidth(),
                            height=self.article8.winfo_screenheight(),
                            bg="black", highlightthickness=0)
        self.page2.pack()
        self.page2.create_image(0, 0, anchor='nw', image=self.foto)

        def linkarticle():
            webbrowser.open_new("https://www.bbc.com/news/disability-65719649")

        button_source = Button(self.page2, text="https://www.bbc.com/news/disability-65719649"
                               , bg="white", fg="blue", borderwidth=0, activebackground='white', font=("Helvetica", 9),
                               command=linkarticle)
        button_source.place(x=150, y=426)

        self.articlebg = Image.open('images\\page7 (2).png')
        self.articlebg = self.articlebg.resize((self.article8.winfo_screenwidth(), self.article8.winfo_screenheight()))
        self.photo = ImageTk.PhotoImage(self.articlebg)
        self.page3 = Canvas(self.scrframe, width=self.article8.winfo_screenwidth(),
                            height=self.article8.winfo_screenheight(),
                            bg="#C7DFDF", highlightthickness=0, )
        self.page3.pack(pady=0, fill='both', expand=True)
        self.page3.create_image(0, 0, anchor='nw', image=self.photo)

        self.medbg = Image.open('images\\page7 (3).png')
        self.medbg = self.medbg.resize((self.article8.winfo_screenwidth(), self.article8.winfo_screenheight()))
        self.medphoto = ImageTk.PhotoImage(self.medbg)
        self.page4 = Canvas(self.scrframe, width=self.article8.winfo_screenwidth(),
                            height=self.article8.winfo_screenheight(),
                            bg="#C7DFDF", highlightthickness=0, )
        self.page4.pack(pady=0, fill='both', expand=True)
        self.page4.create_image(0, 0, anchor='nw', image=self.medphoto)

        self.bmibg = Image.open('images\\page7 (4).png')
        self.bmibg = self.bmibg.resize((self.article8.winfo_screenwidth(), self.article8.winfo_screenheight()))
        self.photo1 = ImageTk.PhotoImage(self.bmibg)
        self.page5 = Canvas(self.scrframe, width=self.article8.winfo_screenwidth(),
                            height=self.article8.winfo_screenheight(),
                            bg="black", highlightthickness=0)
        self.page5.pack(pady=0, fill='both', expand=True)
        self.page5.create_image(0, 0, anchor='nw', image=self.photo1)

        self.page7img = Image.open('images\\page7 (6).png')
        self.page7img = self.page7img.resize((self.article8.winfo_screenwidth(), self.article8.winfo_screenheight()))
        self.photopage7 = ImageTk.PhotoImage(self.page7img)
        self.page7 = Canvas(self.scrframe, width=self.article8.winfo_screenwidth(),
                            height=500,
                            bg="white", highlightthickness=0)
        self.page7.pack(pady=0, fill='both', expand=True)
        self.page7.create_image(0, 0, anchor='nw', image=self.photopage7)

        def on_enter(e):
            self.widget1_button.config(image=self.widget1_img_hover)

        def on_leave(e):
            self.widget1_button.config(image=self.widget1_img_bg)

        def on_click(e):
            self.widget1_button.place_forget()
            self.vid_player.place(x=400, y=60, width=360, height=450)
            self.load_video()

        widget1_img = Image.open("images\\vbtn.png")
        widget1_img_hover = Image.open("images\\vbtnh.png")
        widget1_img_tl = Image.open("images\\vbtnp.png")
        widget1_img = widget1_img.resize((1006, 450))
        widget1_img_hover = widget1_img_hover.resize((1006, 450))
        widget1_img_tl = widget1_img_tl.resize((1006, 450))
        self.widget1_img_bg = ImageTk.PhotoImage(widget1_img)
        self.widget1_img_hover = ImageTk.PhotoImage(widget1_img_hover)
        self.widget1_img_tl = ImageTk.PhotoImage(widget1_img_tl)

        self.widget1_button = Button(self.page7, image=self.widget1_img_bg, width=750, height=379, border=FALSE,
                                     bg="white",)
        self.widget1_button.place(x=150, y=50)

        self.widget1_button.bind("<Enter>", on_enter)
        self.widget1_button.bind("<Leave>", on_leave)
        self.widget1_button.bind("<Button-1>", on_click)

        self.vid_player = TkinterVideo(master=self.page7, scaled=True, bg="gray25", width=300, height=100)
        self.vid_player.bind("<<Ended>>", self.video_ended)

        self.newsimg = Image.open('images\\end1.png')
        self.newsimg = self.newsimg.resize((self.article8.winfo_screenwidth(), self.article8.winfo_screenheight()))
        self.photonews = ImageTk.PhotoImage(self.newsimg)
        self.page6 = Canvas(self.scrframe, width=self.article8.winfo_screenwidth(),
                            height=self.article8.winfo_screenheight(),
                            bg="white", highlightthickness=0)
        self.page6.pack(pady=0, fill='both', expand=True)
        self.page6.create_image(0, 0, anchor='nw', image=self.photonews)



    def toggle_fullscreen(self, event=None):
        current_time = time.time()
        if current_time - self.article8.last_keypress_time < self.article8.double_tap_interval:
            is_fullscreen = self.article8.attributes("-fullscreen")
            self.article8.attributes("-fullscreen", not is_fullscreen)
        else:
            self.article8.last_keypress_time = current_time

    def exit_fullscreen(self, event):
        if self.article8.attributes("-fullscreen"):
            self.article8.attributes("-fullscreen", False)

    def openmainmenu(self):
        win = Toplevel()
        articlemenu.ArticleSorterApp(win)
        win.lift()
        win.attributes('-topmost', True)
        win.after(1, lambda: win.attributes('-topmost', False))
        self.article8.withdraw()
        win.deiconify()

    def update(self, files):
        self.my_list.delete(0, END)

        if not files:
            return

        for file in files:
            file_title = self.file_titles.get(file, "Unknown Title")
            self.my_list.insert(END, file_title)

    def fillout(self, e):
        self.my_entry.delete(0, END)

        self.my_entry.insert(0, self.my_list.get(ANCHOR))

    def execute_file(self, file):
        if file:
            try:
                python_interpreter_path = "D:\\pythonProject1\\Scripts\\python.exe"
                subprocess.Popen([python_interpreter_path, os.path.join(self.folder_path, file)])
                time.sleep(2)
                self.article8.withdraw()
            except FileNotFoundError:
                messagebox.showerror("Error", "File not found.")

    def update_files(self):
        try:
            py_files = [f for f in os.listdir(self.folder_path) if f.endswith('.py')]
            self.update(py_files)
            self.toggle_listbox('show')
        except FileNotFoundError:
            messagebox.showerror("Error", "Directory not found.")

    def toggle_listbox(self, state):
        if state == 'show':
            self.my_list.place(x=1000, y=50)
        elif state == 'hide':
            self.my_list.place_forget()

    def handle_keypress(self, event):
        if event.keysym == 'Return':
            self.check()

    def check(self):
        typed = self.my_entry.get()

        if typed == '':
            self.toggle_listbox('hide')
        else:
            data = [file for file, title in self.file_titles.items() if typed.lower() in title.lower()]
            self.update(data)
            self.toggle_listbox('show')

    def execute_on_double_click(self, event):
        selected_title = self.my_list.get(ANCHOR)
        selected_file = next((file for file, title in self.file_titles.items() if title == selected_title), None)
        self.execute_file(selected_file)

    def load_video(self):
        file_path = "video\\vid_slowed.mp4"

        if file_path:
            self.vid_player.load(file_path)
            audio_path = "video\\vid1.wav"
            pygame.mixer.init()
            pygame.mixer.music.load(audio_path)
            self.vid_player.play()
            pygame.mixer.music.play()

    def video_ended(self, event):
        pygame.mixer.music.stop()
        self.vid_player.place_forget()
        self.widget1_button.place(x=150, y=50)


if __name__ == "__main__":
    root = Tk()
    Article8(root)
    root.mainloop()
