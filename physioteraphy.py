from tkinter import *
from PIL import Image, ImageTk
from customtkinter import CTkButton, CTkFont
from tkinter import messagebox

from balance import Balance

class Physioteraphy():

    def __init__(self, sio):
        self.sio = sio
        self.sio.title("FitInclusive")
        self.sio.rowconfigure(0, weight=1)
        self.sio.columnconfigure(0, weight=1)
        height = 720
        width = 1280
        x = (self.sio.winfo_screenwidth() // 2) - (width // 2)
        y = (self.sio.winfo_screenheight() // 2) - (height // 2)
        self.sio.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.sio.resizable(0, 0)
        self.sio.config(bg="#291C4F")
        self.myfont = CTkFont(family='Poppins', size=14, weight='bold', slant='italic')

        # IMAGE

        self.img_path1 = "D:\\pythonProject1\\pict\\wheelchair.png"
        self.img_path2 = "D:\\pythonProject1\\pict\\backbutton2.png"
        self.img_path3 = "D:\\pythonProject1\\pict\\wcnexticon.png"
        self.load_image()

        # CANVAS

        canvas = Canvas(self.sio, width=self.img_back.width(), height=self.img_back.height(), bg="#291C4F", bd=0, highlightthickness=0)
        canvas.place(x=20, y=20)

        canvas2 = Canvas(self.sio, width=1080, height=150, bg="#291C4F", borderwidth=0, highlightthickness=0)
        canvas2.place(x=100, y=155)
        inner_canvas2 = Canvas(self.sio, width=200, height=150, bg="#7f7b7b", borderwidth=0, highlightthickness=0)
        inner_canvas2.place(x=100, y=155)

        # LABEL

        Label_text = Label(self.sio, text="1 EXERCISE", font=self.myfont, bg="#291C4F", fg="white")
        Label_text.place(x=100, y=120)

        Label_pojok = Label(canvas, text="physioteraphy", bg="#291C4F", fg="white", font=("Italic, 25"))
        Label_pojok.pack(side=RIGHT, padx=10)

        # BUTTON

        def open_BExercise():
            self.sio.destroy()
            new_window = Tk()
            Balance(new_window)
            new_window.mainloop()

        def back():
            self.sio.destroy()


        btn1 = Button(canvas2, image=self.img_next, bg="#291C4F", activebackground="#291C4F", width=200, height=145, borderwidth=0, highlightthickness=0, command=open_BExercise)
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
            sure = messagebox.askyesno("Exit", "Are you sure you want to exit", parent=self.sio)
            if sure:
                self.sio.destroy()

        self.sio.protocol("WM_DELETE_WINDOW", exit)
        self.insert_image(inner_canvas2, x_coord=100, y_coord=80)

        canvas2.create_text(560, 25, text="Balance Exercise", font=("Italic, 25"), fill="white")
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
    Physioteraphy(root)
    root.mainloop()
