import tkinter as tk

from pages.recipes import RecipeBooks
from pages.home import HomePage
from pages.chooser import RecipeChooser
from pages.planner import Calendar
from pages.list import ShoppingList

class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.geometry("1080x2400")

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}

        pages = [
            HomePage,
            RecipeBooks,
            RecipeChooser,
            Calendar,
            ShoppingList
        ]

        for Page in pages:
            frame = Page(container, self)

            self.frames[Page.__name__] = frame

            frame.grid(
                row=0,
                column=0,
                sticky="nsew"
            )

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


app = App()
app.mainloop()
