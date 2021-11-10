import tkinter as tk
from tkinter import ttk

class View(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MQTT Subscriber")
        self.geometry("400x400")
        self.tk.call("source", "mqtt/theme/sun-valley.tcl")
        self.tk.call("set_theme", "light")
        self.setup_layout()
        self.init_frame()


    def setup_layout(self):
        self.rowconfigure(0, weight = 4)
        self.columnconfigure(0, weight = 4)
        self.rowconfigure(1, weight = 1)
        self.columnconfigure(1, weight = 1)


    def init_frame(self):
        entry = self.create_entry_frame(self)
        entry.grid(row= 0, column = 0, sticky= 'nsew', padx= 5, pady= 5)
        buttons = self.create_button_frame(self)
        buttons.grid(row=1, column=0, columnspan=2,sticky= 'nsew', padx= 5, pady= 5)


    def create_entry_frame(self, parent):
        entry_frame = ttk.Entry(parent)
        entry_frame.rowconfigure(0, weight = 1)
        entry_frame.rowconfigure(1, weight = 1)
        entry_frame.rowconfigure(2, weight = 1)
        entry_frame.columnconfigure(0, weight = 1)
        entry_frame.columnconfigure(1, weight = 4)

        self.id_label = ttk.Label(entry_frame, text= "ID:")
        self.id_label.grid(row = 0, column = 0, sticky= 'w', padx= 5, pady= 5)

        self.pass_label = ttk.Label(entry_frame, text= "Password:")
        self.pass_label.grid(row = 1, column = 0, sticky= 'w', padx= 5, pady= 5)

        self.token_label = ttk.Label(entry_frame, text= "Token:")
        self.token_label.grid(row = 2, column = 0, sticky= 'w', padx= 5, pady= 5)        

        self.id_entry = ttk.Entry(entry_frame)
        self.id_entry.grid(row= 0, column= 1, sticky= 'we', padx= 5, pady= 5)

        self.pass_entry = ttk.Entry(entry_frame)
        self.pass_entry.grid(row= 1, column= 1, sticky= 'we', padx= 5, pady= 5)

        self.token_entry = ttk.Entry(entry_frame)
        self.token_entry.grid(row= 2, column= 1, sticky= 'we', padx= 5, pady= 5)

        return entry_frame


    def create_button_frame(self, parent):
        button_frame = ttk.Frame(parent)
        button_frame.rowconfigure (0, weight = 1)
        button_frame.columnconfigure(0, weight = 1)
        button_frame.columnconfigure(1, weight = 1)
        button_frame.columnconfigure(2, weight = 1)
        button_frame.columnconfigure(3, weight = 1)

        self.b1_btn = ttk.Button(button_frame, text="B1")
        self.b1_btn.grid(row = 0, column= 0, sticky= 'nsew', padx= 10, pady= 10) 
        self.b2_btn = ttk.Button(button_frame, text="B2")
        self.b2_btn.grid(row = 0, column= 1, sticky= 'nsew', padx= 10, pady= 10)
        self.b3_btn = ttk.Button(button_frame, text="B3")
        self.b3_btn.grid(row = 0, column= 2, sticky= 'nsew', padx= 10, pady= 10)
        self.send_btn = ttk.Button(button_frame, text="Send")
        self.send_btn.grid(row = 0, column= 3, sticky= 'nsew', padx= 10, pady= 10)

        return button_frame


    def init_window(self):
        self.mainloop()



def main():
    view = View()
    view.init_window()


if __name__=="__main__":
    main()