import tkinter as tk
import os

class HomePage:
    root = tk.Tk()
    root.title("HomePage")
    root.geometry("324x720")

    frame = tk.Frame (root,bg="blue",bd=5)
    frame.pack(padx=10,pady=20)

    label = tk.Label(frame, text = "Ready to organize your week?", font=('Arial', 16))
    label.pack(pady=(20,0))

    def openRecipes():
        os.recipes
    button=tk.Button(frame, text = "Recipe Book", command = openRecipes)
    button.pack(pady=(20,0))


    root.mainloop()