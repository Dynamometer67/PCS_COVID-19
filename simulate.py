# This file defines a function which can be used to create and simulate an SIR
# model

from sir_model import SIR_model
from gui import GUI
import tkinter as tk
from visualize2 import visualize

def create_and_run():
    model = SIR_model()
    model.run()

def run_and_visualize():
    model = SIR_model()
    S, I, R = model.run()
    visualize(S, "Lol")

if __name__ == "__main__":
    model = SIR_model()

    gui = GUI(model, "COVID-19 Simulation")
    # After this, the GUI has updated the values of the parameters of the model
    # and you can start working with the model.
    gui.start()
    try:
        # Put here what happens when the GUI succeeds.
        results = gui.get_entries()
        print(results)
        model.run()
    except tk.TclError:
        # Put here what happens when the user quits the GUI (without pressing
        # the OK button).
        print("aaaaaaaaaaaaaaaaa")

    # Alternatively, for testing and stuff, you can alter the values of the
    # model here without using the GUI. Simply comment anything GUI related
    # from the above code and uncomment the code below.
    # create_and_run()
    # run_and_visualize()
