from tkinter import *
from PIL import Image, ImageTk
from customtkinter import *
from tkinter import ttk
from tkinter import messagebox
import signup1
import persondata
import sqlite3
import mainmenu



class Login:

    def __init__(self, login):
        self.login = login
        self.login.title("Login")
        window_width = 400
        window_height = 550
        screen_width = self.login.winfo_screenwidth()
        screen_height = self.login.winfo_screenheight()
        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)
        self.login.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
        self.login.config(bg="white")

        self.image = Image.open("images\\login.png").resize((400,550))
        self.foto = ImageTk.PhotoImage(self.image)
        self.loginbg = Canvas(self.login,width=400, height=550)
        self.loginbg.pack()
        self.loginbg.create_image(0, 0, image=self.foto, anchor='nw')

        self.email_entry = CTkEntry(self.login,

                                    width=330,
                                    height=50,
                                    corner_radius=10,
                                    font=("Arial", 17, "italic"),
                                    bg_color="white",
                                    fg_color="white",
                                    text_color="black",
                                    border_width=1,
                                    border_color="black",
                                    )
        self.email_entry.place(x=35, y=150)

        email_label = Label(self.login,
                            text="Email Address",
                            font=("Arial", 10, "bold"),
                            fg="black",
                            borderwidth=0,
                            bg="white")
        email_label.place(x=60, y=140)

        self.password_entry = CTkEntry(self.login,
                                    width=330,
                                    height=50,
                                    corner_radius=10,
                                    font=("Arial", 17, "italic"),
                                    bg_color="white",
                                    fg_color="white",
                                    text_color="black",
                                    border_width=1,
                                    border_color="black",
                                    )
        self.password_entry.place(x=35, y=210)

        pass_label = Label(self.login,
                            text="Password",
                            font=("Arial", 10, "bold"),
                            fg="black",
                            borderwidth=0,
                            bg="white")
        pass_label.place(x=60, y=200)

        no_acc_label = CTkButton(self.login,
                                 text="Doesn't have an account ?",
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
        sign_up_button = Button(self.login, text='sign up', cursor="hand2",
                                font=sign_up_font,
                                bg="white", fg="blue", borderwidth=0, activebackground='white',
                                command=self.signup)
        sign_up_button.place(x=196, y=268)

        self.loginbutton = CTkButton(self.login,
                                  text="Login",
                                  width=330,
                                  height=50,
                                  corner_radius=10,
                                  font=("Arial", 17, "bold"),
                                  bg_color="white",
                                  fg_color="black",
                                  text_color="white",
                                  border_color="black",
                                  hover_color="#4D4B4B",
                                  command=self.login1)
        self.loginbutton.place(x=35, y=300)

    def openmainmenu(self):
        win= Toplevel()
        mainmenu.Mainmenu(win)
        self.login.withdraw()
        win.deiconify()



    def signup(self):
        persondata.App(master=self.login)
        self.login.withdraw()

    def login1(self):
        username = self.email_entry.get()
        password = self.password_entry.get()

        user_type, username = login(username, password)
        if user_type == "pengguna":
            messagebox.showinfo("Success", f'Welcome {username}')
            tampilkan_info_login(username)
            self.openmainmenu()
        else:
            messagebox.showerror("Error", "Invalid username or password")


def login(username, password):
    connection = sqlite3.connect("database/fitness.db")
    cursor = connection.cursor()
    find_customer = 'SELECT * FROM pengguna WHERE email = ? AND password = ?'
    cursor.execute(find_customer, (username, password))
    pengguna_result = cursor.fetchall()
    if pengguna_result:
        cursor.execute("UPDATE pengguna SET status_login = 1 WHERE email = ?",
                       (username,))
        connection.commit()
        connection.close()
        return "pengguna", username
    else:
        print("None")

def get_login_info(username):
    connection = sqlite3.connect("database/fitness.db")
    cursor = connection.cursor()

    cursor.execute("SELECT status_login FROM pengguna WHERE email = ?", (username,))
    customer_info = cursor.fetchone()

    connection.close()
    return customer_info


def tampilkan_info_login(username):
    login_info = get_login_info(username)
    if login_info:
        status = login_info
        if status:
            print(f"Pengguna {username} .")
        else:
            print(f"Pengguna {username} tidak sedang login.")
    else:
        print(f"Tidak ada pengguna dengan username {username}.")


if __name__ == "__main__":
    root = CTk()
    app = Login(root)
    root.mainloop()
