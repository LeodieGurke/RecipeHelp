import tkinter as tk


class MyApp(tk.Frame):

    def __init__(self, root):

        self.colour1 = '#222448'
        self.colour2 = '#54527E'
        self.colour3 = 'WHITE'

        super().__init__(
            root, 
            bg=self.colour1        # frame.pack(padx=10,pady=20)
        )

        self.main_frame = self
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)
        
        self.load_main_widgets()




    def load_main_widgets(self):
        self.create_page_container()
        self.create_pager()

    def create_page_container(self):

        self.page_container = tk.Frame(
            self.main_frame,
            background=self.colour1
        )
         
        self.page_container.columnconfigure(0, weight=1)
        self.page_container.rowconfigure(0, weight=0)
        self.page_container.rowconfigure(1, weight=0)

        self.page_container.grid(column=0, row=0, sticky=tk.NSEW)



    def create_pager(self):

        self.pager = tk.Frame(
            self.main_frame,
            background=self.colour1,
            height=125,
            width=400
        )

        self.pager.columnconfigure(1, weight=1)
        self.pager.rowconfigure(0, weight=1)
        self.pager.grid(column=0, row=1, sticky=tk.NS)
        self.pager.grid_propagate(0)

        prev_button = tk.Button(
            self.pager,
            background=self.colour2,
            foreground=self.colour3,
            activebackground=self.colour2,
            activeforeground=self.colour3,
            disabledforeground='#3B3A56',
            highlightthickness=0,
            width=7,
            relief=tk.FLAT,
            font=('Arial', 18),
            cursor='hand1',
            text='Previous',
            state=tk.DISABLED
        )

        prev_button.grid(column=0, row=0)

        self.page_number =tk.Label(
            self.pager,
            background=self.colour1,
            foreground=self.colour3,
            font=('Arial', 18)
        )

        self.page_number.grid(column=1, row=0)

        next_button = tk.Button(
            self.pager,
            background=self.colour2,
            foreground=self.colour3,
            activebackground=self.colour2,
            activeforeground=self.colour3,
            disabledforeground='#3B3A56',
            highlightthickness=0,
            width=7,
            relief=tk.FLAT,
            font=('Arial', 18),
            cursor='hand1',
            text='Next',
        )

        next_button.grid(column=2, row=0)




root = tk.Tk()
root.title("MyApp")
root.geometry("700x500")
root.resizable(width=False, height=False)
my_app_instance = MyApp(root)
root.mainloop()