from tkinter import *
from PIL import Image, ImageTk
from customtkinter import *
from tkinter import ttk
from gtts import gTTS
import playsound
import login2
import persondata
import sqlite3


def tts_signup():
    speech = gTTS(text="THis is Sign Up page", lang='en')
    filepath = "audio\\login.mp3"
    speech.save(filepath)
    try:
        playsound.playsound(filepath)
    except playsound.PlaysoundException:
        print("Error playing audio file")
    finally:
        os.remove(filepath)


def open_signup():
    tts_signup()



class Signup:
    def __init__(self,signup):
        self.master = signup
        self.clicked = False
        self.click_count = 0
        self.master.title("Signup")
        window_width = 400
        window_height = 550
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)
        self.master.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
        self.master.config(bg="white")

        self.data_email = {"email": StringVar}
        self.data = {

            "first_name": StringVar(),
            "last_name": StringVar(),
            "password": StringVar(),
            "confirm_password": StringVar(),
        }

        self.frame1 = Frame(self.master)
        self.frame2 = Frame(self.master)

        for frame in (self.frame1, self.frame2):
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame1()
        # frame1
        self.frame1_bg_Img = Image.open("images\\signup.png").resize((400, 550))
        self.foto = ImageTk.PhotoImage(self.frame1_bg_Img)
        canvas = Canvas(self.frame1, width=400, height=550)
        canvas.pack()
        canvas.create_image(0, 0, image=self.foto, anchor='nw')
        # self.after(100, open_signup())
        self.email_entry = CTkEntry(self.frame1,
                                    placeholder_text="Email Address",
                                    placeholder_text_color="black",
                                    width=330,
                                    height=50,
                                    corner_radius=10,
                                    font=("Poppins", 13),
                                    bg_color="white",
                                    fg_color="white",
                                    text_color="black",
                                    border_width=1,
                                    border_color="black",
                                    textvariable=self.data_email["email"])
        self.email_entry.place(x=35, y=150)

        email_label = Label(self.frame1,
                            text="Email Address",
                            font=("Arial", 10, "bold"),
                            fg="black",
                            borderwidth=0,
                            bg="white")
        email_label.place(x=60, y=140)

        email_entry_b = CTkButton(self.frame1,
                                  text="Continue",
                                  width=330,
                                  height=50,
                                  corner_radius=10,
                                  font=("Arial", 17, "bold"),
                                  bg_color="white",
                                  fg_color="black",
                                  text_color="white",
                                  border_color="black",
                                  hover_color="#4D4B4B",
                                  command=self.continu)
        email_entry_b.place(x=35, y=210)
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
        no_acc_label.place(x=35, y=267)
        sign_up_font = CTkFont(family="DM Sans", size=13, underline=True)
        sign_up_button = Button(self.frame1, text='sign in', cursor="hand2",
                                font=sign_up_font,
                                bg="white", fg="blue", borderwidth=0, activebackground='white',
                                command=self.button_click_signin)
        sign_up_button.place(x=158, y=268)
        # frame2
        self.frame2_bg_Img = Image.open("images\\signup2.png").resize((400, 550))
        self.foto1 = ImageTk.PhotoImage(self.frame2_bg_Img)
        canvas = Canvas(self.frame2, width=400, height=550)
        canvas.pack()
        canvas.create_image(0, 0, image=self.foto1, anchor='nw')

        back_button_img = CTkImage(Image.open("images\\back.png"), size=(30, 20))
        back_button = CTkButton(self.frame2, image=back_button_img,
                                bg_color="white", text="", border_width=0,
                                fg_color="white", command=self.show_frame1,
                                width=30, hover=False)
        back_button.place(x=0, y=0)

        self.firstname_entry = CTkEntry(self.frame2,
                                        placeholder_text_color="black",
                                        width=330,
                                        height=30,
                                        corner_radius=10,
                                        font=("Arial", 13, "italic"),
                                        bg_color="white",
                                        fg_color="white",
                                        text_color="black",
                                        border_width=1,
                                        border_color="black",
                                        textvariable=self.data["first_name"])
        self.firstname_entry.place(x=35, y=150)

        first_label = Label(self.frame2,
                            text="First Name",
                            font=("Arial", 8, "bold"),
                            fg="black",
                            borderwidth=0,
                            bg="white")
        first_label.place(x=60, y=140)

        self.lastname_entry = CTkEntry(self.frame2,
                                       width=330,
                                       height=30,
                                       corner_radius=10,
                                       font=("Arial", 13, "italic"),
                                       bg_color="white",
                                       fg_color="white",
                                       text_color="black",
                                       border_width=1,
                                       border_color="black",
                                       textvariable=self.data["last_name"])
        self.lastname_entry.place(x=35, y=200)

        last_label = Label(self.frame2,
                           text="Last Name",
                           font=("Arial", 8, "bold"),
                           fg="black",
                           borderwidth=0,
                           bg="white")
        last_label.place(x=60, y=190)

        self.password_entry = CTkEntry(self.frame2,
                                       width=330,
                                       height=30,
                                       corner_radius=10,
                                       font=("Arial", 13, "italic"),
                                       bg_color="white",
                                       fg_color="white",
                                       text_color="black",
                                       border_width=1,
                                       border_color="black",
                                       textvariable=self.data["password"])
        self.password_entry.place(x=35, y=250)

        password_label = Label(self.frame2,
                               text="Password",
                               font=("Arial", 8, "bold"),
                               fg="black",
                               borderwidth=0,
                               bg="white")
        password_label.place(x=60, y=240)

        self.password_entry.bind("<KeyRelease>", self.check_password_strength)

        # Password requirements
        self.password_requirements = [
            "At least 8 characters",
            "Lower case letters (a-z)",
            "Upper case letters (A-Z)",
            "Numbers (0-9)",
            "Special characters (e.g. !@#$%^&*)"
        ]
        self.requirements_labels = []
        for i, requirement in enumerate(self.password_requirements):
            label = ttk.Label(self.frame2, text=requirement, foreground="red", background="white", font=("Arial", 8))
            label.place(x=45, y=280 + i * 20)
            self.requirements_labels.append(label)
        self.cpass_entry = CTkEntry(self.frame2,
                                    width=330,
                                    height=30,
                                    corner_radius=10,
                                    font=("Arial", 13, "italic"),
                                    bg_color="white",
                                    fg_color="white",
                                    text_color="black",
                                    border_width=1,
                                    border_color="black",
                                    textvariable=self.data["confirm_password"])
        self.cpass_entry.place(x=35, y=389)
        cpassword_label = Label(self.frame2,
                                text="Confirm Password",
                                font=("Arial", 8, "bold"),
                                fg="black",
                                borderwidth=0,
                                bg="white")
        cpassword_label.place(x=60, y=381)

        self.accept_terms_var = IntVar()
        accept_terms_checkbox = ttk.Checkbutton(self.frame2, text="",
                                                variable=self.accept_terms_var, )
        accept_terms_checkbox.place(x=40, y=430)

        createacc_b = CTkButton(self.frame2,
                                text="Create Account",
                                width=330,
                                height=50,
                                corner_radius=10,
                                font=("Arial", 17, "bold"),
                                bg_color="white",
                                fg_color="black",
                                text_color="white",
                                border_color="black",
                                hover_color="#4D4B4B",
                                command=self.create_account)
        createacc_b.place(x=35, y=470)

        self.error_label_email = ttk.Label(self.frame1, text="", foreground="red", background="white")
        self.error_label_email.place(x=27, y=120)

        self.error_label = ttk.Label(self.frame2, text="", foreground="red", background="white")
        self.error_label.place(x=27, y=120)

    def show_frame1(self):
        self.frame1.tkraise()

    def show_frame2(self):
        self.frame2.tkraise()

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

        if self.accept_terms_var.get() == 0:
            self.error_label.config(text="You must accept the terms of service to create an account.")
            return

        self.persondataopen()

    def continu(self):
        self.resetborder()
        self.error_label_email.config(text="")
        empty_fields = [key for key, var in self.data_email.items() if not var.get().strip()]
        if empty_fields:
            self.error_label_email.config(text="Please fill the email fields.")
            for field in empty_fields:
                if field == "email":
                    self.email_entry.configure(border_color="red")
            return
        else:
            self.show_frame2()

    def reset_borders(self):
        self.firstname_entry.configure(border_color="black")
        self.lastname_entry.configure(border_color="black")

        self.password_entry.configure(border_color="black")
        self.cpass_entry.configure(border_color="black")

    def resetborder(self):
        self.email_entry.configure(border_color="black")

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
        win = CTkToplevel()
        login2.Login(win)
        self.master.withdraw()
        win.deiconify()

    def persondataopen(self):
        persondata.App(self.master)
        self.master.withdraw()


    @staticmethod
    def text_to_speech_signin():
        speech = gTTS(text="For sign in tap here again", lang='en')
        filepath = "audio\\login.mp3"
        speech.save(filepath)
        try:
            playsound.playsound(filepath)
        except playsound.PlaysoundException:
            print("Error playing audio file")
        finally:
            os.remove(filepath)

    def button_click_signin(self):
        if self.click_count % 2 == 0:
            self.text_to_speech_signin()
        else:
            self.login()
        self.click_count += 1
    def submitdata(self):
        first_name = self.firstname_entry.get()
        last_name = self.lastname_entry.get()
        nama_lengkap = first_name + " " + last_name
        self.acc = Account(email=self.email_entry.get(),
                           fullname=nama_lengkap,
                           password=self.cpass_entry.get())

        data_acc = [self.acc.email,self.acc.fullname,self.acc.password]

        return data_acc

if __name__ == "__main__":
    root = CTk()
    Signup(root)
    root.mainloop()
