import tkinter as tk
from tkinter import messagebox
import random


class DiceSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Symulacja rzutu kostką")
        self.root.geometry("400x400")

        self.result_label = tk.Label(root, text="Kliknij, aby rzucić kostką!", font=("Arial", 16))
        self.result_label.pack(pady=30)

        self.roll_button = tk.Button(root, text="Rzuć kostką", font=("Arial", 14), command=self.roll_dice)
        self.roll_button.pack(pady=20)

        self.dice_images = [
            tk.PhotoImage(file=f"dice_{i}.png") for i in range(1, 7)
        ]
        self.dice_label = tk.Label(root)
        self.dice_label.pack(pady=10)

    def roll_dice(self):
        dice_value = random.randint(1, 6)

        self.result_label.config(text=f"Wynik: {dice_value}")
        self.dice_label.config(image=self.dice_images[dice_value - 1])


if __name__ == "__main__":
    root = tk.Tk()

    try:
        app = DiceSimulator(root)
        root.mainloop()
    except tk.TclError:
        messagebox.showerror("Błąd",
                             "Upewnij się, że pliki obrazków (dice_1.png do dice_6.png) znajdują się w tym samym katalogu, co skrypt.")