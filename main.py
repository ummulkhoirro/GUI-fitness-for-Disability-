from tkinter import *
from PIL import Image, ImageTk
from customtkinter import *
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
training2_dir = os.path.join(current_dir, '..', 'TRAINING 2')
training3_dir = os.path.join(current_dir, '..', 'TRAINING 3')
sys.path.append(training2_dir)
sys.path.append(training3_dir)

from sensorictraining import SensoricTraining
from TR import IntelectualMental
from phytraining import PhyTraining

class ChooseTraining: 

    def __init__(self, choose):
        self.choose = choose
        self.click_count = 0
        self.choose.after(1000)
        self.choose.title("FitInclusive")
        height = 720
        width = 1280
        x = (self.choose.winfo_screenwidth() // 2) - (width // 2)
        y = (self.choose.winfo_screenheight() // 4) - (height // 4)
        self.choose.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.choose.resizable(0, 0)
        self.choose.config(bg="#291C4F")
        self.myfont = CTkFont(family='Poppins', size=14, weight='bold', slant='italic')


        title_label = Label(self.choose, text="WHICH ONE ARE YOU?", bg="#291C4F", fg="white", font=("Helvetica", 30, "bold"))
        title_label.pack(pady=(100, 10))

        sub_label = Label(self.choose, text="The aim is to know your workout preferences based on your needs.", bg="#291C4F", fg="white", font=("Helvetica", 18))
        sub_label.pack()

        # Load the image without resizing
        image_path = "D:\\pythonProject1\\pict\\choosetraining.png"# Replace with your image file path
        image = Image.open(image_path)
        image_tk = ImageTk.PhotoImage(image)

        # Create a label to display the image
        image_label = Label(self.choose, image=image_tk, bg="#291C4F")
        image_label.image = image_tk  # Keep a reference to avoid garbage collection
        image_label.pack(pady=(20, 10))  # Adjust padding as needed

        # Create a frame for the buttons and set its width to the desired size
        button_frame = Frame(self.choose, bg="#291C4F", width=image.width, height=50)
        button_frame.pack(pady=(10, 0))
        button_frame.pack_propagate(False)  # Prevent the frame from resizing to fit its children


        def open_phytraining():
            self.choose.destroy()
            new_window = Tk()
            PhyTraining(new_window)  # Buat instance PhyTraining
            new_window.deiconify()

        def open_sensorictraining():
            self.choose.destroy()
            new_window = Tk()
            SensoricTraining(new_window)
            new_window.deiconify()

        def open_intelectualmental():
            self.choose.destroy()
            new_window = Tk()
            IntelectualMental(new_window)
            new_window.deiconify()
        

        # Add CTkButtons to the frame
        left_button = CTkButton(button_frame, text="PHYSIC", font=self.myfont, fg_color="white", text_color="#291C4F", corner_radius=50, command=open_phytraining)
        left_button.pack(side=LEFT, expand=True, fill=BOTH, padx=(0, 10))  # Add padding to the right

        center_button = CTkButton(button_frame, text="INTELECTUAL\nMENTAL", font=self.myfont, fg_color="white", text_color="#291C4F", corner_radius=50, command=open_sensorictraining)
        center_button.pack(side=LEFT, expand=True, fill=BOTH, padx=(10, 10))  # Add padding to the left and right

        right_button = CTkButton(button_frame, text="SENSORIK", font=self.myfont, fg_color="white", text_color="#291C4F", corner_radius=50, command=open_intelectualmental)
        right_button.pack(side=LEFT, expand=True, fill=BOTH, padx=(10, 0))  # Add padding to the left

if __name__ == "__main__":
    root = Tk() 
    app = ChooseTraining(root)
    root.mainloop()
