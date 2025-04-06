from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import articlemenu
import sqlite3
import login2
from CenterWin import center
from datetime import datetime
import math
import meditate





def openarticle():
    win = CTkToplevel()
    articlemenu.ArticleSorterApp(win)
    win.deiconify()
    win.lift()
    win.focus_force()
    win.attributes('-topmost', True)
    win.after(1, lambda: win.attributes('-topmost', False))

    def keep_on_top():
        win.lift()
        win.after(100, keep_on_top)

    keep_on_top()

def openmeditasi():
    win = CTkToplevel()
    meditate.Meditation(win)
    win.deiconify()
    win.lift()
    win.focus_force()
    win.attributes('-topmost', True)
    win.after(1, lambda: win.attributes('-topmost', False))

    def keep_on_top():
        win.lift()
        win.after(100, keep_on_top)

    keep_on_top()


class Mainmenu:
    def __init__(self, mainmenu):
        self.mainmenu = mainmenu
        self.mainmenu.rowconfigure(0, weight=1)
        self.mainmenu.columnconfigure(0, weight=1)
        height = 720
        width = 1280
        x = (mainmenu.winfo_screenwidth() // 2) - (width // 2)
        y = (mainmenu.winfo_screenheight() // 4) - (height // 4)
        self.mainmenu.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.mainmenu.config(bg="white")
        self.mainmenu.attributes("-fullscreen", True)
        self.mainmenu.bind("<Escape>", self.toggle_fullscreen)
        self.mainmenu.bind("<Double-Button-1>", self.toggle_fullscreen)

        def exitt2():
            sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=self.mainmenu, )
            if sure:
                self.mainmenu.destroy()
        self.mainmenu.protocol("WM_DELETE_WINDOW", exitt2)
        self.img2 = Image.open("images\\he2.png")
        self.img2 = self.img2.resize((mainmenu.winfo_screenwidth(), mainmenu.winfo_screenheight()))
        self.foto1 = ImageTk.PhotoImage(self.img2)
        self.canva1 = Canvas(self.mainmenu, width=mainmenu.winfo_screenwidth(), height=mainmenu.winfo_screenheight(),
                             bg="black", highlightthickness=0, borderwidth=0)
        self.canva1.place(x=0, y=0)
        self.canva1.create_image(0, 0, anchor='nw', image=self.foto1)

        self.getlogininfo()

        def scroll_to_top():
            self.scrframe._parent_canvas.yview_moveto(0)

        def home_command():
            scroll_to_top()

        def on_hoverhome(event):
            self.home_button.configure(text_color="#EAAA9E")
            self.home_button.configure(font=("Arial", 19, 'bold'))

        def on_leavehome(event):
            self.home_button.configure(text_color="white")
            self.home_button.configure(font=("Arial", 17, 'bold'))

        self.home_button = CTkButton(self.canva1,
                                     text="home",
                                     bg_color="black",
                                     fg_color="black",
                                     text_color="white",
                                     font=("Arial", 17, 'bold'),
                                     width=140,
                                     height=50,
                                     corner_radius=10,
                                     hover_color="black",
                                     command=home_command)
        self.home_button.place(x=800, y=27)

        self.home_button.bind("<Enter>", on_hoverhome)
        self.home_button.bind("<Leave>", on_leavehome)

        def on_hoversch(event):
            schedule_button.configure(text_color="#EAAA9E")
            schedule_button.configure(font=("Poppins", 19, 'bold'))

        def on_leavesch(event):
            schedule_button.configure(text_color="white")
            schedule_button.configure(font=("Poppins", 17, 'bold'))

        schedule_button = CTkButton(self.canva1,
                                    text="schedule",
                                    bg_color="black",
                                    fg_color="black",
                                    text_color="white",
                                    font=("Poppins", 17, 'bold'),
                                    width=140,
                                    height=50,
                                    corner_radius=10,
                                    hover_color="#767676",
                                    hover=False,
                                    command=self.schedulepage
                                    )
        schedule_button.place(x=950, y=27)
        schedule_button.bind("<Enter>", on_hoversch)
        schedule_button.bind("<Leave>", on_leavesch)

        def on_hoverabo(event):
            aboutus_button.configure(text_color="#EAAA9E")
            aboutus_button.configure(font=("Poppins", 19, 'bold'))

        def on_leaveabo(event):
            aboutus_button.configure(text_color="white")
            aboutus_button.configure(font=("Poppins", 17, 'bold'))

        aboutus_button = CTkButton(self.canva1,
                                   text="Activity",
                                   bg_color="black",
                                   fg_color="black",
                                   text_color="white",
                                   font=("Poppins", 17, 'bold'),
                                   width=140,
                                   height=50,
                                   corner_radius=10,
                                   hover_color="#767676",
                                   hover=False,
                                   command=self.activiti

                                   )
        aboutus_button.place(x=1100, y=27)
        aboutus_button.bind("<Enter>", on_hoverabo)
        aboutus_button.bind("<Leave>", on_leaveabo)

        profilimg = Image.open("images\\logout.png")
        profilimg = profilimg.resize((60,60))
        self.profilfoto = ImageTk.PhotoImage(profilimg)

        self.profilbutton = Button(self.canva1,
                                   text="",
                                   width=100,
                                   height=60,
                                   image=self.profilfoto,
                                   bg="black",
                                   border=False,
                                   command=self.logout,
                                   activebackground="black")
        self.profilbutton.place(x=1250, y=19)



        self.scrframe = CTkScrollableFrame(self.mainmenu,
                                           orientation="vertical",
                                           width=mainmenu.winfo_screenwidth(),
                                           height=700,
                                           fg_color='black',
                                           bg_color='black',
                                           )
        self.scrframe.place(x=0, y=89)

        self.homebg = Image.open('images\\homebg1.png')
        self.homebg = self.homebg.resize((mainmenu.winfo_screenwidth(), mainmenu.winfo_screenheight()))
        self.photos = ImageTk.PhotoImage(self.homebg)
        self.canva = Canvas(self.scrframe, width=mainmenu.winfo_screenwidth(), height=mainmenu.winfo_screenheight(),
                            bg="black", highlightthickness=0)
        self.canva.pack()
        self.canva.create_image(0, 0, anchor='nw', image=self.photos)


        self.fiturimg = Image.open("images\\bg.png")
        self.fiturimg = self.fiturimg.resize((mainmenu.winfo_screenwidth(), mainmenu.winfo_screenheight()))
        self.fiturbg = ImageTk.PhotoImage(self.fiturimg)
        self.med_bg = Canvas(self.scrframe, width=mainmenu.winfo_screenwidth(), height=mainmenu.winfo_screenheight(),
                             bg="black", highlightthickness=0, )
        self.med_bg.pack(pady=0, fill='both', expand=True)
        self.med_bg.create_image(0, 0, anchor='nw', image=self.fiturbg)

        def on_enter(e):
            widget11_button.config(image=self.widget11_img_hover)

        def on_leave(e):
            widget11_button.config(image=self.widget11_img_bg)

        widget11_img = Image.open("images\\5 (1).png")
        widget11_img_hover = Image.open("images\\5 (2).png")
        widget11_img = widget11_img.resize((1100, 720))
        widget11_img_hover = widget11_img_hover.resize((1100, 720))
        self.widget11_img_bg = ImageTk.PhotoImage(widget11_img)
        self.widget11_img_hover = ImageTk.PhotoImage(widget11_img_hover)

        widget11_button = Button(self.med_bg, image=self.widget11_img_bg, width=400, height=600, border=FALSE,
                                bg="black", command=openarticle,activebackground="black")
        widget11_button.place(x=10, y=0)

        widget11_button.bind("<Enter>", on_enter)
        widget11_button.bind("<Leave>", on_leave)

        def on_enter(e):
            widget12_button.config(image=self.widget12_img_hover)

        def on_leave(e):
            widget12_button.config(image=self.widget12_img_bg)

        widget12_img = Image.open("images\\5 (3).png")
        widget12_img_hover = Image.open("images\\5 (4).png")
        widget12_img = widget12_img.resize((1100, 720))
        widget12_img_hover = widget12_img_hover.resize((1100, 720))
        self.widget12_img_bg = ImageTk.PhotoImage(widget12_img)
        self.widget12_img_hover = ImageTk.PhotoImage(widget12_img_hover)

        widget12_button = Button(self.med_bg, image=self.widget12_img_bg, width=400, height=600, border=FALSE,
                                bg="black",activebackground="black" )
        widget12_button.place(x=450, y=0)

        widget12_button.bind("<Enter>", on_enter)
        widget12_button.bind("<Leave>", on_leave)

        def on_enter(e):
            widget13_button.config(image=self.widget13_img_hover)

        def on_leave(e):
            widget13_button.config(image=self.widget13_img_bg)

        widget13_img = Image.open("images\\5 (5).png")
        widget13_img_hover = Image.open("images\\5 (7).png")
        widget13_img = widget13_img.resize((1100, 720))
        widget13_img_hover = widget13_img_hover.resize((1100, 720))
        self.widget13_img_bg = ImageTk.PhotoImage(widget13_img)
        self.widget13_img_hover = ImageTk.PhotoImage(widget13_img_hover)

        widget13_button = Button(self.med_bg, image=self.widget13_img_bg, width=400, height=600, border=FALSE,
                                bg="black",command=openmeditasi )
        widget13_button.place(x=890, y=0)

        widget13_button.bind("<Enter>", on_enter)
        widget13_button.bind("<Leave>", on_leave)


    def logout(self):
        tampilkan_info_login("customer1")
        logout("customer1")
        tampilkan_info_login("customer1")
        win = Toplevel()
        login2.Login(win)
        self.mainmenu.withdraw()
        win.deiconify()


    def toggle_fullscreen(self, event=None):
        is_fullscreen = self.mainmenu.attributes("-fullscreen")
        self.mainmenu.attributes("-fullscreen", not is_fullscreen)

    def activiti(self):
        self.activities = Toplevel(self.mainmenu)
        self.activities.title("Sign Up")
        center.tengah_layar(self.activities, 400, 600)
        self.activities.resizable(False, False)
        self.activities.rowconfigure(0, weight=1)
        self.activities.columnconfigure(0, weight=1)
        height = 650
        width = 960
        x = (self.activities.winfo_screenwidth() // 2) - (width // 2)
        y = (self.activities.winfo_screenheight() // 4) - (height // 4)
        self.activities.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        self.image2 = Image.open("images\\activiti.png")
        self.image2 = self.image2.resize((960, 650))
        self.photo2 = ImageTk.PhotoImage(self.image2)
        self.canvas1 = Canvas(self.activities, width=1366, height=768, bg="#C70039")
        self.canvas1.pack()
        self.canvas1.create_image(0, 0, anchor='nw', image=self.photo2)

        self.labelnama = Label(self.activities,text=self.getlogininfo(),font=('Arial',14,'normal'),bg="#222222",fg="#687BCB")
        self.labelnama.place(x=690, y=373)

        conn = sqlite3.connect('database/fitness.db')
        cursor = conn.cursor()

        # Mendapatkan data dari database
        cursor.execute("SELECT * FROM data_olahraga ORDER BY hari DESC LIMIT 1")  # Mengambil data terakhir
        data = cursor.fetchone()

        tanggal = datetime.strptime(data[1], '%Y-%m-%d').strftime('%A')
        kalori = round(data[3],2)
        detik = round(data[4])

        # Label untuk menampilkan data
        hari_label = Label(self.activities, text=tanggal, font=("Arial", 12), bg="#222222",fg="#D9D9D9")
        hari_label.place(x=330, y=245)

        total_kalori_label = Label(self.activities, text=f"{kalori} kcal", font=("Arial", 12),
                                   bg="#222222",fg="#D9D9D9")
        total_kalori_label.place(x=330, y=340)

        lama_latihan_label = Label(self.activities, text=f"{detik} detik", font=("Arial", 12),
                                   bg="#222222",fg="#D9D9D9")
        lama_latihan_label.place(x=330, y=290)

        olahraga_terakhir_label = Label(self.activities, text=data[5], font=("Arial", 12),
                                        bg="#222222",fg="#D9D9D9")
        olahraga_terakhir_label.place(x=330, y=390)



    def getlogininfo(self):
        conn = sqlite3.connect("database/fitness.db")
        c = conn.cursor()
        c.execute("SELECT nama_lengkap FROM pengguna WHERE status_login = 1")
        customer_info = str(c.fetchone()[0])
        print(customer_info)
        conn.commit()
        conn.close()

        return customer_info

    def openschedulefisik(self):
        import os
        interpret = "D:\pythonProject1\Scripts\python.exe"
        filepath = "D:\pythonProject1\\fisik.py"
        os.system(interpret + " " +filepath )
    def openschedulesensor(self):
        import os
        interpret = "D:\pythonProject1\Scripts\python.exe"
        filepath = "D:\pythonProject1\\sensoric.py"
        os.system(interpret + " " +filepath )
    def openscheduleintelec(self):
        import os
        interpret = "D:\pythonProject1\Scripts\python.exe"
        filepath = "D:\pythonProject1\\intellectual.py"
        os.system(interpret + " " +filepath )

    def schedulepage(self):
        conn = sqlite3.connect("database/fitness.db")
        c = conn.cursor()
        c.execute("SELECT keterbatasan_fisik FROM pengguna WHERE status_login = 1")
        disabel_info = str(c.fetchone()[0])

        if disabel_info == "Keterbatasan Mobilitas" :
            self.openschedulefisik()
        if disabel_info == "Intellectual Disabled":
            self.openscheduleintelec()
        if disabel_info == "Sensoric" :
            self.openschedulesensor()

def get_login_info():
    connection = sqlite3.connect("database/fitness.db")
    cursor = connection.cursor()

    # Ambil informasi login berdasarkan username
    cursor.execute("SELECT status_login FROM pengguna WHERE status_login = 1")
    connection.commit()
    customer_info = cursor.fetchone()
    print(customer_info)
    connection.close()
    return customer_info

def tampilkan_info_login(status):
    # Tampilkan informasi bahwa pengguna sedang login beserta waktu login
    login_info = get_login_info()
    if login_info:
        status = login_info
        if status:
            print(f"Pengguna aktif .")
        else:
            print(f"Pengguna  tidak sedang login.")
    else:
        print(f"Tidak ada pengguna yang login.")

def logout(status):
    # Logout pengguna dengan mengupdate status login menjadi 0
    connection = sqlite3.connect("database/fitness.db")
    cursor = connection.cursor()

    # Logout customer
    cursor.execute("UPDATE pengguna SET status_login = 0 WHERE status_login = 1")
    connection.commit()
    connection.close()

if __name__ == "__main__":
    root = Tk()
    Mainmenu(root)
    root.mainloop()
