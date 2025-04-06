from tkinter import *
from tkinter import ttk
import customtkinter
from PIL import Image, ImageTk
from customtkinter import CTkScrollableFrame
import A1
import A2
import A3
import A4
import A5
import A6
import A7
import A8



class Article:
    def __init__(self, article):
        self.article = article
        self.article.rowconfigure(0, weight=1)
        self.article.columnconfigure(0, weight=1)
        height = 720
        width = 1280
        x = (article.winfo_screenwidth() // 2) - (width // 2)
        y = (article.winfo_screenheight() // 4) - (height // 4)
        self.article.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.article.config(bg="white")
        self.article.attributes("-fullscreen", True)
        self.article.bind("<Escape>", self.toggle_fullscreen)
        self.article.bind("<Double-Button-1>", self.toggle_fullscreen)

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
        self.createwid()

        self.img2 = Image.open("images\\he.png")
        self.img2 = self.img2.resize((article.winfo_screenwidth(), article.winfo_screenheight()))
        self.foto1 = ImageTk.PhotoImage(self.img2)
        self.canva1 = Canvas(self.article, width=article.winfo_screenwidth(), height=article.winfo_screenheight(),
                             bg="black", highlightthickness=0, borderwidth=0)
        self.canva1.place(x=0, y=0)
        self.canva1.create_image(0, 0, anchor='nw', image=self.foto1)
        news1_img = Image.open("images\\1.png")
        news1_img_hover = Image.open("images\\2.png")
        news1_img = news1_img.resize((750, 360))
        news1_img_hover = news1_img_hover.resize((750, 345))
        self.news1_bg = ImageTk.PhotoImage(news1_img)
        self.news1_bg_hover = ImageTk.PhotoImage(news1_img_hover)

        def com():
            self.article1()

        def on_enter(e):
            self.news1_button.config(image=self.news1_bg_hover)

        def on_leave(e):
            self.news1_button.config(image=self.news1_bg)

        self.news1_button = Button(self.scrframe, image=self.news1_bg, width=300, height=330, command=com, border=FALSE,
                              bg="white", )
        self.news1_button.bind("<Enter>", on_enter)
        self.news1_button.bind("<Leave>", on_leave)

        def on_enter(e):
            self.news2_button.config(image=self.news2_bg_hover)

        def on_leave(e):
            self.news2_button.config(image=self.news2_bg)

        def com():
            self.article2()

        news2_img = Image.open("images\\3.png")
        news2_img_hover = Image.open("images\\4.png")
        news2_img = news2_img.resize((750, 360))
        news2_img_hover = news2_img_hover.resize((750, 345))
        self.news2_bg = ImageTk.PhotoImage(news2_img)
        self.news2_bg_hover = ImageTk.PhotoImage(news2_img_hover)

        self.news2_button = Button(self.scrframe, image=self.news2_bg, width=300, height=330, command=com, border=FALSE,
                              bg="white", )
        self.news2_button.bind("<Enter>", on_enter)
        self.news2_button.bind("<Leave>", on_leave)

        def on_enter(e):
            self.news3_button.config(image=self.news3_bg_hover)

        def on_leave(e):
            self.news3_button.config(image=self.news3_bg)

        def com():
            self.article3()

        news3_img = Image.open("images\\5.png")
        news3_img_hover = Image.open("images\\6.png")
        news3_img = news3_img.resize((750, 360))
        news3_img_hover = news3_img_hover.resize((750, 345))
        self.news3_bg = ImageTk.PhotoImage(news3_img)
        self.news3_bg_hover = ImageTk.PhotoImage(news3_img_hover)

        self.news3_button = Button(self.scrframe, image=self.news3_bg, width=300, height=330, command=com, border=FALSE,
                                   bg="white", )
        self.news3_button.bind("<Enter>", on_enter)
        self.news3_button.bind("<Leave>", on_leave)

        def on_enter(e):
            self.news4_button.config(image=self.news4_bg_hover)

        def on_leave(e):
            self.news4_button.config(image=self.news4_bg)

        def com():
            self.article4()

        news4_img = Image.open("images\\7.png")
        news4_img_hover = Image.open("images\\8.png")
        news4_img = news4_img.resize((750, 360))
        news4_img_hover = news4_img_hover.resize((750, 345))
        self.news4_bg = ImageTk.PhotoImage(news4_img)
        self.news4_bg_hover = ImageTk.PhotoImage(news4_img_hover)
        self.news4_button = Button(self.scrframe, image=self.news4_bg, width=300, height=330, command=com, border=FALSE,
                                   bg="white", )
        self.news4_button.bind("<Enter>", on_enter)
        self.news4_button.bind("<Leave>", on_leave)

        def on_enter(e):
            self.news5_button.config(image=self.news5_bg_hover)

        def on_leave(e):
            self.news5_button.config(image=self.news5_bg)

        def com():
            self.article5()

        news5_img = Image.open("images\\9.png")
        news5_img_hover = Image.open("images\\10.png")
        news5_img = news5_img.resize((750, 360))
        news5_img_hover = news5_img_hover.resize((750, 345))
        self.news5_bg = ImageTk.PhotoImage(news5_img)
        self.news5_bg_hover = ImageTk.PhotoImage(news5_img_hover)

        self.news5_button = Button(self.scrframe, image=self.news5_bg, width=300, height=330, command=com, border=FALSE,
                                   bg="white", )
        self.news5_button.bind("<Enter>", on_enter)
        self.news5_button.bind("<Leave>", on_leave)

        def on_enter(e):
            self.news6_button.config(image=self.news6_bg_hover)

        def on_leave(e):
            self.news6_button.config(image=self.news6_bg)

        def com():
            self.article6()
        news6_img = Image.open("images\\11.png")
        news6_img_hover = Image.open("images\\12.png")
        news6_img = news6_img.resize((750, 360))
        news6_img_hover = news6_img_hover.resize((750, 345))
        self.news6_bg = ImageTk.PhotoImage(news6_img)
        self.news6_bg_hover = ImageTk.PhotoImage(news6_img_hover)

        self.news6_button = Button(self.scrframe, image=self.news6_bg, width=300, height=330, command=com, border=FALSE,
                                   bg="white", )
        self.news6_button.bind("<Enter>", on_enter)
        self.news6_button.bind("<Leave>", on_leave)

    def createwid(self):
        self.scrframe = CTkScrollableFrame(self.article,
                                          orientation="vertical",
                                          width=self.article.winfo_screenwidth(),
                                          height=700,
                                          fg_color='white',
                                          bg_color='white',
                                          )
        self.scrframe.place(x=370, y=120)
        for num, article in self.article_images.items():

            self.news1_button.grid(row=0, column=0, padx=10, pady=10)
            self.article_buttons[article] = self.news1_button

            self.news2_button.grid(row=0, column=1, padx=10, pady=10)
            self.article_buttons[article] = self.news2_button

            self.news3_button.grid(row=1, column=0, padx=10, pady=10)
            self.article_buttons[article] = self.news3_button

            self.news4_button.grid(row=1, column=1, padx=10, pady=10)
            self.article_buttons[article] = self.news4_button

            self.news5_button.grid(row=2, column=0, padx=10, pady=10)
            self.article_buttons[article] = self.news5_button

            self.news6_button.grid(row=2, column=1, padx=10, pady=10)
            self.article_buttons[article] = self.news6_button

        self.sort_options = ttk.Combobox(self.article, values=["A-Z", "Z-A"])
        self.sort_options.current(0)
        self.sort_options.pack(pady=10)

        self.btn_sort = Button(self.article, text="Urutkan", command=self.sort_articles)
        self.btn_sort.pack(pady=10)

    def sort_articles(self):
        sort_option = self.sort_options.get()
        sorted_articles = list(self.article_images.items())

        if sort_option == "A-Z":
            self.bubble_sort_articles_asc(sorted_articles)
        elif sort_option == "Z-A":
            self.bubble_sort_articles_desc(sorted_articles)

        self.update_buttons(sorted_articles)

    def bubble_sort_articles_asc(self, articles):
        n = len(articles)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if articles[j][1] > articles[j + 1][1]:
                    articles[j], articles[j + 1] = articles[j + 1], articles[j]

    def bubble_sort_articles_desc(self, articles):
        n = len(articles)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if articles[j][1] < articles[j + 1][1]:
                    articles[j], articles[j + 1] = articles[j + 1], articles[j]

    def update_buttons(self, sorted_articles):
        for i, (num, article) in enumerate(sorted_articles):
            print(article)
            row = i // 2
            col = i % 2

            self.news1_button = self.article_buttons[str(article)]
            print(self.article_buttons[article])
            self.news1_button.grid(row=row, column=col, pady=10, padx=10)

            self.news2_button = self.article_buttons[article]
            self.news2_button.grid(row=row, column=col, pady=10, padx=10)

            self.news3_button = self.article_buttons[article]
            self.news3_button.grid(row=row, column=col, pady=10, padx=10)

            self.news4_button = self.article_buttons[article]
            self.news4_button.grid(row=row, column=col, pady=10, padx=10)

            self.news45button = self.article_buttons[article]
            self.news45button.grid(row=row, column=col, pady=10, padx=10)

            self.news6_button = self.article_buttons[article]
            self.news6_button.grid(row=row, column=col, pady=10, padx=10)
    def article1(self):
        win = Toplevel()
        A1.Article1(win)
        win.lift()  # Membawa jendela ke depan
        win.attributes('-topmost', True)  # Membuat jendela selalu berada di depan
        win.after(1, lambda: win.attributes('-topmost', False))
        self.article.withdraw()
        win.deiconify()



    def toggle_fullscreen(self, event=None):
        is_fullscreen = self.article.attributes("-fullscreen")
        self.article.attributes("-fullscreen", not is_fullscreen)
if __name__ == "__main__" :
    root = customtkinter.CTk()
    Article(root)
    root.mainloop()