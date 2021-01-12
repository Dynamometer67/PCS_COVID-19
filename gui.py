import tkinter as tk

class GUI:
    def __init__(self, model, title="COVID-19 Simulation"):
        self.model = model
        self.root = tk.Tk()
        self.root.title(title)
        self.entry_frame = tk.Frame(master=self.root)
        self.button_frame = tk.Frame(master=self.root)
        self.entries = []

    def start(self):
        self.add_buttons()
        self.entry_frame.grid(row=0, column=0)
        self.button_frame.grid(row=1, column=0)
        self.root.mainloop()

    def add_entry(self, param_name):
        label = tk.Label(master=self.entry_frame, text=param_name)
        entry = tk.Entry(master=self.entry_frame, width=10)
        self.entries.append(entry)
        label.grid(row=0, column=0)
        entry.grid(row=0, column=1)

    def get_entries(self):
        return [entry.get() for entry in self.entries]

    def add_buttons(self):
        button1 = tk.Button(master=self.button_frame, text="OK",
                command=self.root.quit)
        button2 = tk.Button(master=self.button_frame, text="Quit",
                command=self.root.destroy)

        button1.grid(row=0, column=0, padx=5, pady=5)
        button2.grid(row=0, column=1, padx=5, pady=5)
