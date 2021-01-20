# This file defines a class for an SIR model
import numpy as np
from scipy.integrate import odeint

class SIR_model:
    def __init__(self, S0=999, I0=1, R0=0, t0=0, t_max=160, growth_rate=0.2,
            recovery_rate=0.1, vaccinated=0.0, vaccine_efficacy=0.95,
            mask_coverage=0.0, mask_efficacy=0.0, cm_thresh_low=0.25,
            cm_thresh_med=0.5, cm_thresh_high=0.75):
        """This method initiates the SIR model. In this model, S is the amount
        of people susceptible to the virus, I the amount of infected and R the
        amount of recovered or dead people."""
        # Adjustable by the user
        self.S0 = S0
        self.I0 = I0
        self.R0 = R0
        self.t0 = t0
        self.t_max = t_max
        self.growth_rate = growth_rate
        self.rec_rate = recovery_rate
        self.vacc = vaccinated
        self.vacc_eff = vaccine_efficacy
        self.mask_cov = mask_coverage
        self.mask_eff = mask_efficacy
        # self.adjustable = [("S0", "S0"), ("I0", "I0"), ("R0", "R0"),
        #         ("t0", "t0"), ("t_max", "t_max"), ("vaccinated", "vacc"),
        #         ("vaccine_efficacy", "vacc_eff"), ("mask_coverage", "mask_cov"),
        #         ("mask_efficacy", "mask_eff")]
        # self.death_rate = 0.015

    def mask_factor(self):
        C_mask = self.mask_eff * self.mask_cov
        return 1 - 1.75 * C_mask + 0.75 * C_mask**2

    def run(self):
        """This method runs the simulation of the model."""
        self.t = np.linspace(self.t0, self.t_max, self.t_max - self.t0 + 1)
        self.N = self.S0 + self.I0 + self.R0
        self.beta = self.growth_rate * self.mask_factor()

        self.S, self.I, self.R = \
                odeint(self.deriv, [self.S0, self.I0, self.R0], self.t).T

    def deriv(self, y, t):
        S, I, R = y
        return self.dS(S, I), self.dI(S, I), self.dR(I)

    def dS(self, S, I):
        """Calculates the difference in the amount of susceptible people for
        a single timestep."""
        return -self.growth_rate * (S * I / self.N)

    def dI(self, S, I):
        """Calculates the difference in the amount of infected people for
        a single timestep."""
        return -self.dS(S, I) - self.dR(I)

    def dR(self, I):
        """Calculates the difference in the amount of recovered/dead people for
        a single timestep."""
        return self.rec_rate * I

    def show_results(self):
        """When the simulation is over, this method can be used to visualize
        the results of the simulation."""
        pass

    def visualize(self):
        """This method can be used to visualize the simulation while it is
        running."""
        pass
