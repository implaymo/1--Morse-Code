import tkinter as tk

class UI():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Morse Code Converter")
        self.window.geometry("200x200")
        
        
        self.string_entry = tk.Entry(self.window).grid(column=0, row=1)
        
        self.converter_button = tk.Button(self.window, text="Convert").grid(column=0, row=2)
        
        
        self.window.mainloop()
    
app = UI()
