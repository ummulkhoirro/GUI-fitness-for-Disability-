import tkinter as tk
from tkinter import ttk

import customtkinter
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox
from CenterWin import center
from customtkinter import CTkButton, CTkEntry, CTkLabel, CTkImage, CTkFont
import login2


class HoverButton(tk.Button):
    def __init__(self, app, master=None, **kwargs):
        self.defaultBackground = kwargs.pop('background', 'SystemButtonFace')
        self.hoverImage = kwargs.pop('hoverimage', None)
        self.defaultImage = kwargs.pop('image', None)
        self.value = kwargs.pop('value', None)  # Add a value to identify the button
        self.clicked = False
        self.app = app  # Store the reference to the main application
        super().__init__(master, **kwargs)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<Button-1>", self.on_click)

    def on_enter(self, e):
        if not self.clicked:
            if self.hoverImage:
                self.configure(image=self.hoverImage)

    def on_leave(self, e):
        if not self.clicked:
            if self.defaultImage:
                self.configure(image=self.defaultImage)

    def on_click(self, e):
        self.app.set_previous_hovered(self)
        self.clicked = True
        if self.hoverImage:
            self.configure(image=self.hoverImage)
        # self.app.update_selected_value(self.value)  # Update the selected value in the main application

class App(tk.Toplevel):
    def __init__(self,master=None):
        super().__init__(master)
        # self.acc = signup1.Signup(self)
        self.previous_hovered_button = None
        self.selected_value = None  # Add an attribute to store the selected value
        self.title("Sign Up")
        self.selected_gender = None
        self.selected_tujuan = None
        self.selected_disabel = None
        self.age = None
        self.height = None
        self.weight = None
        self.bmi = None
        center.tengah_layar(self, 400, 600)
        self.resizable(False, False)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        height = 650
        width = 950
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 4) - (height // 4)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        self.data = {
            "email": tk.StringVar(),
            "first_name": tk.StringVar(),
            "last_name": tk.StringVar(),
            "password": tk.StringVar(),
            "confirm_password": tk.StringVar(),
        }

        self.frame1 = tk.Frame(self)
        self.frame2 = tk.Frame(self)
        self.kelamin = tk.Frame(self)
        self.tujuan = tk.Frame(self)
        self.disabel = tk.Frame(self)
        self.umur = tk.Frame(self)
        self.tb = tk.Frame(self)
        self.bb = tk.Frame(self)
        self.imt = tk.Frame(self)

        for frame in (self.kelamin, self.tujuan, self.disabel, self.umur, self.tb, self.bb, self.imt,self.frame1, self.frame2):
            frame.grid(row=0, column=0, sticky='nsew')

        self.showframe1()
        #
        # self.frame1_bg_Img = Image.open("images\\signup.png").resize((950, 650))
        # self.foto = ImageTk.PhotoImage(self.frame1_bg_Img)
        # canvas = tk.Canvas(self.frame1, width=950, height=650)
        # canvas.place(x=0, y=0)
        # canvas.create_image(0, 0, image=self.foto, anchor='nw')



        self.img2 = Image.open("images\\signup3.png")
        self.img2 = self.img2.resize((950, 650))
        self.foto1 = ImageTk.PhotoImage(self.img2)
        self.canva1 = tk.Canvas(self.frame1, width=950, height=650,
                             bg="black", highlightthickness=0, borderwidth=0)
        self.canva1.place(x=0, y=0)
        self.canva1.create_image(0, 0, anchor='nw', image=self.foto1)

        no_acc_label = CTkButton(self.frame1,
                                 text="Have an account ?",
                                 anchor='c',
                                 fg_color='white',
                                 bg_color='white',
                                 height=30,
                                 hover_color='#e9e8e8',
                                 font=("Helvetica", 13),
                                 text_color="#291C4F",
                                 border_width=0, )
        no_acc_label.place(x=470, y=57)
        sign_up_font = CTkFont(family="DM Sans", size=13, underline=True)
        sign_up_button = tk.Button(self.frame1, text='sign in', cursor="hand2",
                                font=sign_up_font,
                                bg="white", fg="blue", borderwidth=0, activebackground='white',
                                command=self.button_click_signin)
        sign_up_button.place(x=593, y=60)


        self.email_entry = CTkEntry(self.frame1,
                                    placeholder_text="Email Address",
                                    placeholder_text_color="black",
                                    width=400,
                                    height=50,
                                    corner_radius=0,
                                    font=("Poppins", 13),
                                    bg_color="white",
                                    fg_color="#D9D9D9",
                                    text_color="black",
                                    border_width=1,
                                    border_color="white",
                                    textvariable=self.data["email"]
                                    )
        self.email_entry.place(x=470, y=110)

        email_label = tk.Label(self.frame1,
                            text="Email Address",
                            font=("Arial",8),
                            fg="black",
                            borderwidth=0,
                            bg="white")
        email_label.place(x=490, y=95)

        self.firstname_entry = CTkEntry(self.frame1,
                                        placeholder_text_color="black",
                                        width=400,
                                        height=50,
                                        corner_radius=0,
                                        font=("Arial", 13, "italic"),
                                        bg_color="white",
                                        fg_color="#D9D9D9",
                                        text_color="black",
                                        border_width=1,
                                        border_color="white",
                                        textvariable=self.data["first_name"])
        self.firstname_entry.place(x=470, y=190)

        first_label = tk.Label(self.frame1,
                            text="First Name",
                            font=("Arial", 8),
                            fg="black",
                            borderwidth=0,
                            bg="white")
        first_label.place(x=490, y=175)

        self.lastname_entry = CTkEntry(self.frame1,
                                       width=400,
                                       height=50,
                                       corner_radius=0,
                                       font=("Arial", 13, "italic"),
                                       bg_color="white",
                                       fg_color="#D9D9D9",
                                       text_color="black",
                                       border_width=1,
                                       border_color="white",
                                       textvariable=self.data["last_name"])
        self.lastname_entry.place(x=470, y=270)

        last_label = tk.Label(self.frame1,
                           text="Last Name",
                           font=("Arial", 8),
                           fg="black",
                           borderwidth=0,
                           bg="white")
        last_label.place(x=490, y=255)

        self.password_entry = CTkEntry(self.frame1,
                                       width=400,
                                       height=50,
                                       corner_radius=0,
                                       font=("Arial", 13, "italic"),
                                       bg_color="white",
                                       fg_color="#D9D9D9",
                                       text_color="black",
                                       border_width=1,
                                       border_color="white",
                                       textvariable=self.data["password"])
        self.password_entry.place(x=470, y=350)

        self.password_entry.bind("<KeyRelease>", self.check_password_strength)


        password_label = tk.Label(self.frame1,
                               text="Password",
                               font=("Arial", 8),
                               fg="black",
                               borderwidth=0,
                               bg="white")
        password_label.place(x=490, y=335)

        self.password_requirements = [
            "At least 8 characters",
            "Lower case letters (a-z)",
            "Upper case letters (A-Z)",
            "Numbers (0-9)",
            "Special characters (e.g. !@#$%^&*)"
        ]
        self.requirements_labels = []
        for i, requirement in enumerate(self.password_requirements):
            label = ttk.Label(self.frame1, text=requirement, foreground="red", background="white", font=("Arial", 8))
            label.place(x=480, y=410 + i * 20)
            self.requirements_labels.append(label)
        self.cpass_entry = CTkEntry(self.frame1,
                                    width=400,
                                    height=50,
                                    corner_radius=0,
                                    font=("Arial", 13, "italic"),
                                    bg_color="white",
                                    fg_color="#D9D9D9",
                                    text_color="black",
                                    border_width=1,
                                    border_color="white",
                                    textvariable=self.data["confirm_password"])
        self.cpass_entry.place(x=470, y=530)
        cpassword_label = tk.Label(self.frame1,
                                text="Confirm Password",
                                font=("Arial", 8, ),
                                fg="black",
                                borderwidth=0,
                                bg="white")
        cpassword_label.place(x=490, y=515)

        createacc_b = CTkButton(self.frame1,
                                text="Create Account",
                                width=250,
                                height=40,
                                corner_radius=10,
                                font=("Arial", 14, "bold"),
                                bg_color="white",
                                fg_color="black",
                                text_color="white",
                                border_color="black",
                                hover_color="#4D4B4B",

                                command=self.create_account)
        createacc_b.place(x=540,y=600)

        self.error_label = ttk.Label(self.frame1, text="", foreground="red", background="white")
        self.error_label.place(x=480, y=70)

        self.img = Image.open("images\\signup3.png")
        self.img = self.img.resize((950, 650))
        self.foto = ImageTk.PhotoImage(self.img)
        self.canvas = tk.Canvas(self.kelamin, width=950, height=650,
                                bg="black", highlightthickness=0, borderwidth=0)
        self.canvas.place(x=0, y=0)
        self.canvas.create_image(0, 0, anchor='nw', image=self.foto)

        gender1icon = ImageTk.PhotoImage(Image.open("images/gender (1).png").resize((730, 480)))
        gender1iconh = ImageTk.PhotoImage(Image.open("images/gender (3).png").resize((730, 480)))

        gendericon = ImageTk.PhotoImage(Image.open("images/gender (2).png").resize((730, 480)))
        gendericonh = ImageTk.PhotoImage(Image.open("images/gender (4).png").resize((730, 480)))

        self.gender1_button = HoverButton(self, self.kelamin, image=gender1icon, hoverimage=gender1iconh, width=150, height=400,
                                          border=tk.FALSE, bg='white', activebackground="white",command=lambda: self.update_gender("Laki-laki"))
        self.gender1_button.place(x=290, y=160)

        self.gender_button = HoverButton(self, self.kelamin, image=gendericon, hoverimage=gendericonh, width=150, height=400,
                                         border=tk.FALSE, bg='white', activebackground="white",command=lambda: self.update_gender("Perempuan"))
        self.gender_button.place(x=530, y=160)

        button_next = CTkButton(self.kelamin, text="Berikutnya", bg_color="white", font=("Helvetica", 17, 'bold'),
                                fg_color="#FF5C51", text_color="white", width=130, height=60, command=self.showtujuan)
        button_next.place(x=700, y=580)

        self.img = Image.open("images\\reg (2).png")
        self.img = self.img.resize((950, 650))
        self.foto = ImageTk.PhotoImage(self.img)
        self.canva = tk.Canvas(self.tujuan, width=950, height=650,
                               bg="black", highlightthickness=0, borderwidth=0)
        self.canva.place(x=0, y=0)
        self.canva.create_image(0, 0, anchor='nw', image=self.foto)

        back_button_img = CTkImage(Image.open("images\\back.png"), size=(30, 20))
        back_button = CTkButton(self.tujuan, image=back_button_img,
                                bg_color="white", text="", border_width=0,
                                fg_color="white", command=self.showgender1,
                                width=30, hover=False)
        back_button.place(x=0, y=0)

        tujuanicon = ImageTk.PhotoImage(Image.open("images/tujuan (1).png").resize((650, 450)))
        tujuaniconh = ImageTk.PhotoImage(Image.open("images/tujuan (6).png").resize((650, 450)))

        tujuan1icon = ImageTk.PhotoImage(Image.open("images/tujuan (2).png").resize((650, 450)))
        tujuan1iconh = ImageTk.PhotoImage(Image.open("images/tujuan (5).png").resize((650, 450)))

        tujuan2icon = ImageTk.PhotoImage(Image.open("images/tujuan (3).png").resize((650, 450)))
        tujuan2iconh = ImageTk.PhotoImage(Image.open("images/tujuan (4).png").resize((650, 450)))

        self.tujuan_button = HoverButton(self, self.tujuan, image=tujuanicon, hoverimage=tujuaniconh, width=400,
                                         height=130,
                                         border=tk.FALSE, bg='white', activebackground="white",command=lambda: self.update_tujuan("Menurunkan bb"))
        self.tujuan_button.place(x=100, y=200)

        self.tujuan1_button = HoverButton(self, self.tujuan, image=tujuan1icon, hoverimage=tujuan1iconh, width=400,
                                          height=130,
                                          border=tk.FALSE, bg='white', activebackground="white",command=lambda: self.update_tujuan("tetap bugar"))
        self.tujuan1_button.place(x=100, y=345)
        self.tujuan2_button = HoverButton(self, self.tujuan, image=tujuan2icon, hoverimage=tujuan2iconh, width=400,
                                          height=130,
                                          border=tk.FALSE, bg='white', activebackground="white", command=lambda: self.update_tujuan("Menambah bb"))
        self.tujuan2_button.place(x=100, y=500)

        button_next = CTkButton(self.tujuan, text="Berikutnya", bg_color="white", font=("Helvetica", 17, 'bold'),
                                fg_color="#FF5C51", text_color="white", width=180, height=60, command=self.showdisabel)
        button_next.place(x=700, y=580)

        self.img3 = Image.open("images\\reg (3).png")
        self.img3 = self.img3.resize((950, 650))
        self.foto3 = ImageTk.PhotoImage(self.img3)
        self.canva3 = tk.Canvas(self.disabel, width=950, height=650,
                               bg="black", highlightthickness=0, borderwidth=0)
        self.canva3.place(x=0, y=0)
        self.canva3.create_image(0, 0, anchor='nw', image=self.foto3)

        back_button_img = CTkImage(Image.open("images\\back.png"), size=(30, 20))
        back_button = CTkButton(self.disabel, image=back_button_img,
                                bg_color="white", text="", border_width=0,
                                fg_color="white", command=self.showtujuan,
                                width=30, hover=False)
        back_button.place(x=0, y=0)

        disabelicon = ImageTk.PhotoImage(Image.open("images/disabel (1).png").resize((550, 450)))
        disabeliconh = ImageTk.PhotoImage(Image.open("images/disabel (5).png").resize((550, 450)))

        disabel1icon = ImageTk.PhotoImage(Image.open("images/disabel (2).png").resize((550, 450)))
        disabel1iconh = ImageTk.PhotoImage(Image.open("images/disabel (6).png").resize((550, 450)))

        disabel2icon = ImageTk.PhotoImage(Image.open("images/disabel (3).png").resize((550, 450)))
        disabel2iconh = ImageTk.PhotoImage(Image.open("images/disabel (7).png").resize((550, 450)))

        disabel3icon = ImageTk.PhotoImage(Image.open("images/disabel (4).png").resize((550, 450)))
        disabel3iconh = ImageTk.PhotoImage(Image.open("images/disabel (8).png").resize((550, 450)))

        self.disabel_button = HoverButton(self, self.disabel, image=disabelicon, hoverimage=disabeliconh, width=350,
                                         height=130,
                                         border=tk.FALSE, bg='white', activebackground="white", command=lambda: self.update_disabel("Keterbatasan Mobilitas"))
        self.disabel_button.place(x=150, y=230)

        self.disabel1_button = HoverButton(self, self.disabel, image=disabel1icon, hoverimage=disabel1iconh, width=350,
                                          height=130,
                                          border=tk.FALSE, bg='white', activebackground="white",command=lambda: self.update_disabel("Intellectual Disabled"))
        self.disabel1_button.place(x=500, y=230)
        self.disabel2_button = HoverButton(self, self.disabel, image=disabel2icon, hoverimage=disabel2iconh, width=350,
                                          height=130,
                                          border=tk.FALSE, bg='white', activebackground="white",command=lambda: self.update_disabel("Sensoric"))
        self.disabel2_button.place(x=150, y=390)

        self.disabel3_button = HoverButton(self, self.disabel, image=disabel3icon, hoverimage=disabel3iconh, width=350,
                                          height=130,
                                          border=tk.FALSE, bg='white', activebackground="white",command=lambda: self.update_disabel("Lainnya"))
        self.disabel3_button.place(x=500, y=390)

        button_next = CTkButton(self.disabel, text="Berikutnya", bg_color="white", font=("Helvetica", 17, 'bold'),
                                fg_color="#FF5C51", text_color="white", width=180, height=60, command=self.showumur)
        button_next.place(x=700, y=580)

        self.img4 = Image.open("images\\reg (4).png")
        self.img4 = self.img4.resize((950, 650))
        self.foto4 = ImageTk.PhotoImage(self.img4)
        self.canva4 = tk.Canvas(self.umur, width=950, height=650,
                                bg="black", highlightthickness=0, borderwidth=0)
        self.canva4.place(x=0, y=0)
        self.canva4.create_image(0, 0, anchor='nw', image=self.foto4)

        back_button_img = CTkImage(Image.open("images\\back.png"), size=(30, 20))
        back_button = CTkButton(self.umur, image=back_button_img,
                                bg_color="white", text="", border_width=0,
                                fg_color="white", command=self.showdisabel,
                                width=30, hover=False)
        back_button.place(x=0, y=0)

        vcmd = (self.register(self.validate_number), '%P')
        self.entry_umur =CTkEntry(self.umur, bg_color="white",width=156,height=130,text_color="black",
                              fg_color="white",font=("Arial",76,"normal"),validate='key', validatecommand=vcmd,
                             border_color="black",placeholder_text="Masukan Umur Anda",placeholder_text_color="black")
        self.entry_umur.place(x=390 , y=289)

        button_next = CTkButton(self.umur, text="Berikutnya", bg_color="white", font=("Helvetica", 17, 'bold'),
                                fg_color="#FF5C51", text_color="white", width=130, height=60, command=self.get_age_value)
        button_next.place(x=700, y=580)

        self.img5 = Image.open("images\\reg (5).png")
        self.img5 = self.img5.resize((950, 650))
        self.foto5 = ImageTk.PhotoImage(self.img5)
        self.canva5 = tk.Canvas(self.tb, width=950, height=650,
                                bg="black", highlightthickness=0, borderwidth=0)
        self.canva5.place(x=0, y=0)
        self.canva5.create_image(0, 0, anchor='nw', image=self.foto5)

        back_button_img = CTkImage(Image.open("images\\back.png"), size=(30, 20))
        back_button = CTkButton(self.tb, image=back_button_img,
                                bg_color="white", text="", border_width=0,
                                fg_color="white", command=self.showumur,
                                width=30, hover=False)
        back_button.place(x=0, y=0)

        self.entry_height = CTkEntry(self.tb, bg_color="white", width=156, height=130, text_color="black",
                                   fg_color="white", font=("Arial", 76, "normal"), validate='key', validatecommand=vcmd,
                                   border_color="black",)
        self.entry_height.place(x=390, y=250)

        button_next = CTkButton(self.tb, text="Berikutnya", bg_color="white", font=("Helvetica", 17, 'bold'),
                                fg_color="#FF5C51", text_color="white", width=130, height=60,
                                command=self.get_heightcm_value)
        button_next.place(x=700, y=580)

        self.img6 = Image.open("images\\reg (6).png")
        self.img6 = self.img6.resize((950, 650))
        self.foto6 = ImageTk.PhotoImage(self.img6)
        self.canva6 = tk.Canvas(self.bb, width=950, height=650,
                                bg="black", highlightthickness=0, borderwidth=0)
        self.canva6.place(x=0, y=0)
        self.canva6.create_image(0, 0, anchor='nw', image=self.foto6)

        back_button_img = CTkImage(Image.open("images\\back.png"), size=(30, 20))
        back_button = CTkButton(self.bb, image=back_button_img,
                                bg_color="white", text="", border_width=0,
                                fg_color="white", command=self.showtb,
                                width=30, hover=False)
        back_button.place(x=0, y=0)

        self.entry_weight = CTkEntry(self.bb, bg_color="white", width=156, height=130, text_color="black",
                                     fg_color="white", font=("Arial", 76, "normal"), validate='key',
                                     validatecommand=vcmd,
                                     border_color="black", )
        self.entry_weight.place(x=390, y=250)

        button_next = CTkButton(self.bb, text="Berikutnya", bg_color="white", font=("Helvetica", 17, 'bold'),
                                fg_color="#FF5C51", text_color="white", width=130, height=60,
                                command=self.get_weight_value)
        button_next.place(x=700, y=580)

        self.img7 = Image.open("images\\reg (9).png")
        self.img7 = self.img7.resize((950, 650))
        self.foto7 = ImageTk.PhotoImage(self.img7)
        self.canva7 = tk.Canvas(self.imt, width=950, height=650,
                                bg="black", highlightthickness=0, borderwidth=0)
        self.canva7.place(x=0, y=0)
        self.canva7.create_image(0, 0, anchor='nw', image=self.foto7)

        back_button_img = CTkImage(Image.open("images\\back.png"), size=(30, 20))
        back_button = CTkButton(self.imt, image=back_button_img,
                                bg_color="white", text="", border_width=0,
                                fg_color="white", command=self.showbb,
                                width=30, hover=False)
        back_button.place(x=0, y=0)

        self.bmi_label = tk.Label(self.imt , text="299", font=("Helvetica",18,),background="white", fg="black")
        self.bmi_label.place(x=355, y=230)

        self.kalori_label = tk.Label(self.imt, text="299", font=("Helvetica", 18,), background="white",
                                  fg="black")
        self.kalori_label.place(x=355, y=320)

        self.air_label = tk.Label(self.imt, text="299", font=("Helvetica", 18,), background="white",
                                  fg="black")
        self.air_label.place(x=355, y=420)

        self.bmitier = tk.Label(self.imt, text="299", font=("Helvetica", 13,), background="white",
                                  fg="black")
        self.bmitier.place(x=640,  y=220)

        self.labelbmicapt = CTkLabel(self.imt, corner_radius=10, bg_color="white", fg_color="grey",
                                     width=300, height=90, text="")
        self.labelbmicapt.place(x=285, y=485)

        self.bmicapt =  tk.Label(self.imt, text="299", font=("Helvetica", 13), background="white",
                                  fg="black")
        self.bmicapt.place(x=300, y=500)

        button_next = CTkButton(self.imt, text="Ok", bg_color="white", font=("Helvetica", 17, 'bold'),
                                fg_color="#FF5C51", text_color="white", width=130, height=60,
                                command=self.persondataopen)
        button_next.place(x=700, y=580)


    def validate_number(self, P):
        if P.isdigit() or P == "":
            return True
        else:
            return False

    def update_gender(self, gender):
        self.selected_gender = gender
        print(f"Selected gender: {self.selected_gender}")
        return self.selected_gender

    def update_tujuan(self, tujuan):
        self.selected_tujuan = tujuan
        print(f"tujuan: {self.selected_tujuan}")

    def update_disabel(self, disabel):
        self.selected_disabel =disabel
        print(f"Disability: {self.selected_disabel}")

    def get_age_value(self):
        age_value = self.entry_umur.get()
        if not age_value:
            self.entry_umur.configure(border_color="red")
            messagebox.showerror("Error", "Umur tidak boleh kosong")
        else:
            self.entry_umur.configure(border_color="white")
            self.age = age_value
            print(f"Umur : {self.age} Tahun")
            self.showtb()

    def get_heightcm_value(self):
        height_value = self.entry_height.get()
        Height = height_value
        if not height_value:
            self.entry_height.configure(border_color="red")
            messagebox.showerror("Error", "Field tidak boleh kosong")
        else:
            self.entry_height.configure(border_color="white")
            self.height = Height
            print(f"Tinggi badan : {self.height} Cm")
            self.showbb()

    def get_weight_value(self):
        weight_value = self.entry_weight.get()
        weight = weight_value
        if not weight_value:
            self.entry_weight.configure(border_color="red")  # Change border to red
            messagebox.showerror("Error", "Field tidak boleh kosong")
        else:
            self.entry_weight.configure(border_color="white")  # Reset border to original color
            self.weight = weight
            print(f"berat badan : {self.weight} Kg")
            self.showimt()
            self.calculate_bmi()

    def calculate_bmi(self):
        if self.age and self.height and self.weight:
            bmi = self.calculate_bmi_value(float(self.weight), float(self.height) / 100)
            self.bmi_label.config(text=f"{bmi:.2f}")
            if bmi < 18.5:
                self.labelbmicapt.configure(fg_color="#80C0D6")
                self.bmicapt.config(bg="#80C0D6")
            elif 18.5 <= bmi < 24.9:
                self.labelbmicapt.configure(fg_color="#AEEB9F")
                self.bmicapt.config(bg="#AEEB9F")
            elif 25 <= bmi < 29.9:
                self.labelbmicapt.configure(fg_color="#DFD76C")
                self.bmicapt.config(bg="#DFD76C")
            else:
                self.labelbmicapt.configure(bg_color="#C24C4C")
                self.bmicapt.config(bg="#C24C4C")

            kalori = self.calculate_kalori(float(self.weight), float(self.height), int(self.age))
            self.kalori_label.config(text=f"{kalori} Kcal")

            liter_air = self.calculate_liter_air(float(self.weight))
            self.air_label.config(text=f"{liter_air:.2f} Liter")

            bmitier = self.get_bmi_tier(bmi)
            self.bmitier.config(text=bmitier)

            bmicapt = self.get_bmi_caption(bmi)
            self.bmicapt.config(text=bmicapt)

    def calculate_bmi_value(self, weight, height):
        return weight / (height ** 2)

    def calculate_kalori(self, weight, height, age):
        return (10 * weight) + (6.25 * height) - (5 * age) + 5

    def calculate_liter_air(self, weight):
        return weight * 0.033

    def set_previous_hovered(self, button):
        if self.previous_hovered_button:
            self.previous_hovered_button.clicked = False
            if self.previous_hovered_button.defaultImage:
                self.previous_hovered_button.configure(image=self.previous_hovered_button.defaultImage)
        self.previous_hovered_button = button


    def show_warning(self):
        messagebox.showwarning("Warning", "Please select your gender before proceeding.")

    def showframe1(self):
        self.frame1.tkraise()

    def showframe2(self):
        self.frame2.tkraise()

    def showgender1(self):
        self.kelamin.tkraise()

    def showtujuan(self):
        if self.selected_gender is None:
            self.show_warning()
        else:
            self.tujuan.tkraise()


    def showdisabel(self):
        if self.selected_tujuan is None:
            self.show_warning()
        else:
            self.disabel.tkraise()

    def showumur(self):
        if self.selected_disabel is None:
            self.show_warning()
        else:
            self.umur.tkraise()


    def showtb(self):
        if self.age is None:
            self.show_warning()
        else:
            self.tb.tkraise()

    def showbb(self):
        if self.height is None:
            self.show_warning()
        else:
            self.bb.tkraise()
    def showimt(self):
        self.imt.tkraise()

    def get_bmi_caption(self, bmi):
        if bmi < 18.5:
            return "Anda termasuk dalam kategori \nnderweight (Berat Badan Kurang)."
        elif 18.5 <= bmi < 24.9:
            return "Anda termasuk dalam kategori Normal."
        elif 25 <= bmi < 29.9:
            return "Anda termasuk dalam kategori\nOverweight (Berat Badan Berlebih)."
        else:
            return "Anda termasuk dalam kategori \nObesity (Obesitas)."

    def get_bmi_tier(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"
    def create_account(self):
        self.reset_borders()
        self.error_label.config(text="")

        empty_fields = [key for key, var in self.data.items() if not var.get().strip()]
        if empty_fields:
            self.error_label.config(text="Please fill all the fields.")
            for field in empty_fields:
                if field == "first_name":
                    self.firstname_entry.configure(border_color="red")
                elif field == "last_name":
                    self.lastname_entry.configure(border_color="red")
                elif field == "email":
                    self.email_entry.configure(border_color="red")
                elif field == "password":
                    self.password_entry.configure(border_color="red")
                elif field == "confirm_password":
                    self.cpass_entry.configure(border_color="red")
            return

        if self.data["password"].get() != self.data["confirm_password"].get():
            self.error_label.config(text="Passwords do not match.")
            self.password_entry.configure(border_color="red")
            self.cpass_entry.configure(border_color="red")
            return
        self.showgender1()

    def reset_borders(self):
        self.email_entry.configure(border_color="black")
        self.firstname_entry.configure(border_color="black")
        self.lastname_entry.configure(border_color="black")

        self.password_entry.configure(border_color="black")
        self.cpass_entry.configure(border_color="black")



    def check_password_strength(self, event=None):
        password = self.data["password"].get()
        checks = [
            len(password) >= 8,
            any(c.islower() for c in password),
            any(c.isupper() for c in password),
            any(c.isdigit() for c in password),
            any(c in "!@#$%^&*()" for c in password)
        ]

        for check, label in zip(checks, self.requirements_labels):
            if check:
                label.config(foreground="green")
            else:
                label.config(foreground="red")

    def login(self):
        win = customtkinter.CTkToplevel()
        login2.Login(win)
        self.withdraw()
        win.deiconify()

    def button_click_signin(self):
        self.login()



    def persondataopen(self):
        email = self.email_entry.get()
        firstname = self.firstname_entry.get()
        lastname = self.lastname_entry.get()
        fullname = firstname + " " + lastname
        password = self.cpass_entry.get()
        kelamin = self.selected_gender
        tujuan = self.selected_tujuan
        disabel = self.selected_disabel
        umur = int(self.age)
        tb = int(self.height)
        bb = int(self.weight)
        data_list = [email,fullname,password,kelamin,tujuan,disabel,umur,tb,bb]
        print(data_list)
        if all(element is not None for element in data_list):
            conn = sqlite3.connect("database/fitness.db")
            c = conn.cursor()
            c.execute("INSERT INTO pengguna(email,nama_lengkap, password, jenis_kelamin, tujuan, keterbatasan_fisik, umur, tinggi_badan, berat_badan) VALUES(?,?,?,?,?,?,?,?,?)",
                      data_list)
            conn.commit()
            conn.close()


if __name__ == "__main__":
    app = App()
    app.mainloop()


