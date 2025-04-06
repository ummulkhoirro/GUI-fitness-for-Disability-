import tkinter
from tkinter import *
from customtkinter import CTkToplevel
from PIL import Image, ImageTk
from mainmenu import Mainmenu
import threading


class LoadingScreen:
    def __init__(self, parent):
        self.load = CTkToplevel(parent)
        self.load.title("")
        self.load.iconbitmap("audio.ico")
        self.load.geometry("400x200")
        height = 200
        width = 400
        x = (self.load.winfo_screenwidth() // 2) - (width // 2)
        y = (self.load.winfo_screenheight() // 4) - (height // 4)
        self.load.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.load.config(bg="white")
        self.load.resizable(False, False)
        self.img2 = Image.open("images\\load.png")
        self.img2 = self.img2.resize((400, 200))
        self.foto1 = ImageTk.PhotoImage(self.img2)
        self.page1 = Canvas(self.load, width=self.load.winfo_screenwidth(),
                            height=self.load.winfo_screenheight(),
                            bg="black", highlightthickness=0, borderwidth=0)
        self.page1.place(x=0, y=0)
        self.page1.create_image(0, 0, anchor='nw', image=self.foto1)


class App(tkinter.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("App")
        self.loading_screen = LoadingScreen(self)  # Kirim instance tk.Toplevel ke LoadingScreen
        self.withdraw()
        self.loading_thread = threading.Thread(target=self.simulate_loading)
        self.loading_thread.start()

    def simulate_loading(self):
        import time
        time.sleep(5)
        self.show_main_menu()

    def show_main_menu(self):
        main_menu_window = Toplevel(self)
        Mainmenu(main_menu_window)
        main_menu_window.deiconify()
        main_menu_window.rowconfigure(0, weight=1)
        main_menu_window.columnconfigure(0, weight=1)
        height = 720
        width = 1280
        x = (main_menu_window.winfo_screenwidth() // 2) - (width // 2)
        y = (main_menu_window.winfo_screenheight() // 4) - (height // 4)
        main_menu_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        main_menu_window.config(bg="white")
        main_menu_window.attributes("-fullscreen", True)
        self.loading_screen.load.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
