from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
import subprocess
import articlemenu
from tkinter import  messagebox
import time
import webbrowser
import audio6


class Article6 :
    def __init__(self, article6):
        self.article6 = article6
        self.folder_path = "D:/pythonProject1"
        self.article6.rowconfigure(0, weight=1)
        self.article6.columnconfigure(0, weight=1)
        height = 720
        width = 1280
        x = (self.article6.winfo_screenwidth() // 2) - (width // 2)
        y = (self.article6.winfo_screenheight() // 4) - (height // 4)
        self.article6.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.article6.config(bg="white")
        self.article6.last_keypress_time = 0
        self.article6.double_tap_interval = 0.3
        self.article6.attributes("-fullscreen", True)
        self.article6.bind("<Escape>", self.exit_fullscreen)
        self.article6.bind("<Double-Button-1>", self.toggle_fullscreen)
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
        self.img2 = self.img2.resize((self.article6.winfo_screenwidth(), self.article6.winfo_screenheight()))
        self.foto1 = ImageTk.PhotoImage(self.img2)
        self.page1 = Canvas(self.article6, width=self.article6.winfo_screenwidth(),
                             height=self.article6.winfo_screenheight(),
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
            winapp = audio6.TextToSpeechApp(win)
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
        self.my_entry.place(x=1000,y=23)

        self.my_list = Listbox(self.page1, width=40,
                               activestyle="dotbox",
                               font=("Arial",9),
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

        self.scrframe = CTkScrollableFrame(self.article6,
                                           orientation="vertical",
                                           width=self.article6.winfo_screenwidth(),
                                           height=700,
                                           fg_color='white',
                                           bg_color='white',
                                           )
        self.scrframe.place(x=0, y=89)

        self.img1 = Image.open("images\\page5 (1).png")
        self.img1 = self.img1.resize((self.article6.winfo_screenwidth(), self.article6.winfo_screenheight()))
        self.foto = ImageTk.PhotoImage(self.img1)
        self.page2 = Canvas(self.scrframe, width=self.article6.winfo_screenwidth(),
                            height=self.article6.winfo_screenheight(),
                            bg="black", highlightthickness=0)
        self.page2.pack()
        self.page2.create_image(0, 0, anchor='nw', image=self.foto)

        def linkarticle():
            webbrowser.open_new("https://atlantic.ctvnews.ca/more/healthy-lifestyle-can-reduce-genetic-risks-of-early-death-by-62-study-1.6886797")

        button_source = Button(self.page2, text="https://atlantic.ctvnews.ca/more/healthy-lifestyle-can-reduce-genetic-risks-of-early-death-by-study"
                               ,bg="white", fg="blue", borderwidth=0, activebackground='white', font=("Helvetica",9),command=linkarticle)
        button_source.place(x=150, y=426)

        self.articlebg = Image.open('images\\page5 (2).png')
        self.articlebg = self.articlebg.resize((self.article6.winfo_screenwidth(), self.article6.winfo_screenheight()))
        self.photo = ImageTk.PhotoImage(self.articlebg)
        self.page3 = Canvas(self.scrframe, width=self.article6.winfo_screenwidth(),
                              height=self.article6.winfo_screenheight(),
                              bg="#C7DFDF", highlightthickness=0, )
        self.page3.pack(pady=0, fill='both', expand=True)
        self.page3.create_image(0, 0, anchor='nw', image=self.photo)

        self.bmibg = Image.open('images\\page5 (3).png')
        self.bmibg = self.bmibg.resize((self.article6.winfo_screenwidth(), self.article6.winfo_screenheight()))
        self.photo1 = ImageTk.PhotoImage(self.bmibg)
        self.page5 = Canvas(self.scrframe, width=self.article6.winfo_screenwidth(),
                            height=self.article6.winfo_screenheight(),
                            bg="black", highlightthickness=0)
        self.page5.pack(pady=0, fill='both', expand=True)
        self.page5.create_image(0, 0, anchor='nw', image=self.photo1)

        self.medbg = Image.open('images\\page (7).png')
        self.medbg = self.medbg.resize((self.article6.winfo_screenwidth(), self.article6.winfo_screenheight()))
        self.medphoto = ImageTk.PhotoImage(self.medbg)
        self.page4 = Canvas(self.scrframe, width=self.article6.winfo_screenwidth(),
                             height= 370,
                             bg="#C7DFDF", highlightthickness=0, )
        self.page4.pack(pady=0, fill='both', expand=True)
        self.page4.create_image(0, 0, anchor='nw', image=self.medphoto)

    def toggle_fullscreen(self, event=None):
        current_time = time.time()
        if current_time - self.article6.last_keypress_time < self.article6.double_tap_interval:
            self.last_keypress_time = 0
            is_fullscreen = self.article6.attributes("-fullscreen")
            self.article6.attributes("-fullscreen", not is_fullscreen)
        else:
            self.article6.last_keypress_time = current_time

    def exit_fullscreen(self, event):
        if self.article6.attributes("-fullscreen"):
            self.article6.attributes("-fullscreen", False)

    def openmainmenu(self):
        win = Toplevel()
        articlemenu.ArticleSorterApp(win)
        win.lift()  # Membawa jendela ke depan
        win.attributes('-topmost', True)  # Membuat jendela selalu berada di depan
        win.after(1, lambda: win.attributes('-topmost', False))
        self.article6.withdraw()
        win.deiconify()

    def update(self, files):
        # Clear the listbox
        self.my_list.delete(0, END)

        if not files:
            return

        # Add files to listbox without .py extension
        for file in files:
            file_title = self.file_titles.get(file, "Unknown Title")
            self.my_list.insert(END, file_title)

    # Update entry box with listbox clicked
    def fillout(self, e):
        # Delete whatever is in the entry box
        self.my_entry.delete(0, END)

        # Add clicked list item to entry box
        self.my_entry.insert(0, self.my_list.get(ANCHOR))

    # Function to execute selected .py file
    def execute_file(self, file):
        if file:
            try:
                python_interpreter_path = "D:\pythonProject1\Scripts\python.exe"
                subprocess.Popen([python_interpreter_path, os.path.join(self.folder_path, file)])
                time.sleep(2)
                self.article6.withdraw()
            except FileNotFoundError:
                messagebox.showerror("Error", "File not found.")

    # Update the list of files when folder is selected
    def update_files(self):
        try:
            py_files = [f for f in os.listdir(self.folder_path) if f.endswith('.py')]
            self.update(py_files)
            self.toggle_listbox('show')
        except FileNotFoundError:
            messagebox.showerror("Error", "Directory not found.")

    # Function to show/hide listbox
    def toggle_listbox(self, state):
        if state == 'show':
            self.my_list.place(x=1000,y=50)
        elif state == 'hide':
            self.my_list.place_forget()

    # Function to handle key press event
    def handle_keypress(self, event):
        if event.keysym == 'Return':
            self.check()

    # Create function to check entry vs listbox
    def check(self):
        # grab what was typed
        typed = self.my_entry.get()

        if typed == '':
            self.toggle_listbox('hide')
        else:
            data = [file for file, title in self.file_titles.items() if typed.lower() in title.lower()]
            self.update(data)
            self.toggle_listbox('show')

    # Function to execute file when double-clicked in listbox
    def execute_on_double_click(self, event):
        selected_title = self.my_list.get(ANCHOR)
        # Reverse dictionary lookup to find corresponding file name
        selected_file = next((file for file, title in self.file_titles.items() if title == selected_title), None)
        self.execute_file(selected_file)

if __name__ == "__main__":
    root = Tk()
    Article6(root)
    root.mainloop()