import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt

class BMIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")

        # Create an empty DataFrame to store user data
        self.df = pd.DataFrame(columns=["Name", "Weight(kg)", "Height(cm)", "BMI"])

        # Create GUI elements
        self.label_name = tk.Label(root, text="Name:")
        self.entry_name = tk.Entry(root)

        self.label_weight = tk.Label(root, text="Weight (kg):")
        self.entry_weight = tk.Entry(root)

        self.label_height = tk.Label(root, text="Height (cm):")
        self.entry_height = tk.Entry(root)

        self.btn_calculate = tk.Button(root, text="Calculate BMI", command=self.calculate_bmi)
        self.btn_save = tk.Button(root, text="Save Data", command=self.save_data)
        self.btn_view_history = tk.Button(root, text="View History", command=self.view_history)
        self.btn_plot_trend = tk.Button(root, text="Plot BMI Trend", command=self.plot_trend)

        # Grid layout
        self.label_name.grid(row=0, column=0, padx=10, pady=5)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        self.label_weight.grid(row=1, column=0, padx=10, pady=5)
        self.entry_weight.grid(row=1, column=1, padx=10, pady=5)

        self.label_height.grid(row=2, column=0, padx=10, pady=5)
        self.entry_height.grid(row=2, column=1, padx=10, pady=5)

        self.btn_calculate.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
        self.btn_save.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
        self.btn_view_history.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
        self.btn_plot_trend.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

    def calculate_bmi(self):
        name = self.entry_name.get()
        weight = float(self.entry_weight.get())
        height_cm = float(self.entry_height.get())

        # Convert height from cm to m
        height_m = height_cm / 100

        bmi = round(weight / (height_m ** 2), 2)
        messagebox.showinfo("BMI Result", f"Hello {name}, Your BMI is {bmi}")

        # Append data to DataFrame
        self.df = pd.concat([self.df, pd.DataFrame({"Name": [name], "Weight(kg)": [weight], "Height(cm)": [height_cm], "BMI": [bmi]})], ignore_index=True)

    def save_data(self):
        self.df.to_csv("bmi_data.csv", index=False)
        messagebox.showinfo("Data Saved", "BMI data saved successfully!")

    def view_history(self):
        top = tk.Toplevel()
        top.title("BMI History")

        tree = ttk.Treeview(top)
        tree["columns"] = ("Name", "Weight (kg)", "Height (cm)", "BMI")
        tree.heading("#0", text="Index")
        tree.column("#0", width=50)
        for col in tree["columns"]:
            tree.heading(col, text=col)

        for i, row in self.df.iterrows():
            tree.insert("", "end", text=str(i), values=(row["Name"], row["Weight(kg)"], row["Height(cm)"], row["BMI"]))

        tree.pack(expand=True, fill="both")

    def plot_trend(self):
        plt.figure(figsize=(8, 6))
        plt.plot(self.df.index, self.df["BMI"], marker="o", linestyle="-", color="b")
        plt.title("BMI Trend Analysis")
        plt.xlabel("Index")
        plt.ylabel("BMI")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = BMIApp(root)
    root.mainloop()
