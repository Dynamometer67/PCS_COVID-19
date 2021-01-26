# -----------------------------------------------------------------------------
# Jesse van den Berge - 12410241
# Mark van Hofwegen   - 12378348
#
# This file defines functions which can be used to create and simulate an SIR
# model
# -----------------------------------------------------------------------------

from sir_model import SIR_model
from gui import GUI
import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib import ticker


def get_mask_eff_data(growth_rate=0.4, rec_rate=0.1):
    """This function is used to generate data for one of the figures. It runs a
    simulation of the model for mask_eff values from 0.0 to 1.0 with intervals
    of 0.01. It returns an array of these mask_eff values and an array
    containing I + R at the end of the simulation for every value of mask_eff.
    """
    total_I_vals = []
    mask_eff_vals = np.linspace(0.0, 1.0, 101)

    for mask_eff in mask_eff_vals:
        model = SIR_model(mask_cov=0.95, mask_eff=mask_eff, t_max=365,
                I0=10**5, S0=10**6, rec_rate=rec_rate, growth_rate=growth_rate,
                stochastic=0)
        model.run()
        total_I_vals.append(int(model.I[-1] + model.R[-1]))

    return mask_eff_vals, np.array(total_I_vals)


def find_infl_point(y):
    """finds the first inflection point in the array of values y."""
    y_diff_2 = np.diff(y, n=2)
    for i in range(1, len(y_diff_2)):
        if y_diff_2[i-1] * y_diff_2[i] <= 0:
            return i
    return None


def get_infl_points():
    """Finds the first and only inflection point for the mask_eff_data for
    different values of rec_rate and growth_rate. Whenever a point is found, it
    prints it."""
    for rec_rate in np.linspace(0.05, 0.25, 5):
        for growth_rate in np.linspace(0.1, 0.5, 5):
            x, y = get_mask_eff_data(growth_rate, rec_rate)
            i = find_infl_point(y)

            if i:
                print("rec_rate = " + str(rec_rate) + ", growth_rate = " +
                    str(growth_rate) + ", infl_point = " + str(x[i]))


def visualize_mask_eff(figname=None):
    """visualizes the mask_eff_data by plotting a graph. Also saves the
    resulting figure if a filename is given."""
    mask_eff, total_I = get_mask_eff_data()
    plt.plot(mask_eff, total_I, 'r-')
    plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
    plt.title("Influence of mask efficacy on infected")
    plt.xlabel("Mask efficacy")
    plt.ylabel("Total Infected")

    if figname:
        plt.savefig("images/" + figname + ".svg")
    plt.show()


def extract_noise():
    """This function extracts the noise values by subtracting the
    non-stochastic model from a stochastic model. returns the time array and an
    array containing noise values for S, I and R in that order."""
    model1 = SIR_model(stochastic=0)
    model2 = SIR_model(stochastic=1)

    model1.run()
    model2.run()

    S_noise = model2.S - model1.S
    I_noise = model2.I - model1.I
    R_noise = model2.R - model1.R

    return model1.t, S_noise, I_noise, R_noise


def visualize_noise(figname=None):
    """This function plots the noise values over time. Saves the resulting
    figure with the name figname if figname is given."""
    t, S_noise, I_noise, R_noise = extract_noise()
    plt.plot(t, S_noise, 'b-', label="S noise")
    plt.plot(t, I_noise, 'r-', label="I noise")
    plt.plot(t, R_noise, 'g-', label="R noise")

    plt.ticklabel_format(axis="y", style="sci", scilimits=(0,3))
    plt.title("Visualization of the noise")
    plt.xlabel("Time (days)")
    plt.ylabel("Noise value")
    plt.legend()

    if figname:
        plt.savefig("images/" + figname + ".svg")
    plt.show()


if __name__ == "__main__":
    model = SIR_model(stochastic=0)
    gui = GUI(model, "COVID-19 Simulation")
    # After the following method, the GUI has updated the values of the
    # parameters of the model and you can start working with the model.
    gui.start()
    # Put here what happens when the GUI succeeds.
    model.run()
    model.show_results("SIR simulation of COVID-19 spread")
