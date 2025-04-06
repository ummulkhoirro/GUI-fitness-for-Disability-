from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
import subprocess
import articlemenu
from tkinter import messagebox
import time
import webbrowser
import os
import audio1

class Article1:
    def __init__(self, article1):
        self.article1 = article1
        self.folder_path = "D:/pythonProject1"
        self.article1.rowconfigure(0, weight=1)
        self.article1.columnconfigure(0, weight=1)
        height = 720
        width = 1280
        x = (self.article1.winfo_screenwidth() // 2) - (width // 2)
        y = (self.article1.winfo_screenheight() // 4) - (height // 4)
        self.article1.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.article1.config(bg="white")
        self.article1.last_keypress_time = 0
        self.article1.double_tap_interval = 0.3
        self.article1.attributes("-fullscreen", True)
        self.article1.bind("<Escape>", self.exit_fullscreen)
        self.article1.bind("<Double-Button-1>", self.toggle_fullscreen)
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
        self.img2 = self.img2.resize((self.article1.winfo_screenwidth(), self.article1.winfo_screenheight()))
        self.foto1 = ImageTk.PhotoImage(self.img2)
        self.page1 = Canvas(self.article1, width=self.article1.winfo_screenwidth(),
                            height=self.article1.winfo_screenheight(),
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
            winapp = audio1.TextToSpeechApp(win)
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

        # Function to show/hide listbox
        self.toggle_listbox('hide')

        # Function to handle key press event
        self.my_entry.bind("<Key>", self.handle_keypress)

        # Bind double-click event on listbox
        self.my_list.bind("<Double-Button-1>", self.execute_on_double_click)

        # Create a binding on the listbox onclick
        self.my_list.bind("<<ListboxSelect>>", self.fillout)

        def mainmenu():
            self.openmainmenu()

        def home_command():
            mainmenu()

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

        self.scrframe = CTkScrollableFrame(self.article1,
                                           orientation="vertical",
                                           width=self.article1.winfo_screenwidth(),
                                           height=700,
                                           fg_color='white',
                                           bg_color='white',
                                           )
        self.scrframe.place(x=0, y=89)

        self.img1 = Image.open("images\\page (1).png")
        self.img1 = self.img1.resize((self.article1.winfo_screenwidth(), self.article1.winfo_screenheight()))
        self.foto = ImageTk.PhotoImage(self.img1)
        self.page2 = Canvas(self.scrframe, width=self.article1.winfo_screenwidth(),
                            height=self.article1.winfo_screenheight(),
                            bg="black", highlightthickness=0)
        self.page2.pack()
        self.page2.create_image(0, 0, anchor='nw', image=self.foto)

        def linkarticle():
            webbrowser.open_new("https://www.ucsfhealth.org/education/behavior-modification-ideas-for-weight-management")

        button_source = Button(self.page2, text="https://www.ucsfhealth.org/education/behavior-modification-ideas-for-weight-management"
                               ,bg="white", fg="blue", borderwidth=0, activebackground='white', font=("Helvetica",13),command=linkarticle)
        button_source.place(x=150, y=422)


        self.articlebg = Image.open('images\\page (2).png')
        self.articlebg = self.articlebg.resize((self.article1.winfo_screenwidth(), self.article1.winfo_screenheight()))
        self.photo = ImageTk.PhotoImage(self.articlebg)
        self.page3 = Canvas(self.scrframe, width=self.article1.winfo_screenwidth(),
                            height=self.article1.winfo_screenheight(),
                            bg="#C7DFDF", highlightthickness=0, )
        self.page3.pack(pady=0, fill='both', expand=True)
        self.page3.create_image(0, 0, anchor='nw', image=self.photo)

        self.medbg = Image.open('images\\page (3).png')
        self.medbg = self.medbg.resize((self.article1.winfo_screenwidth(), self.article1.winfo_screenheight()))
        self.medphoto = ImageTk.PhotoImage(self.medbg)
        self.page4 = Canvas(self.scrframe, width=self.article1.winfo_screenwidth(),
                            height=self.article1.winfo_screenheight(),
                            bg="#C7DFDF", highlightthickness=0, )
        self.page4.pack(pady=0, fill='both', expand=True)
        self.page4.create_image(0, 0, anchor='nw', image=self.medphoto)

        self.bmibg = Image.open('images\\page (4).png')
        self.bmibg = self.bmibg.resize((self.article1.winfo_screenwidth(), self.article1.winfo_screenheight()))
        self.photo1 = ImageTk.PhotoImage(self.bmibg)
        self.page5 = Canvas(self.scrframe, width=self.article1.winfo_screenwidth(),
                            height=self.article1.winfo_screenheight(),
                            bg="black", highlightthickness=0)
        self.page5.pack(pady=0, fill='both', expand=True)
        self.page5.create_image(0, 0, anchor='nw', image=self.photo1)

        self.newsimg = Image.open('images\\page (5).png')
        self.newsimg = self.newsimg.resize((self.article1.winfo_screenwidth(), self.article1.winfo_screenheight()))
        self.photonews = ImageTk.PhotoImage(self.newsimg)
        self.page6 = Canvas(self.scrframe, width=self.article1.winfo_screenwidth(),
                            height=self.article1.winfo_screenheight(),
                            bg="white", highlightthickness=0)
        self.page6.pack(pady=0, fill='both', expand=True)
        self.page6.create_image(0, 0, anchor='nw', image=self.photonews)

        self.page7img = Image.open('images\\page (6).png')
        self.page7img = self.page7img.resize((self.article1.winfo_screenwidth(), self.article1.winfo_screenheight()))
        self.photopage7 = ImageTk.PhotoImage(self.page7img)
        self.page7 = Canvas(self.scrframe, width=self.article1.winfo_screenwidth(),
                            height=self.article1.winfo_screenheight(),
                            bg="white", highlightthickness=0)
        self.page7.pack(pady=0, fill='both', expand=True)
        self.page7.create_image(0, 0, anchor='nw', image=self.photopage7)

        self.page8img = Image.open('images\\page (7).png')
        self.page8img = self.page8img.resize((self.article1.winfo_screenwidth(), self.article1.winfo_screenheight()))
        self.photopage8 = ImageTk.PhotoImage(self.page8img)
        self.page8 = Canvas(self.scrframe, width=self.article1.winfo_screenwidth(),
                            height=370,
                            bg="white", highlightthickness=0)
        self.page8.pack(pady=0, fill='both', expand=True)
        self.page8.create_image(0, 0, anchor='nw', image=self.photopage8)

    def toggle_fullscreen(self, event=None):
        current_time = time.time()
        if current_time - self.article1.last_keypress_time < self.article1.double_tap_interval:
            self.last_keypress_time = 0
            is_fullscreen = self.article1.attributes("-fullscreen")
            self.article1.attributes("-fullscreen", not is_fullscreen)
        else:
            self.article1.last_keypress_time = current_time

    def exit_fullscreen(self, event):
        if self.article1.attributes("-fullscreen"):
            self.article1.attributes("-fullscreen", False)

    def openmainmenu(self):
        win = Toplevel()
        articlemenu.ArticleSorterApp(win)
        win.lift()
        win.attributes('-topmost', True)
        win.after(1, lambda: win.attributes('-topmost', False))
        self.article1.withdraw()
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
                python_interpreter_path = "D:\pythonProject1\Scripts\python.exe"
                subprocess.Popen([python_interpreter_path, os.path.join(self.folder_path, file)])
                time.sleep(2)
                self.article1.withdraw()
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


if __name__ == "__main__":
    root = Tk()
    Article1(root)
    root.mainloop()
