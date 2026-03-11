import tkinter as tk
from logic import get_message

class AppUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("My App")
        self.root.geometry("300x150")

        self.label = tk.Label(self.root, text="Press the button")
        self.label.pack(pady=10)

        self.button = tk.Button(
            self.root,
            text="Click",
            command=self.on_click
        )
        self.button.pack()

    def on_click(self):
        message = get_message()
        self.label.config(text=message)

    def run(self):
        self.root.mainloop()
