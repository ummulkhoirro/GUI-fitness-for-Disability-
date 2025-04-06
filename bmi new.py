import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# creating an object
root = tk.Tk()

# setting title and geometry
root.title("BMI Calculator")
root.geometry("1280x720")

# background color for window
root.config(bg="lightblue")

# BMI Calculation
def bmi():
    Height = float(height.get())
    Weight = float(weight.get())
    m = Height / 100  # converting height into meter
    B = round(float(Weight / m ** 2), 1)  # calculating
    label.config(text=B)  # displaying

    # Menyimpan data ke dalam file
    with open("user_data.txt", "w") as file:
        file.write(f"{Height},{Weight},{B}")

    if B < 18.5:
        result_text = f'{B}\nUnderweight\nYou need to gain weight'
    elif 18.5 <= B <= 24.9:
        result_text = f'{B}\nNormal\nYou are all ok! :)'
    elif 25 <= B <= 29.9:
        result_text = f'{B}\nOverweight\nYou need to lose weight slightly'
    elif 30 <= B <= 34.9:
        result_text = f'{B}\nObese\nYou should lose weight'
    else:
        result_text = f'{B}\nExtremely Obese\nYou need to consult with a doctor'

    label1.config(text=result_text)

def main():
    try:
        with open("user_data.txt", "r") as file:
            data = file.read().split(",")
            height.set(data[0])
            weight.set(data[1])
            label.config(text=data[2])
            # Update man image if needed
            update_man_image()
    except FileNotFoundError:
        pass  # File tidak ditemukan, biarkan nilai default

def get_current(event):
    height.set('{:.0f}'.format(current.get()))
    update_man_image()

def get_current2(event):
    weight.set('{:.0f}'.format(current2.get()))

def update_man_image():
    size = int(float(height.get()))
    img = Image.open("D:\\PJ 2\\gambar\\man.png")
    resize = img.resize((50, 10 + size))
    p = ImageTk.PhotoImage(resize)
    man.config(image=p)
    man.image = p
    man.place(x=280, y=630 - size)

# Heading label
top = tk.Label(root, text="BMI CALCULATOR", font=("arial", 25, "bold"), width=500, bd=10, bg="white")
top.place(x=0, y=0)

# Bottom box
tk.Label(root, width=720, height=30, bg="lightcyan").pack(side="bottom")

# two boxes
box = tk.PhotoImage(file="D:\\PJ 2\\gambar\\box.png")
tk.Label(root, image=box).place(x=380, y=100)
tk.Label(root, image=box).place(x=650, y=100)

# scale
scale = tk.PhotoImage(file="D:\\PJ 2\\gambar\\scale.png")
tk.Label(root, image=scale, bg="lightcyan").place(x=200, y=380)

# slider 1
current = tk.DoubleVar()
slider_h = ttk.Scale(root, from_=0, to=220, orient="horizontal", command=get_current, variable=current)
slider_h.place(x=445, y=230)

# slider 2
current2 = tk.DoubleVar()
slider_w = ttk.Scale(root, from_=0, to=200, orient="horizontal", command=get_current2, variable=current2)
slider_w.place(x=710, y=230)

# Entry widget for height
height = tk.StringVar()
weight = tk.StringVar()
h = tk.Entry(root, textvariable=height, width=5, font=("arial", 50), bg="white", fg="black", bd=0,
             justify="center")
h.place(x=400, y=140)

# Entry widget for weight
w = tk.Entry(root, textvariable=weight, width=5, font=("arial", 50), bg="white", fg="black", bd=0,
             justify="center")
w.place(x=665, y=140)

# man
man = tk.Label(root, bg="lightcyan")
man.place(x=70, y=530)

# Label widget for Height
height_label = tk.Label(root, text="Height", font=("Arial", 12), bg="white", fg="black")
height_label.place(x=400, y=110)

# Label widget for Weight
weight_label = tk.Label(root, text="Weight", font=("Arial", 12), bg="white", fg="black")
weight_label.place(x=665, y=110)

# button for report
tk.Button(root, text="Hasil", width=15, height=2, font=("Arial", 10, "bold"), bg="#1f6e68", fg="white",
          command=bmi).place(x=1100, y=360)

# label widget for showing calculated BMI
label = tk.Label(root, font=("arial", 50, "bold"), bg="lightcyan", fg="red")
label.place(x=900, y=340)

# Label widget for showing message
label1 = tk.Label(root, font=("arial", 20, "bold"), bg="lightcyan", fg="black", width=50)
label1.place(x=500, y=500)

# Memuat data saat aplikasi dimulai
if __name__ == "__main__":
    main()

# event loop
root.mainloop()
