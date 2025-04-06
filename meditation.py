from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

class Meditasi:
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

        def exitt2():
            sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=self.meditasi, )
            if sure:
                self.meditasi.destroy()

        self.meditasi.protocol("WM_DELETE_WINDOW", exitt2)
        self.img2 = Image.open("images\\medhe.png")
        self.img2 = self.img2.resize((meditasi.winfo_screenwidth(), meditasi.winfo_screenheight()))
        self.foto1 = ImageTk.PhotoImage(self.img2)
        self.canva1 = Canvas(self.meditasi, width=meditasi.winfo_screenwidth(), height=meditasi.winfo_screenheight(),
                             bg="black", highlightthickness=0, borderwidth=0)
        self.canva1.place(x=0, y=0)
        self.canva1.create_image(0, 0, anchor='nw', image=self.foto1)

        self.scrframe = CTkScrollableFrame(self.meditasi,
                                           orientation="vertical",
                                           width=1280,
                                           height=690,
                                           fg_color='#0A0D32',
                                           bg_color='#0A0D32',
                                           border_width=0,
                                           )
        self.scrframe.place(x=75, y=0)

        self.img1 = Image.open("images\\med1.png")
        self.img1 = self.img1.resize((1280, self.meditasi.winfo_screenheight()))
        self.foto = ImageTk.PhotoImage(self.img1)
        self.canva = Canvas(self.scrframe, width=meditasi.winfo_screenwidth(), height=meditasi.winfo_screenheight(),
                            bg="black", highlightthickness=0)
        self.canva.pack()
        self.canva.create_image(0, 0, anchor='nw', image=self.foto)

        self.articlebg = Image.open('images\\med2.png')
        self.articlebg = self.articlebg.resize((1280, meditasi.winfo_screenheight()))
        self.photo = ImageTk.PhotoImage(self.articlebg)
        self.home_bg = Canvas(self.scrframe, width=meditasi.winfo_screenwidth(), height=meditasi.winfo_screenheight(),
                              bg="#C7DFDF", highlightthickness=0, )
        self.home_bg.pack(pady=0, fill='both', expand=True)
        self.home_bg.create_image(0, 0, anchor='nw', image=self.photo)

        
    def toggle_fullscreen(self, event=None):
        is_fullscreen = self.meditasi.attributes("-fullscreen")
        self.meditasi.attributes("-fullscreen", not is_fullscreen)
        
if __name__ == "__main__":
    root = Tk()
    Meditasi(root)
    root.mainloop()