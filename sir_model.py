# -----------------------------------------------------------------------------
# Jesse van den Berge - 12410241
# Mark van Hofwegen   - 12378348
#
# This file contains the main SIR model for this project.
# -----------------------------------------------------------------------------

import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt


def find_max(S, I, R):
    """This method finds the maximum number out of all three arrays."""
    max = np.array([S, I, R])
    return np.max(max)


class SIR_model:
    def __init__(self, S0=10**6, I0=10**3, R0=0, t_max=150, growth_rate=0.4,
                 rec_rate=0.1, mask_cov=0.0, mask_eff=0.0, stochastic=1.0):
        """This method initiates the SIR model. In this model, S0 is the
        initial amount of people susceptible to the virus, I0 the amount of
        infected and R0 the amount of recovered or dead people. t_max is the
        amount of timesteps. growth_rate indicates how easily the virus
        spreads. rec_rate means how many of the infected move to recovered
        every timestep. mask_cov means the amount of people wearing mouth masks
        and mask_eff means how effective those masks are. stochastic is used
        to indicate whether the model is stochastic or not."""
        self.S0 = S0
        self.I0 = I0
        self.R0 = R0
        self.t_max = t_max
        self.growth_rate = growth_rate
        self.rec_rate = rec_rate
        self.mask_cov = mask_cov
        self.mask_eff = mask_eff
        self.stochastic = stochastic


    def mask_factor(self):
        """This method is to calculate the mask_factor based on the given
        mask coverage and mask efficacy."""
        C_mask = self.mask_eff * self.mask_cov
        return 1 - 1.75 * C_mask + 0.75 * C_mask**2


    def run(self):
        """This method runs the simulation of the model. When the simulation is
        done, arrays containing the values for S, I and R at every timestep are
        put into self.S, self.I and self.R respectively."""
        self.t_max = int(self.t_max)
        self.t = np.linspace(0, self.t_max, self.t_max + 1)
        self.N = self.S0 + self.I0 + self.R0
        self.beta = self.growth_rate * self.mask_factor()

        if self.stochastic:
            self.euler_maruyama()
        else:
            self.run_ODEs()


    def run_ODEs(self):
        """Computes the values for S, I and R at every timestep"""
        self.S, self.I, self.R = \
                odeint(self.step, [self.S0, self.I0, self.R0], self.t).T


    def step(self, y, t):
        """Computes a single step for the non-stochastic model. y is a list or
        tuple containing the values for S, I and R in that order. t is the
        array of timestamps. t is not used in this function, but this function
        is used for scipy.integrate.odeint, which requires a function to take
        these parameters."""
        S, I, R = y
        dS = self.dS(S, I)
        dI = self.dI(S, I)
        dR = self.dR(I)

        return dS, dI, dR


    def dS(self, S, I):
        """Calculates the difference in the amount of susceptible people for
        a single timestep."""
        return -self.beta * (S * I / self.N)


    def dI(self, S, I):
        """Calculates the difference in the amount of infected people for
        a single timestep."""
        return -self.dS(S, I) - self.dR(I)


    def dR(self, I):
        """Calculates the difference in the amount of recovered/dead people for
        a single timestep."""
        return self.rec_rate * I


    def noise(self, dX, mu, sigma_factor, X):
        sigma = min(abs(sigma_factor * dX), abs(0.1 * self.N))
        noise = np.random.normal(mu, sigma)
        new_X = X + dX + noise

        if new_X > self.N:
            return self.N - (X + dX)
        if new_X < 0:
            return -(X + dX)
        if abs(noise) > abs(dX):
            return dX if abs(noise + dX) == abs(noise) + abs(dX) else -dX
        return noise


    def euler_maruyama(self):
        """
        https://www.math.kit.edu/ianm3/lehre/nummathfin2012w/media/euler_maruyama.pdf
        https://en.wikipedia.org/wiki/Euler%E2%80%93Maruyama_method
        """
        self.S = np.zeros(self.t.shape)
        self.I = np.zeros(self.t.shape)
        self.R = np.zeros(self.t.shape)
        self.S[0] = self.S0
        self.I[0] = self.I0
        self.R[0] = self.R0
        mu = 0.0
        sigma_factor = 0.5

        for i in range(1, len(self.t)):
            dS = self.dS(self.S[i-1], self.I[i-1])
            dI = self.dI(self.S[i-1], self.I[i-1])
            dR = self.dR(self.I[i-1])
            S_noise = self.noise(dS, mu, sigma_factor, self.S[i-1])
            R_noise = self.noise(dR, mu, sigma_factor, self.R[i-1])

            self.S[i] = self.S[i-1] + dS + S_noise
            self.I[i] = self.I[i-1] + dI - S_noise - R_noise
            self.R[i] = self.R[i-1] + dR + R_noise


    def plot_SIR(self, t, S, I, R, title, max_number, animated=False):
        """Method to visualize the simulation with certain parameters.
        Animated can be changed to "True" if the amount of S, I or R needs to
        be known. Max_number is the largest number out of S, I and R."""
        S_label = "Susceptible"
        I_label = "Infected"
        R_label = "Recovered"

        if animated:
            S_label += ": " + str(int(S[-1]))
            I_label += ": " + str(int(I[-1]))
            R_label += ": " + str(int(R[-1]))

        plt.plot(t, S, 'b-', label=S_label)
        plt.plot(t, I, 'r-', label=I_label)
        plt.plot(t, R, 'g-', label=R_label)

        plt.xlabel('Time (days)')
        plt.ylabel('Cases')
        plt.title(title)
        plt.xlim(0, self.t_max)
        plt.ylim(0, max_number + 0.05 * max_number)
        plt.ticklabel_format(axis="y", style="sci", scilimits=(0,3))
        plt.legend()


    def show_results(self, title, figname=None):
        """When the simulation is over, this method can be used to visualize
        the results of the simulation."""
        max_number = find_max(self.S, self.I, self.R)
        self.plot_SIR(self.t, self.S, self.I, self.R, title, max_number)

        if figname:
            plt.savefig("images/" + figname + ".svg")
        plt.show()


    def visualize(self, title):
        """This method can be used to visualize the simulation step by step."""
        max_number = find_max(self.S, self.I, self.R)
        # Loop over the entire t_max span, then draw the graph for every
        # given t. After this is done, clear the plot and draw t+1.
        for i in range(1, self.t_max + 1):
            t = np.linspace(0, i, num=i+1)
            y_s = self.S[:i+1]
            y_i = self.I[:i+1]
            y_r = self.R[:i+1]

            self.plot_SIR(t, y_s, y_i, y_r, title, max_number, animated=True)
            plt.draw()
            plt.pause(0.00001)

            # If the user closes the plot, stop the for loop.
            if not plt.get_fignums():
                break

            # Clear the plot until everything has been drawn.
            if i < self.t_max:
                plt.clf()
            else:
                plt.show()
