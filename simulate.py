# This file defines a function which can be used to create and simulate an SIR
# model

from sir_model import SIR_model
from gui import GUI
import tkinter as tk

def create_and_run():
    model = SIR_model()
    model.run()

if __name__ == "__main__":
    model = SIR_model()
    gui = GUI(model)
    gui.add_entry("X")
    gui.start()
    try:
        results = gui.get_entries()
        print(int(results[0]))
    except tk.TclError:
        print("a")
