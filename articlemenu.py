from tkinter import *
import customtkinter
from PIL import Image, ImageTk
from customtkinter import CTkScrollableFrame, CTkOptionMenu
from tkinter import messagebox
import os
from functools import partial
import A1
import A2
import A3
import A4
import A5
import A6
import A7
import A8
import time



class ArticleSorterApp:
    def __init__(self, root):
        self.root = root
        self.last_keypress_time = 0
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        height = 720
        width = 1280
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 4) - (height // 4)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.root.config(bg="white")
        self.root.title("Pengurutan Artikel")
        self.root.attributes("-fullscreen", True)
        self.root.bind("<Escape>", self.exit_fullscreen)
        self.root.bind("<Double-Button-1>", self.toggle_fullscreen)

        self.article_images = {
            1: "Behavior Modification Ideas for Weight Management",
            2: "Guidelines for Losing Weight",
            3: "Disability is not an obstacle to success.",
            4: "Living Well With Disabilty",
            5: "Improve Your Sleep Hygine",
            6: "Healthy Lifestyle is Choice",
            7: "Stress Hacks: Your Path to Peace",
            8: "Making AI delivery robots disability-friendly"
        }

        self.article_buttons = {}
        self.img2 = Image.open("images\\he.png")
        self.img2 = self.img2.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
        self.foto1 = ImageTk.PhotoImage(self.img2)
        self.canva1 = Canvas(self.root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(),
                             bg="black", highlightthickness=0, borderwidth=0)
        self.canva1.place(x=0, y=0)
        self.canva1.create_image(0, 0, anchor='nw', image=self.foto1)
        self.sort_options = CTkOptionMenu(self.root, values=["A-Z", "Z-A"], command=self.sort_articles, width=100)
        self.sort_options.set("A-Z")
        self.sort_options.configure(bg_color="white", fg_color="white", text_color="black", dropdown_fg_color="white",
                                    dropdown_text_color="black", button_color="white", anchor="center")
        self.sort_options.place(x=256, y=160)

        backimg = Image.open("images/back.png")
        backimg = backimg.resize((120,80))
        self.backbg = ImageTk.PhotoImage(backimg)
        back = Button(self.root, image=self.backbg, width=100, height=70,fg="white", border=False,background="white",command=self.openmainmenu)
        back.place(x=10,y=20)

        self.create_widgets()

    def create_widgets(self):
        self.main_frame = CTkScrollableFrame(self.canva1, orientation="vertical", width=self.root.winfo_screenwidth(),
                                             height=700, fg_color='white', bg_color='white')
        self.main_frame.place(x=0, y=200)

        for num, article in self.article_images.items():
            normal_image_path = f"images/{num}.png"

            # Memuat gambar normal
            if os.path.exists(normal_image_path):
                normal_image = Image.open(normal_image_path)
                normal_image = normal_image.resize((580, 430))
                normal_photo = ImageTk.PhotoImage(normal_image)
            else:
                normal_photo = None

            btn = Button(self.main_frame, text="", image=normal_photo,
                         compound="top", width=550, height=340,cursor="hand2",highlightthickness=0,
                         bg="white", border=False, command=partial(self.open_article, num),activebackground="grey")
            btn.normal_photo = normal_photo
            btn.grid(row=(num - 1) // 2, column=(num - 1) % 2, pady=0, padx=60)
            self.article_buttons[article] = btn


    def insertion_sort_articles(self, articles):
        for i in range(1, len(articles)):
            key = articles[i]
            j = i - 1
            while j >= 0 and key[1] < articles[j][1]:
                articles[j + 1] = articles[j]
                j -= 1
            articles[j + 1] = key
        return articles

    def sort_articles(self, choice):
        choice = self.sort_options.get()
        sorted_articles = list(self.article_images.items())

        if choice == "A-Z":
            sorted_articles = self.insertion_sort_articles(sorted_articles)
        elif choice == "Z-A":
            sorted_articles = self.insertion_sort_articles(sorted_articles)[::-1]

        self.update_buttons(sorted_articles)

    def update_buttons(self, sorted_articles):
        for i, (num, article) in enumerate(sorted_articles):
            row = i // 2
            col = i % 2

            image_path = f"images/{num}.png"
            if os.path.exists(image_path):
                image = Image.open(image_path)
                image = image.resize((580, 430))
                photo = ImageTk.PhotoImage(image)
            else:
                messagebox.showerror("Error")

            btn = self.article_buttons[article]
            btn.config(image=photo, compound="top", width=550, height=340, bg="white")
            btn.photo = photo
            btn.grid(row=row, column=col, pady=0, padx=60)


    def open_article(self, num):
        win = Toplevel()
        if num == 1:
            A1.Article1(win)
        elif num == 2:
            A2.Article2(win)
        elif num == 3:
            A3.Article3(win)
        elif num == 4:
            A4.Article4(win)
        elif num == 5:
            A5.Article5(win)
        elif num == 6:
            A6.Article6(win)
        elif num == 7:
            A7.Article7(win)
        elif num == 8:
            A8.Article8(win)
        win.lift()
        win.attributes('-topmost', True)
        win.after(1, lambda: win.attributes('-topmost', False))
        self.root.withdraw()
        win.deiconify()
    def toggle_fullscreen(self, event=None):
        current_time = time.time()
        if current_time - self.root.last_keypress_time < self.root.double_tap_interval:
            self.last_keypress_time = 0
            is_fullscreen = self.root.attributes("-fullscreen")
            self.root.attributes("-fullscreen", not is_fullscreen)
        else:
            self.root.last_keypress_time = current_time

    def exit_fullscreen(self, event):
        if self.root.attributes("-fullscreen"):
            self.root.attributes("-fullscreen", False)

    def openmainmenu(self):
        self.root.withdraw()

if __name__ == "__main__":
    root = customtkinter.CTk()
    app = ArticleSorterApp(root)
    root.mainloop()

