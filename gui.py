import tkinter as tk

class GUI:
    def __init__(self, model, title):
        """Initiates the GUI. expects a model which ONLY has parameters that
        the user can adjust"""
        self.model = model
        self.root = tk.Tk()
        self.root.title(title)
        self.entry_frame = tk.Frame(master=self.root)
        self.button_frame = tk.Frame(master=self.root)
        self.entries = []

    def start(self):
        """Start the GUI so that the user can easily adjust the parameters of
        the model."""
        self.add_entries()
        self.add_buttons()
        self.entry_frame.grid(row=0, column=0)
        self.button_frame.grid(row=1, column=0)
        self.root.mainloop()

    def add_entry(self, param_name, param_val, row):
        """Make an entry for a parameter. Label the entry with param_name and
        give it a default value of param_val. The argument row means the row in
        the grid in which the entry has to be placed."""
        label = tk.Label(master=self.entry_frame, text=param_name)
        entry = tk.Entry(master=self.entry_frame, width=10)
        entry.insert(0, str(param_val))
        self.entries.append((param_name, entry))
        label.grid(row=row, column=0, padx=5, pady=2)
        entry.grid(row=row, column=1, padx=10, pady=2)

    def add_entries(self):
        """Makes an entry for all parameters in self.model."""
        # If this doesn't work anymore because the model has parameters which
        # the user shouldn't change, add a parameter X to the GUI or this
        # function which indicates the number of parameters that can be altered
        # by the user. Then, you only have to do the first X parameters. For 
        # this to work, update the order of the parameters of the model.
        for i, (name, val) in enumerate(vars(self.model).items()):
            self.add_entry(name, val, i)

    def get_entries(self):
        """Returns the parameter names and their new corresponding values as a
        list of tuples."""
        return [(param_name, entry.get()) for param_name, entry in self.entries]
        
    def entries_to_model(self):
        """Update the parameter values of self.model to match the user input
        from the entries."""
        new_params = self.get_entries()
        for name, val in new_params:
            vars(self.model)[name] = val

    def ok(self):
        """Defines what happens when the user presses the 'OK' button"""
        self.entries_to_model()
        self.root.quit()

    def add_buttons(self):
        """Adds an 'OK' and a 'Quit' button to the GUI."""
        button1 = tk.Button(master=self.button_frame, text="OK",
                command=self.ok)
        button2 = tk.Button(master=self.button_frame, text="Quit",
                command=self.root.destroy)

        button1.grid(row=0, column=0, padx=5, pady=5)
        button2.grid(row=0, column=1, padx=5, pady=5)
