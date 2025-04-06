from tkinter import *
from PIL import Image, ImageTk
from customtkinter import CTkButton, CTkFont
from tkinter import messagebox

from danceaerobic import DanceAerobic

class Aerobics():

    def __init__(self, aerob):
        self.aerob = aerob
        self.aerob.title("FitInclusive")
        self.aerob.rowconfigure(0, weight=1)
        self.aerob.columnconfigure(0, weight=1)
        height = 720
        width = 1280
        x = (self.aerob.winfo_screenwidth() // 2) - (width // 2)
        y = (self.aerob.winfo_screenheight() // 2) - (height // 2)
        self.aerob.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.aerob.resizable(0, 0)
        self.aerob.config(bg="#291C4F")
        self.myfont = CTkFont(family='Poppins', size=14, weight='bold', slant='italic')

        # IMAGE

        self.img_path1 = "D:\\pythonProject1\\pict\\wheelchair.png"
        self.img_path2 = "D:\\pythonProject1\\pict\\backbutton2.png"
        self.img_path3 = "D:\\pythonProject1\\pict\\wcnexticon.png"
        self.load_image()

        # CANVAS

        canvas = Canvas(self.aerob, width=self.img_back.width(), height=self.img_back.height(), bg="#291C4F", bd=0, highlightthickness=0)
        canvas.place(x=20, y=20)

        canvas2 = Canvas(self.aerob, width=1080, height=150, bg="#291C4F", borderwidth=0, highlightthickness=0)
        canvas2.place(x=100, y=155)
        inner_canvas2 = Canvas(self.aerob, width=200, height=150, bg="#7f7b7b", borderwidth=0, highlightthickness=0)
        inner_canvas2.place(x=100, y=155)

        # LABEL

        Label_text = Label(self.aerob, text="1 EXERCISE", font=self.myfont, bg="#291C4F", fg="white")
        Label_text.place(x=100, y=120)

        Label_pojok = Label(canvas, text="wheelchair aerob", bg="#291C4F", fg="white", font=("Italic, 25"))
        Label_pojok.pack(side=RIGHT, padx=10)

        # BUTTON

        def open_DAerobic():
            self.aerob.destroy()
            new_window = Tk()
            DanceAerobic(new_window)
            new_window.mainloop()

        def back():
            self.aerob.destroy()


        btn1 = Button(canvas2, image=self.img_next, bg="#291C4F", activebackground="#291C4F", width=200, height=145, borderwidth=0, highlightthickness=0, command=open_DAerobic)
        btn1.pack()

        btn_back = CTkButton(master=canvas,
                             image=self.img_back,
                             fg_color="#291C4F",
                             hover_color="#291C4F",
                             width=50,
                             text='',
                             command=back)
        btn_back.pack()

        def exit():
            sure = messagebox.askyesno("Exit", "Are you sure you want to exit", parent=self.aerob)
            if sure:
                self.aerob.destroy()

        self.aerob.protocol("WM_DELETE_WINDOW", exit)
        self.insert_image(inner_canvas2, x_coord=100, y_coord=80)

        canvas2.create_text(560, 25, text="Dance Aerobic", font=("Italic, 25"), fill="white")
        canvas2.create_text(560, 50, text="10 minutes", font=self.myfont, fill="white")

        x_right = 1080
        y_center = 75
        canvas2.create_window(x_right, y_center, window=btn1, anchor=E)


    def load_image(self):
        img = Image.open(self.img_path1)
        width = 400
        height = 350
        width_ratio = width / img.width
        height_ratio = height / img.height
        resize_ratio = min(width_ratio, height_ratio)
        new_width = int(img.width * resize_ratio)
        new_height = int(img.height * resize_ratio)
        img = img.resize((new_width, new_height), Image.LANCZOS)
        img_back = Image.open(self.img_path2)
        img_next = Image.open(self.img_path3)
        self.img = ImageTk.PhotoImage(img)
        self.img_back = ImageTk.PhotoImage(img_back)
        img_next = img_next.resize((50, 80), Image.LANCZOS)
        self.img_next = ImageTk.PhotoImage(img_next)
        return self.img

    def insert_image(self, canvas, x_coord, y_coord):
        canvas.create_image(x_coord, y_coord, image=self.img)

if __name__ == "__main__":
    root = Tk()
    Aerobics(root)
    root.mainloop()
