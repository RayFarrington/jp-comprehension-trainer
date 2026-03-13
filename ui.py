import tkinter as tk
from logic import get_message

class AppUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Language Comprehension Training")
        self.root.geometry("300x150")

        self.label = tk.Label(self.root, text="Press the button")
        self.label.pack(pady=10)

        self.hiragana_button = tk.Button(
            self.root,
            text="Hiragana",
            command=lambda: self.on_click("hiragana")
        )
        self.hiragana_button.pack()
        self.kanji_button = tk.Button(
                self.root,
                text="Kanji",
                command=lambda: self.on_click("kanji")
                )
        self.kanji_button.pack()

    def on_click(self, opt):
        message = get_message(opt)
        self.label.config(text=message)

    def run(self):
        self.root.mainloop()
