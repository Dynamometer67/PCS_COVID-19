# This file defines a function which can be used to create and simulate an SIR
# model

from sir_model import SIR_model
from gui import GUI
import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib import ticker


def get_mask_eff_data(growth_rate=0.4, rec_rate=0.1):
    total_I_vals = []
    mask_eff_vals = np.linspace(0.0, 1.0, 101)

    for mask_eff in mask_eff_vals:
        model = SIR_model(mask_cov=0.95, mask_eff=mask_eff, t_max=365,
                I0=10**5, S0=10**6, rec_rate=rec_rate, growth_rate=growth_rate)
        model.run()
        total_I_vals.append(int(model.I[-1] + model.R[-1]))

    return mask_eff_vals, np.array(total_I_vals)


def find_infl_point(y):
    y_diff_2 = np.diff(y, n=2)
    for i in range(1, len(y_diff_2)):
        if y_diff_2[i-1] * y_diff_2[i] <= 0:
            return i - 1
    return None


def get_infl_points():
    infl_points = []
    for rec_rate in np.linspace(0.05, 0.25, 5):
        for growth_rate in np.linspace(0.1, 0.5, 5):
            x, y = get_mask_eff_data(growth_rate, rec_rate)
            i = find_infl_point(y)
            if i :
                infl_points.append(x[i])
                print("rec_rate = " + str(rec_rate) + ", growth_rate = " +
                    str(growth_rate) + ", infl_point = " + str(x[i]))


def visualize_mask_eff(figname=None):
    mask_eff, total_I = get_mask_eff_data()
    plt.plot(mask_eff, total_I, 'r-')
    plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
    plt.title("Influence of mask efficacy on infected")
    plt.xlabel("Mask efficacy")
    plt.ylabel("Total Infected")
    if figname:
        plt.savefig("images/" + figname + ".svg")
    plt.show()


if __name__ == "__main__":
    model = SIR_model(mask_cov=0.95, rec_rate=0.1, growth_rate=0.4, mask_eff=0.65, t_max=150, stochastic=1,
            S0=10**6, I0=10**5)

    # gui = GUI(model, "COVID-19 Simulation")
    # # After this, the GUI has updated the values of the parameters of the model
    # # and you can start working with the model.
    # gui.start()
    try:
        # Put here what happens when the GUI succeeds.
        model.run()
        model.show_results("SIR simulation of COVID-19 spread", save=True, \
                figname="mask_eff_65")
        # model.visualize("SIR simulation of COVID-19 spread")
        # print("Final S: " + str(int(model.S[-1])))
        # print("Final I: " + str(int(model.I[-1])))
        # print("Final R: " + str(int(model.R[-1])))
        # print("Total infected: " + str(int(model.R[-1] + model.I[-1])))
        # visualize_mask_eff("mask_on_infected")
        # visualize_mask_eff()
        # get_infl_points()
    except tk.TclError:
        # Put here what happens when the user quits the GUI (without pressing
        # the OK button).
        print("aaaaaaaaaaaaaaaaa")
