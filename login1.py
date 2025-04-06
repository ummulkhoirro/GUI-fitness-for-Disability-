from tkinter import *
from PIL import Image, ImageTk
from customtkinter import CTkButton, CTkEntry, CTkFont
from tkinter import messagebox
from gtts import gTTS
import playsound
import os
import signup2


def tts_login():
    speech = gTTS(text="Welcome to login page", lang='en')
    filepath = "audio\\login.mp3"
    speech.save(filepath)
    try:
        playsound.playsound(filepath)
    except playsound.PlaysoundException:
        print("Error playing audio file")
    finally:
        os.remove(filepath)


def open_login():
    tts_login()


class Loginpage:
    def __init__(self, loginpage):
        self.loginpage = loginpage
        self.click_count = 0
        self.click_count1 = 0
        self.loginpage.after(1000, open_login)
        self.loginpage.title("Boba Cafe")
        self.loginpage.rowconfigure(0, weight=1)
        self.loginpage.columnconfigure(0, weight=1)
        height = 720
        width = 1280
        x = (loginpage.winfo_screenwidth() // 2) - (width // 2)
        y = (loginpage.winfo_screenheight() // 4) - (height // 4)
        self.loginpage.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.loginpage.resizable(0, 0)
        self.loginpage.config(bg="#B28C6E")
        self.myfont = CTkFont(family='Poppins', size=21, weight='bold')

        def exitt2():
            def tts_exit():
                speech = gTTS(text="Are you sure want to exit", lang='en')
                filepath = "audio\\login.mp3"
                speech.save(filepath)
                try:
                    playsound.playsound(filepath)
                except playsound.PlaysoundException:
                    print("Error playing audio file")
                finally:
                    os.remove(filepath)
            tts_exit()
            sure = messagebox.askyesno("Exit","Are you sure you want to exit?" ,parent=self.loginpage, )
            if sure:
                self.loginpage.destroy()
        self.loginpage.protocol("WM_DELETE_WINDOW", exitt2)

        self.img1 = Image.open("images\\login2.png")
        self.img1 = self.img1.resize((1280, 720))
        self.foto = ImageTk.PhotoImage(self.img1)
        self.canva = Canvas(self.loginpage, width=1366, height=768, bg="black")
        self.canva.pack()
        self.canva.create_image(0, 0, anchor='nw', image=self.foto)

        def text_to_speech1():
            speech = gTTS(text="PLEASE ENTER YOUR USERNAME OR YOUR PHONE NUMBER BELOW THE TEXT ", lang='en')
            filepath = "audio\\enter_email_label.mp3"
            speech.save(filepath)
            try:
                playsound.playsound(filepath)
            except playsound.PlaysoundException:
                print("Error playing audio file")
            finally:
                os.remove(filepath)

        enter_email_label = CTkButton(self.loginpage,
                                      text="Username \t\t\t",
                                      anchor='c',
                                      fg_color='white',
                                      bg_color='white',
                                      height=40,
                                      hover_color='#e9e8e8',
                                      font=self.myfont,
                                      text_color="#291C4F",
                                      command=text_to_speech1)
        enter_email_label.place(x=721, y=235)

        def text_to_speech2():
            speech = gTTS(text="PLEASE ENTER YOUR PASSWORD BELOW THE TEXT", lang='en')
            filepath = "audio\\enter_password_label.mp3"
            speech.save(filepath)
            try:
                playsound.playsound(filepath)
            except playsound.PlaysoundException:
                print("Error playing audio file")
            finally:
                os.remove(filepath)

        enter_password_label = CTkButton(self.loginpage,
                                         text="Password\t\t\t",
                                         anchor='c',
                                         fg_color='white',
                                         bg_color='white',
                                         height=40,
                                         hover_color='#e9e8e8',
                                         font=self.myfont,
                                         text_color="#291C4F",
                                         command=text_to_speech2)
        enter_password_label.place(x=721, y=354)
        entry_username = CTkEntry(self.loginpage,
                                  width=380,
                                  height=50,
                                  placeholder_text="Masukkan Username atau Email",
                                  placeholder_text_color="#4D4C4C",
                                  corner_radius=50,
                                  font=("Arial", 17, "italic"),
                                  bg_color="white",
                                  fg_color="#ECECEC",
                                  text_color="black",
                                  border_color="#ECECEC",
                                  )
        entry_username.place(x=721, y=285)
        entry_password = CTkEntry(self.loginpage,
                                  width=380,
                                  height=50,
                                  placeholder_text="Masukkan password",
                                  placeholder_text_color="#4D4C4C",
                                  corner_radius=50,
                                  font=("Arial", 17, "italic"),
                                  bg_color="white",
                                  fg_color="#ECECEC",
                                  text_color="black",
                                  border_color="#ECECEC",
                                  )
        entry_password.place(x=721, y=404)

        button_login = CTkButton(self.loginpage,
                                 text="Sign in ",
                                 font=("Roboto", 25, 'bold'),
                                 width=200,
                                 height=55,
                                 corner_radius=10,
                                 bg_color="white",
                                 fg_color="#291C4F",
                                 hover_color="#6C54B2",
                                 command=self.button_click_signin)
        button_login.place(x=854, y=501)

        def text_to_speech3():
            speech = gTTS(text="Does not have an account ?", lang='en')
            filepath = "audio\\enter_password_label.mp3"
            speech.save(filepath)
            try:
                playsound.playsound(filepath)
            except playsound.PlaysoundException:
                print("Error playing audio file")
            finally:
                os.remove(filepath)

        no_acc_label = CTkButton(self.loginpage,
                                 text="Does not have an account ?",
                                 anchor='c',
                                 fg_color='white',
                                 bg_color='white',
                                 height=40,
                                 hover_color='#e9e8e8',
                                 font=("Helvetica", 17),
                                 text_color="#291C4F",
                                 command=text_to_speech3)
        no_acc_label.place(x=792, y=130)
        sign_up_font = CTkFont(family="DM Sans", size=17, underline=True)
        sign_up_button = Button(self.loginpage, text='sign up', cursor="hand2",
                                font=sign_up_font,
                                bg="white", fg="blue", border=0, activebackground='white',
                                command=self.button_click_signup)
        sign_up_button.place(x=1002, y=135)

    def signup(self):
        win = Toplevel()
        signup.Signup(win)
        self.loginpage.withdraw()
        win.deiconify()

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

    @staticmethod
    def text_to_speech_signup():
        speech = gTTS(text="For signup tap here again", lang='en')
        filepath = "audio\\signup.mp3"
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
            self.main_function_signin()
        self.click_count += 1

    def button_click_signup(self):
        if self.click_count1 % 2 == 0:
            self.text_to_speech_signup()
        else:
            self.main_function_signup()
        self.click_count1 += 1

    def main_function_signin(self):
        # Fungsi utama yang ingin Anda eksekusi setelah tombol diklik dua kali
        messagebox.showinfo("Info", "Ini adalah fungsi utama setelah tombol diklik dua kali")

    def main_function_signup(self):
        self.signup()


if __name__ == "__main__":
    root = Tk()
    Loginpage(root)
    root.mainloop()
