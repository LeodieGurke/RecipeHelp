import tkinter as tk
import os

class HomePage:
    root = tk.Tk()
    root.title("HomePage")
    root.geometry("324x720")

    label = tk.Label(root, text = "Ready to organize your week?", font=('Arial', 16))
    label.pack()

    def openRecipes():
        os.recipes
    button=tk.Button(root, text = "Recipe Book", command = openRecipes)
    button.pack()

print("yo mama")

root.mainloop()