# This file defines a function which can be used to create and simulate an SIR
# model

from sir_model import SIR_model
from gui import GUI
import tkinter as tk


if __name__ == "__main__":
    model = SIR_model()

    # gui = GUI(model, "COVID-19 Simulation")
    # # After this, the GUI has updated the values of the parameters of the model
    # # and you can start working with the model.
    # gui.start()
    try:
        # Put here what happens when the GUI succeeds.
        model.run()
        model.visualize("SIR simulation of COVID-19 spread", save=False)
    except tk.TclError:
        # Put here what happens when the user quits the GUI (without pressing
        # the OK button).
        print("aaaaaaaaaaaaaaaaa")
