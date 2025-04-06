from tkinter import *
from PIL import Image, ImageTk
from customtkinter import CTkButton, CTkEntry, CTkFont, CTkScrollableFrame
from tkinter import messagebox
from gtts import gTTS
import playsound
import os


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
    def __init__(self, signup):
        self.signup = signup
        self.click_count = 0
        self.signup.after(1500,open_signup)
        self.signup.title("Boba Cafe")
        self.signup.rowconfigure(0, weight=1)
        self.signup.columnconfigure(0, weight=1)
        height = 720
        width = 1280
        x = (signup.winfo_screenwidth() // 2) - (width // 2)
        y = (signup.winfo_screenheight() // 4) - (height // 4)
        self.signup.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.signup.resizable(0, 0)
        self.signup.config(bg="#B28C6E")
        self.myfont = CTkFont(family='Poppins', size=12, weight='bold', slant='italic')

        def exitt2():
            sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=self.signup)
            if sure:
                self.signup.destroy()

        self.signup.protocol("WM_DELETE_WINDOW", exitt2)

        self.img1 = Image.open("images\\signup1.png")
        self.img1 = self.img1.resize((1280, 720))
        self.foto = ImageTk.PhotoImage(self.img1)
        self.canva = Canvas(self.signup, width=1366, height=768, bg="black")
        self.canva.pack()
        self.canva.create_image(0, 0, anchor='nw', image=self.foto)

        self.scrframe = CTkScrollableFrame(self.signup,
                                           orientation="vertical",
                                           width=518,
                                           height=350,
                                           fg_color='white',
                                           bg_color='white',
                                           )
        self.scrframe.place(x=627, y=200)
        def text_to_speech1():
            speech = gTTS(text="ENTER YOUR FULLNAME BELOW THE TEXT ", lang='en')
            filepath = "audio\\enter_email_label.mp3"
            speech.save(filepath)
            try:
                playsound.playsound(filepath)
            except playsound.PlaysoundException:
                print("Error playing audio file")
            finally:
                os.remove(filepath)
        enter_fullname_label = CTkButton(self.scrframe,
                                         text="ENTER YOUR FULLNAME BELOW THE TEXT\t\t",
                                         anchor='c',
                                         fg_color='white',
                                         bg_color='white',
                                         height=40,
                                         hover_color='#e9e8e8',
                                         font=self.myfont,
                                         text_color="#291C4F",
                                         command=text_to_speech1)
        enter_fullname_label.pack(pady=10)
        entry_fullname1 = CTkEntry(self.scrframe,
                                   width=380,
                                   height=50,
                                   placeholder_text="Enter your full name",
                                   placeholder_text_color="#4D4C4C",
                                   corner_radius=50,
                                   font=("Arial", 17, "italic"),
                                   bg_color="white",
                                   fg_color="#ECECEC",
                                   text_color="black",
                                   border_color="#ECECEC",
                                   )
        entry_fullname1.pack(pady=10)

        def text_to_speech2():
            speech = gTTS(text="CREATE YOUR USERNAME BELOW THE TEXT", lang='en')
            filepath = "audio\\enter_email_label.mp3"
            speech.save(filepath)
            try:
                playsound.playsound(filepath)
            except playsound.PlaysoundException:
                print("Error playing audio file")
            finally:
                os.remove(filepath)

        enter_username_label = CTkButton(self.scrframe,
                                         text="CREATE YOUR USERNAME BELOW THE TEXT\t\t",
                                         anchor='c',
                                         fg_color='white',
                                         bg_color='white',
                                         height=40,
                                         hover_color='#e9e8e8',
                                         font=self.myfont,
                                         text_color="#291C4F",
                                         command=text_to_speech2)
        enter_username_label.pack(pady=10)

        entry_username2 = CTkEntry(self.scrframe,
                                   width=380,
                                   height=50,
                                   placeholder_text="Create your username",
                                   placeholder_text_color="#4D4C4C",
                                   corner_radius=50,
                                   font=("Arial", 17, "italic"),
                                   bg_color="white",
                                   fg_color="#ECECEC",
                                   text_color="black",
                                   border_color="#ECECEC",
                                   )
        entry_username2.pack(pady=10)

        def text_to_speech3():
            speech = gTTS(text="ENTER YOUR PHONE NUMBER BELOW THE TEXT", lang='en')
            filepath = "audio\\enter_email_label.mp3"
            speech.save(filepath)
            try:
                playsound.playsound(filepath)
            except playsound.PlaysoundException:
                print("Error playing audio file")
            finally:
                os.remove(filepath)

        enter_number_label = CTkButton(self.scrframe,
                                       text="ENTER YOUR PHONE NUMBER BELOW THE TEXT\t",
                                       anchor='c',
                                       fg_color='white',
                                       bg_color='white',
                                       height=40,
                                       hover_color='#e9e8e8',
                                       font=self.myfont,
                                       text_color="#291C4F",
                                       command=text_to_speech3)
        enter_number_label.pack(pady=10)

        entry_number3 = CTkEntry(self.scrframe,
                                 width=380,
                                 height=50,
                                 placeholder_text="Enter your phone number",
                                 placeholder_text_color="#4D4C4C",
                                 corner_radius=50,
                                 font=("Arial", 17, "italic"),
                                 bg_color="white",
                                 fg_color="#ECECEC",
                                 text_color="black",
                                 border_color="#ECECEC",
                                 )
        entry_number3.pack(pady=10)

        def text_to_speech4():
            speech = gTTS(text="ENTER YOUR BIRTHDATE BELOW THE TEXT", lang='en')
            filepath = "audio\\enter_email_label.mp3"
            speech.save(filepath)
            try:
                playsound.playsound(filepath)
            except playsound.PlaysoundException:
                print("Error playing audio file")
            finally:
                os.remove(filepath)

        enter_birth_label = CTkButton(self.scrframe,
                                      text="ENTER YOUR BIRTHDATE BELOW THE TEXT\t\t",
                                      anchor='c',
                                      fg_color='white',
                                      bg_color='white',
                                      height=40,
                                      hover_color='#e9e8e8',
                                      font=self.myfont,
                                      text_color="#291C4F",
                                      command=text_to_speech4)
        enter_birth_label.pack(pady=10)

        entry_birth4 = CTkEntry(self.scrframe,
                                width=380,
                                height=50,
                                placeholder_text="Enter your birthdate",
                                placeholder_text_color="#4D4C4C",
                                corner_radius=50,
                                font=("Arial", 17, "italic"),
                                bg_color="white",
                                fg_color="#ECECEC",
                                text_color="black",
                                border_color="#ECECEC",
                                )
        entry_birth4.pack(pady=10)

        def text_to_speech5():
            speech = gTTS(text="ENTER YOUR GENDER BELOW THE TEXT", lang='en')
            filepath = "audio\\enter_email_label.mp3"
            speech.save(filepath)
            try:
                playsound.playsound(filepath)
            except playsound.PlaysoundException:
                print("Error playing audio file")
            finally:
                os.remove(filepath)

        enter_gender_label = CTkButton(self.scrframe,
                                       text="ENTER YOUR GENDER BELOW THE TEXT\t\t",
                                       anchor='c',
                                       fg_color='white',
                                       bg_color='white',
                                       height=40,
                                       hover_color='#e9e8e8',
                                       font=self.myfont,
                                       text_color="#291C4F",
                                       command=text_to_speech5)
        enter_gender_label.pack(pady=10)

        entry_gender5 = CTkEntry(self.scrframe,
                                 width=380,
                                 height=50,
                                 placeholder_text="What's your gender",
                                 placeholder_text_color="#4D4C4C",
                                 corner_radius=50,
                                 font=("Arial", 17, "italic"),
                                 bg_color="white",
                                 fg_color="#ECECEC",
                                 text_color="black",
                                 border_color="#ECECEC",
                                 )
        entry_gender5.pack(pady=10)

        def text_to_speech6():
            speech = gTTS(text="CREATE YOUR PASSWORD BELOW THE TEXT", lang='en')
            filepath = "audio\\enter_email_label.mp3"
            speech.save(filepath)
            try:
                playsound.playsound(filepath)
            except playsound.PlaysoundException:
                print("Error playing audio file")
            finally:
                os.remove(filepath)

        enter_password_label = CTkButton(self.scrframe,
                                       text="CREATE YOUR PASSWORD BELOW THE TEXT\t\t",
                                       anchor='c',
                                       fg_color='white',
                                       bg_color='white',
                                       height=40,
                                       hover_color='#e9e8e8',
                                       font=self.myfont,
                                       text_color="#291C4F",
                                       command=text_to_speech6)
        enter_password_label.pack(pady=10)

        entry_password6 = CTkEntry(self.scrframe,
                                   width=380,
                                   height=50,
                                   placeholder_text="Emter your password",
                                   placeholder_text_color="#4D4C4C",
                                   corner_radius=50,
                                   font=("Arial", 17, "italic"),
                                   bg_color="white",
                                   fg_color="#ECECEC",
                                   text_color="black",
                                   border_color="#ECECEC",
                                   )
        entry_password6.pack(pady=10)

        def text_to_speech7():
            speech = gTTS(text="ENTER YOUR PASSWORD AGAIN BELOW THE TEXT", lang='en')
            filepath = "audio\\enter_email_label.mp3"
            speech.save(filepath)
            try:
                playsound.playsound(filepath)
            except playsound.PlaysoundException:
                print("Error playing audio file")
            finally:
                os.remove(filepath)

        enter_cpassword_label = CTkButton(self.scrframe,
                                       text="ENTER YOUR PASSWORD AGAIN BELOW THE TEXT\t",
                                       anchor='c',
                                       fg_color='white',
                                       bg_color='white',
                                       height=40,
                                       hover_color='#e9e8e8',
                                       font=self.myfont,
                                       text_color="#291C4F",
                                       command=text_to_speech7)
        enter_cpassword_label.pack(pady=10)

        entry_cpassword7 = CTkEntry(self.scrframe,
                                    width=380,
                                    height=50,
                                    placeholder_text="Confirm your password",
                                    placeholder_text_color="#4D4C4C",
                                    corner_radius=50,
                                    font=("Arial", 17, "italic"),
                                    bg_color="white",
                                    fg_color="#ECECEC",
                                    text_color="black",
                                    border_color="#ECECEC",
                                    )
        entry_cpassword7.pack(pady=10)


if __name__ == "__main__":
    root = Tk()
    Signup(root)
    root.mainloop()
