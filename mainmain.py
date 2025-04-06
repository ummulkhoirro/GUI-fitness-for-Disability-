import tkinter as tk

from main import ChooseTraining
from phytraining import PhyTraining

class MainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("FitInclusive")
        self.geometry("1280x720")
        self.resizable(0, 0)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (ChooseTraining, PhyTraining):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("ChooseTraining")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
