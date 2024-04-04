import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")

        self.length_label = ttk.Label(master, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.length_entry = ttk.Entry(master, width=10)
        self.length_entry.grid(row=0, column=1, padx=5, pady=5)

        self.complexity_label = ttk.Label(master, text="Password Complexity:")
        self.complexity_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.complexity_combobox = ttk.Combobox(master, values=["Low", "Medium", "High"])
        self.complexity_combobox.current(1)
        self.complexity_combobox.grid(row=1, column=1, padx=5, pady=5)

        self.generate_button = ttk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.password_label = ttk.Label(master, text="Generated Password:")
        self.password_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.password_entry = ttk.Entry(master, width=30, state="readonly")
        self.password_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        self.copy_button = ttk.Button(master, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def generate_password(self):
        length = self.length_entry.get()
        complexity = self.complexity_combobox.get()

        try:
            length = int(length)
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid password length.")
            return

        if complexity == "Low":
            characters = string.ascii_letters + string.digits
        elif complexity == "Medium":
            characters = string.ascii_letters + string.digits + string.punctuation
        elif complexity == "High":
            characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_entry.config(state="normal")
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
        self.password_entry.config(state="readonly")

    def copy_to_clipboard(self):
        password = self.password_entry.get()
        pyperclip.copy(password)
        messagebox.showinfo("Success", "Password copied to clipboard.")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
