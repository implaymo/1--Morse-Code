import tkinter as tk

class UI():
    def __init__(self, morse_code_dict):
        self.morse_code_dict = morse_code_dict
        
        
        self.window = tk.Tk()
        self.window.title("Morse Code Converter")
        self.window.geometry("300x300")
        
        self.text = tk.Label(self.window, text="Convert text to Morse Code!")
        self.text.grid(column=1, row=0)
        
        self.input = tk.Label(self.window, text="Input your text: ")
        self.input.grid(column=0, row=1)
        
        self.result = tk.Label(self.window, text="Morse Code: ")
        self.result.grid(column=0, row=2)
        
        self.morse_code_result = tk.Label(self.window)
        self.morse_code_result.grid(column=1, row=2)
        
        self.string_entry = tk.Entry(self.window)
        self.string_entry.grid(column=1, row=1)
        
        
        self.converter_button = tk.Button(self.window, text="Convert", command=self.string_to_morse_code)
        self.converter_button.grid(column=1, row=3)
        
        
        self.window.mainloop()


    def string_to_morse_code(self):
        user_input = self.string_entry.get()
        final_code = [self.morse_code_dict[letter] for letter in user_input.upper()]
        morse_code = ''.join(final_code)
        self.morse_code_result.config(text=f"{morse_code}")
        
        